# APRS V6 Pro - All-In-One Runner Script
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "[1/4] Seeding Verified E-Commerce Intelligence..." -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan
& .\.venv\Scripts\python.exe tools/seed_market_data.py

Write-Host "`n===================================================" -ForegroundColor Cyan
Write-Host "[2/4] Running Browser-Use Cloud & Budget Tests..." -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan
& .\.venv\Scripts\pytest.exe tests/test_browser_use_cloud.py -v

Write-Host "`n===================================================" -ForegroundColor Cyan
Write-Host "[3/4] Validating Streamlit 9-Tab Dashboard Headless..." -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan
& .\.venv\Scripts\python.exe -c "from streamlit.testing.v1 import AppTest; at = AppTest.from_file('web/app.py'); at.run(); Write-Host ('Dashboard UI Check: ' + str(len(at.exception)) + ' exceptions.')"

Write-Host "`n===================================================" -ForegroundColor Green
Write-Host "[4/4] Launching APRS V6 Pro Streamlit Dashboard..." -ForegroundColor Green
Write-Host "Local URL: http://localhost:8501" -ForegroundColor Yellow
Write-Host "===================================================" -ForegroundColor Green
& .\.venv\Scripts\streamlit.exe run web/app.py
