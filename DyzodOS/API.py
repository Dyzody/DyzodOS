import graphics_driver
import keyboard_driver

#Writes a simple line of Text to StdOut
def WriteLine(Text):
    graphics_driver.WriteLn(Text)

#Get a written line by the User
#Returns what the user sends via ENTER
def GetInput():
    return keyboard_driver.Keyboard_Input()