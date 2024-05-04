::Installs any dependecies and runs the Program
cd /d %~dp0

py -m pip install pygame
py -m pip install cryptography
py -m pip install numpy
py -m pip install keyboard
py kernel.py