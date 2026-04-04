@echo off
echo Smart Vault Co. — Course Scraper Setup
echo ======================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed.
    echo Download from: https://python.org/downloads
    echo Make sure to check "Add Python to PATH" during install.
    pause
    exit /b 1
)

echo Python found. Installing packages...
pip install playwright anthropic python-dotenv requests
echo.
echo Installing Chromium browser...
playwright install chromium
echo.
echo Setup complete!
echo.
echo NEXT STEP: Add your course credentials to .env file:
echo.
echo   TONY_CLOSER_EMAIL=your@email.com
echo   TONY_CLOSER_PASSWORD=yourpassword
echo   SEAN_TERRY_EMAIL=your@email.com
echo   SEAN_TERRY_PASSWORD=yourpassword
echo.
echo Then run: run.bat
echo.
pause
