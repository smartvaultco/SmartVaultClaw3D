@echo off
title Smart Vault Co. — Stop All Bots
echo.
echo Stopping all Smart Vault bots...

wsl -e bash -c "openclaw stop 2>/dev/null || true"
pm2 stop all 2>nul
pm2 save

echo Done. All bots stopped.
pause
