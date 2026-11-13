@echo off
cd /d "%~dp0"
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
) else (
    set "PY=python"
)

echo Running LeetCode Daily Agent...
"%PY%" leetcode_agent.py
pause

