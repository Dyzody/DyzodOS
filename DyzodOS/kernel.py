import os
import threading
import numpy
import time

import settings
import vectors

import keyboard_driver
import graphics_driver
import hard_drive
import users
import shell

Graphics_Thread = None

def WriteLnToGraphicsThread(Text):
    graphics_driver.WriteLn(Text)

def FlushStdOut():
    graphics_driver.StdOut = []

def OnInput(Inp):
    graphics_driver.WriteLn(Inp)

def WaitForMedia():
    if settings.Hard_Drive: return settings.Hard_Drive
    
    graphics_driver.WriteLn("No Hard Drive")
    graphics_driver.WriteLn("Write CREATE in Plain Text to create a Hard Drive")

    keyboard_driver.ExpectInp("CREATE")
    graphics_driver.WriteLn("Creating Hard Drive...")

    hard_drive.Create()

def Command(command):
    
    args = command.split()

    if args:
        cmd = args[0]
        cmd = cmd.lower()
        try:
            app = getattr(shell, cmd)
            app(*args)
        except Exception as error:
            graphics_driver.WriteLn(f"Error occurred: {error}")
            return error
        
def ListenForCommands():
    while settings.IsGraphicsRunning:
        command = keyboard_driver.Keyboard_Input()
        Command(command)

def Bootloader():
    time.sleep(1)

    graphics_driver.WriteLn("Sanity check")
    graphics_driver.WriteLn(f"{os.cpu_count()} Threads OK")
    graphics_driver.WriteLn("Graphics OK")
    graphics_driver.WriteLn("Keyboard OK")
    graphics_driver.WriteLn(f"MEM OK 1024KB")
    graphics_driver.WriteLn("ENTER TO CONTINUE")
    time.sleep(1)
    settings.IsGraphicsRunning = True
    FlushStdOut()

def InitKernel():
    #Graphics Thread

    print("Starting Main Graphics Thread")
    Graphics_Thread = threading.Thread(target=graphics_driver.InitGraphics, args=[settings.Fullscreen])
    Graphics_Thread.start()

    #Keyboard Thread
    print("Starting Main Keyboard Thread")
    Keyboard_Driver_Thread = threading.Thread(target=keyboard_driver.Init)
    Keyboard_Driver_Thread.start()
    
    graphics_driver.WriteLn("System Daemon started")

    Bootloader()
    WaitForMedia()
    users.OnBoot()
    users.UserSetup(AllowCancel=False)
    print("Starting Main Shell Thread")
    Shell_Thread = threading.Thread(target=ListenForCommands)
    Shell_Thread.start()
    graphics_driver.WriteLn("Setup Complete")
    graphics_driver.WriteLn("TYPE HELP FOR HELP")


if __name__ == '__main__':
    InitKernel()