@echo off

if not exist ".env" (
    echo Error: .env file not found.
    exit /b 1
)

echo Reading .env file...
for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    set "%%A=%%B"
)

if "%GIT_USERNAME%"=="" (
    echo Warning: GIT_USERNAME is not set in .env.
) else (
    git config user.name "%GIT_USERNAME%"
    echo Successfully set git config user.name to "%GIT_USERNAME%"
)

if "%GIT_EMAIL%"=="" (
    echo Warning: GIT_EMAIL is not set in .env.
) else (
    git config user.email "%GIT_EMAIL%"
    echo Successfully set git config user.email to "%GIT_EMAIL%"
)
