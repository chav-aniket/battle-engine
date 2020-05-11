"""
Battle System
Developed by: Aniket Chavan
Start Date: 11-05-20
"""

import os
# import tkinter
from signal import signal, SIGINT, SIGTERM

from classes import Battle, Monster, Move
from monsters import Chris, Thomas
from error import useError

VERSION = 0.1
# tkinter.Tcl().eval('info patchlevel')

chris = Chris()
thomas = Thomas()

def exitProgram(signal, frame):
    print("\nExiting Battle System")
    os._exit(0)

# window = Tk()
# window.title("Battle System ")

if __name__ == "__main__":
    signal(SIGINT, exitProgram)
    signal(SIGTERM, exitProgram)
    Battle(chris, thomas)
