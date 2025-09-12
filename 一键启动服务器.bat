@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ==========================================
echo           Birthday Gift Web Server
echo ==========================================
echo.
echo Starting server...
echo.

REM Try using python command
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Using python to start server
    python server.py
    goto :end
)

REM Try using python3 command
python3 --version >nul 2>&1
if %errorlevel% == 0 (
    echo Using python3 to start server
    python3 server.py
    goto :end
)

REM If Python is not found
echo.
echo Python not found, please install Python first
echo.
echo Download: https://python.org
echo.
echo After installation, run this file again
echo.
pause
goto :end

:end
echo.
echo Server stopped
pause