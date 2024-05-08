##SAMPLE LAYOUT OF A PLUGIN FILE##
import time
import sys
sys.path.append("../")

import API
import settings

import graphics_driver
from graphics_driver import onrenderframe, unbindfromframe, changerenderparams
import vectors
from vectors import Vector2D

API.ClearOutput()

API.WriteLine("Get Flashbanged")
time.sleep(1)
id = onrenderframe(graphics_driver.DrawRect, (Vector2D(0,0), settings.SCREEN_SIZE))
time.sleep(5)
changerenderparams(id, (vectors.getaverageVector(Vector2D(0,0), settings.SCREEN_SIZE), Vector2D(50, 50)))

time.sleep(3)

unbindfromframe(id)

API.WriteLine("Write a command for me to execute from your shell")
Inp = API.GetInput()
API.RunCommand(command=Inp, echo=True, caller="Sample Plugin")

##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##
##IF THE RENDERING INSTRUCTIONS ARE NOT UNBOUND##
##   THE PROGRAM WILL NOT EXIT ITS EXECUTION   ##
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##