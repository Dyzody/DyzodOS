import sys
import keyboard
import time

import settings
import graphics_driver

InputBuffer = ""
CollectingInput = False

def log_keystroke(event):
    global CollectingInput
    global InputBuffer
    key_name = event.name

    if key_name == "enter":
        CollectingInput = False
    elif key_name == "backspace":
        InputBuffer = InputBuffer[:-1]
    elif key_name == "space":
        InputBuffer += " "
    elif key_name == "nach-oben":
        settings.StdOut_offset.y += -settings.Line_Spacing
        #print("up")
    elif key_name == "nach-unten":
        settings.StdOut_offset.y += settings.Line_Spacing
        #print("down")
    if len(key_name) > 1:
        return
    InputBuffer += key_name
    #print(InputBuffer)

def ExpectInp(Expect):
    Result = ""
    while not Result == Expect:
        Result = Keyboard_Input()

def Keyboard_Input():
    global CollectingInput
    global InputBuffer

    CollectingInput = True

    InputBuffer = ""

    while CollectingInput and settings.IsGraphicsRunning:
        graphics_driver.WriteBottomRow(InputBuffer)
        pass
        #print("Waiting on Input")
    graphics_driver.WriteLn(InputBuffer)
    return InputBuffer

def Init():
    keyboard.on_press(log_keystroke)
    while settings.IsGraphicsRunning:
        time.sleep(1)
    sys.exit()