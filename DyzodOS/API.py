import graphics_driver
import keyboard_driver

def WriteLine(Text):
    graphics_driver.WriteLn(Text)

def GetInput():
    return keyboard_driver.Keyboard_Input()