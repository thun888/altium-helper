@echo off
:home
echo Welcome to the ALTIUM-HELPER HOME
echo Type 1 to make a package
echo Type 2 to calculate distance
set/p option=
if "%option%"=="1" python packager.py
if "%option%"=="2" python mouse.py
goto home