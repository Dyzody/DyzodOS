import sys
import time
import pygame

import settings
CollectingInput = False

def log_otherinp(event):
    key_name = event.key
    
    # Process special keys
    if key_name == pygame.K_ESCAPE:  # Escape key
        settings.reset()
    elif key_name == pygame.K_BACKSPACE:  # Backspace key
        settings.InputBuffer = settings.InputBuffer[:-1]
    elif key_name == pygame.K_SPACE:  # Space key
        settings.InputBuffer += " "
    elif key_name == pygame.K_UP:  # Up arrow key
        settings.StdOut_offset.y -= settings.Line_Spacing
    elif key_name == pygame.K_DOWN:  # Down arrow key
        settings.StdOut_offset.y += settings.Line_Spacing
    elif key_name == pygame.K_RETURN:
        settings.CollectingInput = False
        

# Function to process the keystrokes (event handling)
def log_keystroke_text(event):
    
    print(event)
    
    key_name = event.text

    print(key_name)

    # Add the character to the buffer (ignore non-character keys like shift, etc.)
    if len(key_name) == 1 and settings.CollectingInput:
        print(settings.InputBuffer)
        settings.InputBuffer += key_name
        return True

# Function to handle waiting for input and capturing it
def ExpectInp(Expect):
    Result = ""
    while not Result == Expect:
        Result = Keyboard_Input()

# Function to capture input directly from the window (using pygame)
def Keyboard_Input():
    settings.CollectingInput = True
    settings.InputBuffer = ""

    while settings.CollectingInput and settings.IsGraphicsRunning:
        time.sleep(0.001)
    
    buffer = settings.InputBuffer
    settings.InputBuffer = ""
    return buffer