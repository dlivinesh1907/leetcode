@echo off
cd /d "%~dp0"
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
) else (
    set "PY=python"
)

echo Starting Fast Batch Solver to 400 problems...
"%PY%" batch_solver.py 400
pause

