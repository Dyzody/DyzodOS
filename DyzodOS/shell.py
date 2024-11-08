#LOWERCASE
import os
import sys
import shutil

import settings
import keyboard_driver
import data_tools
import graphics_driver
import hard_drive
import users
import inspect

def ls(*args):
    directory = settings.get_dir()
    graphics_driver.WriteLn(f"Contents of directory {directory}:")
    dir_list = os.listdir(directory)
    
    for obj in dir_list:
        graphics_driver.WriteLn(obj)

def cd(*args):
    pathlocation = args[1]
    
    if pathlocation == "..":
        if settings.current_path != settings.DEFAULT_PATH:
            parent_dir = '/'.join(settings.current_path.split('/')[:-1])
            settings.current_path = (parent_dir if parent_dir else "")
    else:
        new_path = f"{pathlocation}"
        # Check if the new path exists
        if os.path.exists(f"{settings.get_dir()}{new_path}"):
            
            if len(settings.current_path) > 0:
                settings.current_path += "/"

            settings.current_path += f"{new_path}"
        else:
            graphics_driver.WriteLn("Directory not found.")

def run(*args):
    if len(args) < 2:
        graphics_driver.WriteLn("Error: no filename")
        return

    file_name = args[1]
    file_path = os.path.join(f"{settings.get_dir()}{file_name}")
    
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

def clear(*args):
    graphics_driver.StdOut = []

def whoami(*args):
    graphics_driver.WriteLn(settings.CurrentUser.Name)
    
def view_drive_content(*args):
    content = hard_drive.GetHddContent()
    graphics_driver.WriteLn(content)

def rm(*args):
    
    name = ""
    remove_folder = False

    #Protect the user from themself
    if args[1] == "-r":
        name = args[2]
        remove_folder = True
    else:
        name = args[1]
    
    pathname = settings.get_dir() + name
    success = False

    if os.path.exists(pathname):
        if os.path.isfile(pathname) and not remove_folder:
            os.remove(pathname)
            success = True
            graphics_driver.WriteLn(f"File '{pathname}' removed successfully.")
        elif os.path.isdir(pathname) and remove_folder:
            shutil.rmtree(pathname)
            graphics_driver.WriteLn(f"Directory '{pathname}' removed successfully.")
            success = True
    else:
        graphics_driver.WriteLn(f"'{pathname}' does not exist.")

    if not success:
        graphics_driver.WriteLn("rm: Syntax error: rm -rf for folders, rm for files.")


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