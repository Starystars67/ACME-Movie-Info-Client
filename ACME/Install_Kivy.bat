@echo off

set /P loc=please enter your python location:

echo INFO: Installing latest pip and wheel.
%loc%\python.exe -m pip install --upgrade pip wheel setuptools
goto Dependencies

:Dependencies
echo INFO: Installing docutils pygments.
%loc%\python.exe -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
echo INFO: Installing kivy.deps.gstreamer
%loc%\python.exe -m pip install kivy.deps.gstreamer
goto Angle

:Angle
echo INFO: Installing angle backend.
%loc%\python.exe -m pip install kivy.deps.angle
goto Kivy

:Kivy
echo.
echo INFO: Installing Kivy.
%loc%\python.exe -m pip install kivy
REM goto Examples

set /P ex=Would you like to install the examples? (Y/N):
IF "%ex%"=="Y" OR IF "%ex%"=="y" (
  echo INFO: Installing Kivy examples.
  %loc%\python.exe -m pip install kivy_examples
)

echo Installation Complete.
pause
