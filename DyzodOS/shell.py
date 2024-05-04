#LOWERCASE
import os
import sys

import settings
import keyboard_driver
import graphics_driver
import hard_drive
import users
import inspect

def run(*args):
    if len(args) < 2:
        graphics_driver.WriteLn("Error: no filename")
        return
    
    file_name = args[1]
    file_path = os.path.join("user_hdd/" + file_name)
    
    if not os.path.isfile(file_path):
        graphics_driver.WriteLn(f"Error: File '{file_name}' not found.")
        return

    try:
        with open(file_path) as f:
            script_code = f.read()
            exec(script_code)
    except Exception as e:
        graphics_driver.WriteLn(f"Error executing {file_name}: {e}")

def help(*args):
    globals_dict = globals()
    function_names = [name for name, obj in globals_dict.items() if callable(obj) and inspect.isfunction(obj)]
    graphics_driver.WriteLn(f"{settings.HELP_PROMPT} {function_names}")

def cls(*args):
    graphics_driver.StdOut = []

def whoami(*args):
    graphics_driver.WriteLn(settings.CurrentUser.Name)
    
def view_drive_content(*args):
    content = hard_drive.GetHddContent()
    graphics_driver.WriteLn(content)

def rm_rf_no_preserve_root(*args):
    hard_drive.Create()
    graphics_driver.WriteLn("The Operation has completed successfully")

def createuser(*args):
    users.User(args[1], args[2])

def echo(*args):
    graphics_driver.WriteLn(args[1])

def shutdown(*args):
    settings.IsGraphicsRunning = False
    graphics_driver.pygame.quit()
    sys.exit()

def getusers(*args):
    UserNames = ""
    for User in users.users:
        UserNames = f"{UserNames + User.Name}:{User.pw}, "

    graphics_driver.WriteLn(UserNames)