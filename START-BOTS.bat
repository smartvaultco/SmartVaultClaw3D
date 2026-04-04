@echo off
title Smart Vault Co. — Start All Bots
echo.
echo ============================================
echo   SMART VAULT CO. — BOT STARTUP
echo ============================================
echo.

REM Step 1: Start OpenClaw Gateway in WSL2
echo [1/3] Starting OpenClaw Gateway in WSL2...
wsl -e bash -c "cd /mnt/f/Smart-Vault-Ai && openclaw start --config openclaw.json --daemon 2>&1 &"
timeout /t 3 /nobreak >nul
echo       Gateway starting on port 18789...
echo.

REM Step 2: Start PM2 (scheduler + monitor)
echo [2/3] Starting PM2 scheduler...
cd /d f:\Smart-Vault-Ai
pm2 start ecosystem.config.js --env production 2>nul
pm2 save
echo       PM2 running.
echo.

REM Step 3: Start Claw3D (3D office UI)
echo [3/3] Starting Claw3D office UI...
start "Claw3D" cmd /k "cd /d f:\Smart-Vault-Ai\claw3d-temp && npm run dev"
echo       Claw3D starting at http://localhost:3000/office
echo.

echo ============================================
echo   ALL SYSTEMS ONLINE
echo   Telegram bots are live and listening.
echo   Open http://localhost:3000/office to watch
echo   your agents work in real-time.
echo ============================================
echo.
pause
