import pytest
from unittest.mock import MagicMock, patch
from tools.browser_use_cloud import BrowserUseCloudClient


def test_browser_use_cloud_mock_mode():
    """Test that mock mode returns success without spending or hitting live API."""
    client = BrowserUseCloudClient(api_key="bu_mock_test_key", mock_mode=True)
    res = client.run_task("Search for top trending kitchen gadgets on Amazon")
    
    assert res["status"] == "finished"
    assert res["is_success"] is True
    assert res["cost_usd"] == 0.0
    assert res["mock"] is True
    assert "Mock browser-use execution" in res["output"]


def test_browser_use_cloud_cost_cap_enforcement():
    """Test that run terminates and stops session if cost exceeds cap."""
    client = BrowserUseCloudClient(api_key="bu_mock_test_key", mock_mode=False)
    
    mock_sdk = MagicMock()
    mock_created = MagicMock()
    mock_created.id = "task-cap-1"
    mock_created.session_id = "sess-cap-1"
    mock_sdk.tasks.create.return_value = mock_created

    # Task exceeds cost cap of $1.00
    mock_task_view = MagicMock()
    mock_task_view.status = "started"
    mock_task_view.cost = 1.25
    mock_task_view.output = "Partial progress"
    mock_sdk.tasks.get.return_value = mock_task_view

    client._sdk_client = mock_sdk
    res = client.run_task("Scrape products", max_cost_usd=1.00)

    assert res["status"] == "stopped_cost_cap"
    assert res["is_success"] is False
    mock_sdk.tasks.stop.assert_called_once_with("task-cap-1")
    mock_sdk.sessions.stop.assert_called_once_with("sess-cap-1")


def test_browser_use_cloud_timeout_and_stop():
    """Test that timeout cancels and stops the task and session."""
    client = BrowserUseCloudClient(api_key="bu_mock_test_key", mock_mode=False)
    
    mock_sdk = MagicMock()
    mock_created = MagicMock()
    mock_created.id = "task-to-1"
    mock_created.session_id = "sess-to-1"
    mock_sdk.tasks.create.return_value = mock_created

    mock_task_view = MagicMock()
    mock_task_view.status = "started"
    mock_task_view.cost = 0.10
    mock_sdk.tasks.get.return_value = mock_task_view

    client._sdk_client = mock_sdk
    res = client.run_task("Long scrape", timeout_seconds=1, poll_interval=0.5)

    assert res["status"] == "timeout_stopped"
    assert res["is_success"] is False
    mock_sdk.tasks.stop.assert_called_once_with("task-to-1")
    mock_sdk.sessions.stop.assert_called_once_with("sess-to-1")
