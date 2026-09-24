@echo off
title IA LIVRE - servidor local
cd /d "%~dp0"
where py >nul 2>&1
if %errorlevel%==0 (
  py ia-livre-local.py
  goto :fim
)
where python >nul 2>&1
if %errorlevel%==0 (
  python ia-livre-local.py
  goto :fim
)
echo.
echo Python nao foi encontrado neste computador.
echo.
echo Instale Python 3 e execute este arquivo novamente.
pause
:fim
