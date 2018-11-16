@echo off
echo Installing all dependencies...
call npm i
goto PKG

:PKG
echo Installing Executable Compiler...
call npm i -g pkg

echo All Done. Please use Compile.bat to generate your Executable.
pause
