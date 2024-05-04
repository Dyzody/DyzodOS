import time

import keyboard_driver
import graphics_driver
import hard_drive

import settings

users = []
usernames = []

if not hard_drive.GetClusterByName("Users"):
    hard_drive.AddCluster("Users", "")

class User:
    def __init__(self, Name, pw, write_to_disk=True):
        self.Name = Name
        self.pw = pw
        users.append(self)
        usernames.append(self.Name)
        if write_to_disk:
            hard_drive.WriteToCluster("Users", f"{Name}:{pw},")

def OnBoot():
    if not settings.Hard_Drive:
        return
    ClusterContent = hard_drive.GetClusterByName("Users")
    if len(ClusterContent) <= 0:
        return
    ClusterArray = ClusterContent.split(",")
    if len(ClusterArray) <= 0:
        return
    for CUser in ClusterArray:
        CUserData = CUser.split(":")
        if len(CUserData) != 2:
            continue
        CUserName = CUserData[0]
        CUserPassword = CUserData[1]
        User(CUserName, CUserPassword, write_to_disk=False)

def Login(Name, PW):
    #graphics_driver.WriteLn(f"{len(users)} Benutzer")
    retval = False
    for CUser in users:
        if CUser.Name == Name and CUser.pw == PW:
            settings.CurrentUser = CUser
            graphics_driver.WriteLn("Anmeldung erfolgreich")
            retval = True
    return retval

import time

def UserSetup(AllowCancel=True):
    while True:
        time.sleep(0.3)
        graphics_driver.WriteLn("LOGIN or SIGNUP ?")

        if AllowCancel:
            graphics_driver.WriteLn("Schreiben Sie CANCEL um abzubrechen")

        inp = keyboard_driver.Keyboard_Input()
        inp = inp.upper()

        if AllowCancel and inp == "CANCEL":
            return

        if inp not in ["LOGIN", "SIGNUP"]: 
            graphics_driver.WriteLn("Invalid Input. LOGIN or SIGNUP ?")
            continue

        if inp == "LOGIN" and len(users) <= 0:
            graphics_driver.WriteLn("Keine Benutzer vorhanden, SIGNUP wird durchgeführt")
            inp = "SIGNUP"

        if inp == "LOGIN":
            graphics_driver.WriteLn("Nutzername eingeben")
            user = keyboard_driver.Keyboard_Input()
            graphics_driver.WriteLn("Passwort eingeben")
            pw = keyboard_driver.Keyboard_Input()
            Success = Login(user, pw)

            graphics_driver.WriteLn(f"Success: {str(Success)}")

            if Success: 
                graphics_driver.WriteLn("Returning Function")
                return
            else:
                graphics_driver.WriteLn("Anmeldung fehlgeschlagen")
                continue

        else:
            graphics_driver.WriteLn("Nutzername eingeben")
            NewUser = keyboard_driver.Keyboard_Input()
            if NewUser in usernames:
                graphics_driver.WriteLn("User already exists")
                continue
            graphics_driver.WriteLn("Passwort eingeben")
            Password = keyboard_driver.Keyboard_Input()
            graphics_driver.WriteLn(f"Hallo {NewUser} dein Passwort ist {Password}. Ist das korrekt? JA / NEIN")
            CONFIRM = keyboard_driver.Keyboard_Input()
            CONFIRM = CONFIRM.upper()
            if CONFIRM == "NEIN":
                graphics_driver.WriteLn("Neustart des Programms")
                continue
            User(NewUser, Password)
            graphics_driver.WriteLn("Nutzer erfolgreich erstellt. Bitte melde dich nun an.")
            time.sleep(0.1)
