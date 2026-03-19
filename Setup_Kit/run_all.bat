@echo off
echo Initiating all setup scripts...
echo.

echo [1/2] Running setup.bat...
call git_setup.bat

echo.
echo [2/2] Running package_installer.bat...
call package_installer.bat

echo.
echo All scripts have been executed successfully!
pause
