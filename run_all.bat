@echo off
title APRS V6 Pro - All-In-One Runner
echo ===================================================
echo [1/4] Initializing Database Schema...
echo ===================================================
echo NOTE: Fake demo data is NOT auto-loaded.
echo       To seed demo data, run: python tools\seed_market_data.py --demo
.\.venv\Scripts\python.exe -c "from core.database import init_db; init_db(); print('Database schema initialized.')"
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Database initialization failed.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ===================================================
echo [2/4] Running Browser-Use Cloud & Budget Tests...
echo ===================================================
.\.venv\Scripts\pytest.exe tests\test_browser_use_cloud.py -v
if %ERRORLEVEL% neq 0 (
    echo [WARNING] Test failed. Continuing...
)

echo.
echo ===================================================
echo [3/4] Validating Streamlit 9-Tab Dashboard Headless...
echo ===================================================
.\.venv\Scripts\python.exe -c "from streamlit.testing.v1 import AppTest; at = AppTest.from_file('web/app.py'); at.run(); print('Dashboard UI Check: ' + str(len(at.exception)) + ' exceptions.')"

echo.
echo ===================================================
echo [4/4] Launching APRS V6 Pro Streamlit Dashboard...
echo URL: http://localhost:8501
echo ===================================================
.\.venv\Scripts\streamlit.exe run web\app.py
pause
