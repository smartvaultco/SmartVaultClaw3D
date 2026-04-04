@echo off
echo Smart Vault Co. — Course Scraper
echo ================================
echo.

REM Check Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Install from python.org
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Installing dependencies...
pip install -r requirements.txt >nul 2>&1
playwright install chromium >nul 2>&1
echo Dependencies ready.
echo.

REM Menu
echo Which course do you want to scrape?
echo [1] Tony The Closer (ronaproof.com / Kajabi)
echo [2] Sean Terry (flip2freedom.com)
echo [3] Both
echo.
set /p choice="Enter 1, 2, or 3: "

if "%choice%"=="1" (
    echo.
    echo Starting Tony The Closer scraper...
    python scraper.py --platform kajabi
)
if "%choice%"=="2" (
    echo.
    echo Starting Sean Terry scraper...
    python scraper.py --platform flip2freedom
)
if "%choice%"=="3" (
    echo.
    echo Starting Tony The Closer scraper...
    python scraper.py --platform kajabi
    echo.
    echo Starting Sean Terry scraper...
    python scraper.py --platform flip2freedom
)

echo.
echo Done! Check f:\Smart-Vault-Ai\KB\realestate\ for your KB files.
pause
