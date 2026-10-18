@echo off
setlocal
where node >nul 2>nul
if not errorlevel 1 (
  node "%~dp0scripts\preview.cjs" %*
  goto done
)
set "STABLEMIND_NODE=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
if not exist "%STABLEMIND_NODE%" (
  echo Installez Node.js puis relancez ce fichier.
  pause
  exit /b 1
)
"%STABLEMIND_NODE%" "%~dp0scripts\preview.cjs" %*
:done
pause
