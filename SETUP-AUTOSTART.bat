@echo off
title Smart Vault Co. — Configure Auto-Start on Boot
echo.
echo ============================================
echo   SMART VAULT CO. — BOOT AUTO-START SETUP
echo ============================================
echo.
echo This will make all bots start automatically
echo every time Windows boots.
echo.

REM Configure PM2 to start on Windows boot via Task Scheduler
echo [1/2] Configuring PM2 Windows startup...
pm2 startup windows -u %USERNAME% 2>nul
pm2 save
echo       PM2 auto-start configured.
echo.

REM Create Windows Task Scheduler entry for WSL2 OpenClaw
echo [2/2] Creating Windows Task to start OpenClaw on boot...
schtasks /create /tn "SmartVaultOpenClaw" /tr "wsl -e bash -c 'openclaw start --config /mnt/f/Smart-Vault-Ai/openclaw.json --daemon'" /sc ONSTART /ru SYSTEM /f 2>nul
echo       Boot task created.
echo.

echo ============================================
echo   AUTO-START CONFIGURED
echo   Bots will start automatically on reboot.
echo   Run START-BOTS.bat to start them now.
echo ============================================
pause
