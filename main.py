"""
Battle System
Developed by: Aniket Chavan
Start Date: 11-05-20
"""

import os
# import tkinter
import random
import werkzeug
from threading import Thread
from signal import signal, SIGINT, SIGTERM

from classes import Monster, Move
from monsters import Chris, Thomas
from error import useError

VERSION = 0.1
# tkinter.Tcl().eval('info patchlevel')

chris = Chris()
thomas = Thomas()

class Battle(Thread):
    def __init__(self, blue: Monster, red: Monster):
        self.turn = 0
        Thread.__init__(self)
        self.blue = blue
        self.red = red
        self.log = []
        self.start()

    def endGame(self, msg):
        print(msg)
        self.blue.clear_stats()
        self.red.clear_stats()
        os._exit(0)
        del self

    def checkState(self):
        if self.blue.health <= 0:
            self.endGame(f"{self.red.name} beat {self.blue.name}, better luck next time!")
        elif self.red.health <= 0:
            self.endGame(f"Congratulations, {self.blue.name} beat {self.red.name}!")

    def logUpdate(self, text):
        while len(self.log) > 5:
            self.log.pop(0)
        self.log.append(text)

    def start(self):
        while True:
            os.system('clear')
            print('-------------------------------------------------')
            print(f"Opponent: {self.red.name} - {round(self.red.health)} HP")
            print("\n")
            print(f"You: {self.blue.name} - {round(self.blue.health)} HP")
            print()
            print("Battle Log:")
            print("===")
            for line in self.log:
                print(line)
            print("===")
            self.checkState()
            print("These are your moves - ")
            for count, move in enumerate(self.blue.moves):
                print(f"{count+1}. {move.name} {move.uses} Uses Left")
            while True:
                while True:
                    try:
                        curr_move = int(input("Enter move number: "))
                        if curr_move > len(self.blue.moves):
                            raise ValueError
                    except ValueError:
                        print("Please enter a valid number")
                    else:
                        break
                try:
                    self.logUpdate(self.blue.moves[curr_move-1].use(self.red))
                except useError:
                    print("You have exhausted all uses of this move")
                else:
                    break
            self.logUpdate(self.red.moves[random.randint(0, len(self.red.moves)-1)].use(self.blue))
            # os.system('clear')

def exitProgram(signal, frame):
    print("\nExiting Battle System")
    os._exit(0)

# window = Tk()
# window.title("Battle System ")

if __name__ == "__main__":
    signal(SIGINT, exitProgram)
    signal(SIGTERM, exitProgram)
    new = Battle(chris, thomas)
