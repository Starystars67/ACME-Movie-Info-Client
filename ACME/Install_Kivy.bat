@echo off

echo INFO: Installing latest pip and wheel.
C:\Python27amd64\python.exe -m pip install --upgrade pip wheel setuptools
goto Dependencies

:Dependencies
echo INFO: Installing docutils pygments.
C:\Python27amd64\python.exe -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
echo INFO: Installing kivy.deps.gstreamer
C:\Python27amd64\python.exe -m pip install kivy.deps.gstreamer
goto Angle

:Angle
echo INFO: Installing angle backend.
C:\Python27amd64\python.exe -m pip install kivy.deps.angle
goto Kivy

:Kivy
echo.
echo INFO: Installing Kivy.
C:\Python27amd64\python.exe -m pip install kivy
goto Examples

:Examples
echo INFO: Installing Kivy examples.
C:\Python27amd64\python.exe -m pip install kivy_examples