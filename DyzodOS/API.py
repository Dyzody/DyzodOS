import kernel
import settings
import graphics_driver
import keyboard_driver
from vectors import Vector2D

#Writes a simple line of Text to StdOut
def WriteLine(Text:str) -> None:
    graphics_driver.WriteLn(Text)

#Get a written line by the User
#Returns what the user sends via ENTER
def GetInput() -> str:
    return keyboard_driver.Keyboard_Input()

#Runs a shell command
def RunCommand(command:str, echo=False, caller="Application") -> str:
    if echo:
        WriteLine(f"{caller} executing command: {command} EOF")
    result = kernel.Command(command)
    return result