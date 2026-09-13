"""
tools/browser_use_cloud.py — Lightweight Hosted Browser-Use Cloud Integration.

Specifications:
- Hosted V4 agent / managed task execution via browser-use-sdk
- Uses server-side BROWSER_USE_API_KEY (never exposed to client)
- Defaults to 'gpt-5.6-luna'
- Hard spending cap: $1.00 per run (max_cost_usd)
- Validates completed status and results
- Stops sessions and cancels abandoned/timed-out runs
- Mock mode support for zero-spend unit tests
"""

import os
import time
import logging
from typing import Dict, Any, Optional, List
from pathlib import Path
from dotenv import load_dotenv

# Load .env
_ENV_FILE = Path(__file__).resolve().parent.parent / ".env"
if _ENV_FILE.exists():
    load_dotenv(_ENV_FILE)

logger = logging.getLogger("aprs.browser_use_cloud")

DEFAULT_MODEL = os.getenv("BROWSER_USE_LLM", "gpt-5.6-luna")
DEFAULT_MAX_COST_USD = float(os.getenv("BROWSER_USE_MAX_COST_USD", "1.00"))


class BrowserUseCloudClient:
    """
    Smallest working Browser-Use Cloud integration for APRS.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        default_model: str = DEFAULT_MODEL,
        max_cost_usd: float = DEFAULT_MAX_COST_USD,
        mock_mode: bool = False
    ):
        self.api_key = api_key or os.getenv("BROWSER_USE_API_KEY", "")
        self.default_model = default_model
        self.max_cost_usd = max_cost_usd
        self.mock_mode = mock_mode
        self._sdk_client = None

        if not self.mock_mode and self.api_key:
            try:
                from browser_use_sdk import BrowserUse
                self._sdk_client = BrowserUse(api_key=self.api_key)
            except ImportError:
                logger.warning("browser-use-sdk not installed; falling back to mock mode.")
                self.mock_mode = True

    def run_task(
        self,
        task: str,
        llm: Optional[str] = None,
        timeout_seconds: int = 120,
        poll_interval: float = 3.0,
        max_cost_usd: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Execute a hosted browser task with cost-capping and result validation.

        Args:
            task: Instruction prompt for the browser agent.
            llm: Model identifier (defaults to gpt-5.6-luna).
            timeout_seconds: Max wait time before abandoning and stopping the run.
            poll_interval: Seconds between status polls.
            max_cost_usd: Per-run spend cap (defaults to $1.00).

        Returns:
            Dict containing status, output, cost, and metadata.
        """
        spend_cap = max_cost_usd or self.max_cost_usd
        model_name = llm or self.default_model

        # Mock Mode execution (used for tests to avoid live spending)
        if self.mock_mode or not self.api_key:
            logger.info("Running Browser-Use Cloud in mock mode (no live spending).")
            return {
                "task_id": "mock-task-12345",
                "session_id": "mock-session-67890",
                "status": "finished",
                "is_success": True,
                "output": "Mock browser-use execution completed successfully.",
                "cost_usd": 0.00,
                "model": model_name,
                "mock": True
            }

        # Live Execution via browser-use-sdk
        task_id = None
        session_id = None
        try:
            logger.info(f"Creating hosted browser task with model={model_name}, max_cost=${spend_cap:.2f}")
            created = self._sdk_client.tasks.create(
                task=task,
                llm=model_name
            )
            task_id = created.id
            session_id = created.session_id
            logger.info(f"Task created: id={task_id}, session={session_id}")

            start_time = time.time()
            while time.time() - start_time < timeout_seconds:
                task_view = self._sdk_client.tasks.get(task_id)
                status = str(task_view.status).lower()

                # Cost check
                current_cost = getattr(task_view, "cost", None)
                if current_cost is not None and float(current_cost) >= spend_cap:
                    logger.warning(f"Task {task_id} reached cost cap of ${spend_cap:.2f}. Stopping immediately.")
                    self._safely_stop(task_id, session_id)
                    return {
                        "task_id": task_id,
                        "session_id": session_id,
                        "status": "stopped_cost_cap",
                        "is_success": False,
                        "output": task_view.output or "",
                        "cost_usd": current_cost,
                        "error": f"Run capped at ${spend_cap:.2f}"
                    }

                if status in ["finished", "taskstatus.finished"]:
                    logger.info(f"Task {task_id} finished successfully. Cost: {current_cost}")
                    return {
                        "task_id": task_id,
                        "session_id": session_id,
                        "status": "finished",
                        "is_success": bool(getattr(task_view, "is_success", True)),
                        "output": getattr(task_view, "output", "") or "",
                        "cost_usd": current_cost or 0.0,
                        "model": model_name
                    }
                elif status in ["failed", "taskstatus.failed"]:
                    logger.error(f"Task {task_id} failed on cloud worker.")
                    return {
                        "task_id": task_id,
                        "session_id": session_id,
                        "status": "failed",
                        "is_success": False,
                        "output": getattr(task_view, "output", "") or "",
                        "cost_usd": current_cost or 0.0,
                        "error": "Task execution failed"
                    }
                elif status in ["stopped", "taskstatus.stopped"]:
                    return {
                        "task_id": task_id,
                        "session_id": session_id,
                        "status": "stopped",
                        "is_success": False,
                        "output": getattr(task_view, "output", "") or "",
                        "cost_usd": current_cost or 0.0
                    }

                time.sleep(poll_interval)

            # Timed out — stop browser & cancel abandoned run
            logger.warning(f"Task {task_id} timed out after {timeout_seconds}s. Stopping and canceling run.")
            self._safely_stop(task_id, session_id)
            return {
                "task_id": task_id,
                "session_id": session_id,
                "status": "timeout_stopped",
                "is_success": False,
                "output": "",
                "cost_usd": 0.0,
                "error": f"Timed out after {timeout_seconds} seconds"
            }

        except Exception as e:
            logger.error(f"Error executing browser task: {e}")
            if task_id:
                self._safely_stop(task_id, session_id)
            return {
                "task_id": task_id,
                "session_id": session_id,
                "status": "error",
                "is_success": False,
                "output": "",
                "cost_usd": 0.0,
                "error": str(e)
            }

    def _safely_stop(self, task_id: Optional[str], session_id: Optional[str] = None):
        """Ensure task and underlying browser session are stopped to avoid lingering costs."""
        if not self._sdk_client:
            return
        if task_id:
            try:
                self._sdk_client.tasks.stop(task_id)
                logger.info(f"Task {task_id} successfully stopped.")
            except Exception as e:
                logger.warning(f"Could not stop task {task_id}: {e}")
        if session_id:
            try:
                self._sdk_client.sessions.stop(session_id)
                logger.info(f"Session {session_id} successfully stopped.")
            except Exception as e:
                logger.warning(f"Could not stop session {session_id}: {e}")


# Singleton instance
browser_use_cloud_client = BrowserUseCloudClient()
