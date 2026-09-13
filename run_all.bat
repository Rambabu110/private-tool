@echo off
title APRS V6 Pro - All-In-One Runner
echo ===================================================
echo [1/4] Seeding Verified E-Commerce Intelligence Data...
echo ===================================================
.\.venv\Scripts\python.exe tools\seed_market_data.py
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Data seeding failed.
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
