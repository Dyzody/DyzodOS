##SAMPLE LAYOUT OF A PLUGIN FILE##
import time
import sys
sys.path.append("../")

import API
import graphics_driver
from graphics_driver import onrenderframe, unbindfromframe
from vectors import Vector2D

API.WriteLine("Hello!")
id = onrenderframe(graphics_driver.DrawRect, (Vector2D(30, 30), Vector2D(30, 30)))
time.sleep(5)
unbindfromframe(index=id)

API.WriteLine("Write a command for me to execute from your shell")
Inp = API.GetInput()
API.RunCommand(command=Inp, echo=True, caller="Sample Plugin")