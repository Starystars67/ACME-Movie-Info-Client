@echo off

cd C:\Users\Chris Ross\AppData\Local\Programs\Python\Python37-32

echo INFO: Installing latest pip and wheel.
python.exe -m pip install --upgrade pip wheel setuptools
goto Dependencies

:Dependencies
echo INFO: Installing docutils pygments.
python.exe -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
echo INFO: Installing kivy.deps.gstreamer
python.exe -m pip install kivy.deps.gstreamer
goto Angle

:Angle
echo INFO: Installing angle backend.
python.exe -m pip install kivy.deps.angle
goto Kivy

:Kivy
echo.
echo INFO: Installing Kivy.
python.exe -m pip install kivy
goto Examples

:Examples
echo INFO: Installing Kivy examples.
python.exe -m pip install kivy_examples