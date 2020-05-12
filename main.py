"""
Battle System
Developed by: Aniket Chavan
Start Date: 11-05-20
"""

import os
# import tkinter
from signal import signal, SIGINT, SIGTERM

from classes import Battle
from monsters import *

VERSION = 0.1
# tkinter.Tcl().eval('info patchlevel')

def exitProgram(signal, frame):
    print("\nExiting Battle System")
    os._exit(0)

# window = Tk()
# window.title("Battle System ")

if __name__ == "__main__":
    signal(SIGINT, exitProgram)
    signal(SIGTERM, exitProgram)
    while True:
        try:
            print("Which Pokemon would you like to use?")
            print("Turtwig (1) or Chimchar (2)")
            user = int(input("Enter number: "))
            if user > 2:
                raise ValueError
        except ValueError:
            os.system('clear')
            print("Please input a valid number")
        else:
            break
    if user:
        Battle(Turtwig(), Chimchar())
    else:
        Battle(Chimchar(), Turtwig())
