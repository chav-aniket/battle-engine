"""
Battle System
Developed by: Aniket Chavan
Start Date: 11-05-20
"""

import os
# import tkinter
import random
from threading import Thread
from signal import signal, SIGINT, SIGTERM

VERSION = 0.1

# tkinter.Tcl().eval('info patchlevel')

class Move:
    '''
    Move class constructor
    '''
    def __init__(self, name, val):
        self.name = name
        self.owner = None
        self.damage = 10
        self.uses = 10
    
    def addOwner(self, owner):
        self.owner = owner

class AttackMove(Move):
    '''
    Attack move class constructor
    '''
    def __init__(self, name, val):
        super().__init__(name, val)
        self.name = name
        self.val = val

    def use(self, opponent):
        opponent.take(self.val)
        return f"{self.owner.name} used {self.name} and dealt {self.val} damage!"

class RegenMove(Move):
    '''
    Healing move class constructor
    '''
    def __init__(self, name, val):
        super().__init__(name, val)
        self.name = name
        self.val = val
    
    def use(self, opponent):
        self.owner.heal(self.val)
        return f"{self.owner.name} used {self.name} to heal for {self.val}!"


class Monster:
    '''
    Monster class constructor
    '''
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.health = 100
        self.attack = 100
        self.defence = 100
        self.moves = []

    def take(self, val):
        self.health -= val

    def heal(self, val):
        self.health += val

    def learnMove(self, move):
        self.moves.append(move)
        move.addOwner(self)

chris = Monster("Chris")
chris.learnMove(AttackMove("Bitch Slap", 30))
chris.learnMove(AttackMove("Poke", 10))
chris.learnMove(RegenMove("Heal", 10))

thomas = Monster("Thomas")
thomas.learnMove(AttackMove("Poke", 10))
thomas.learnMove(RegenMove("Heal", 10))
thomas.learnMove(AttackMove("Bitch Slap", 30))

class Battle(Thread):
    def __init__(self, blue, red):
        self.turn = 0
        Thread.__init__(self)
        self.blue = blue
        self.red = red
        self.log = []
        self.start()

    def check_state(self):
        if self.blue.health <= 0:
            print(f"{self.red.name} beat {self.blue.name}, better luck next time!")
            os._exit(0)
            del self
        elif self.red.health <= 0:
            print(f"Congratulations, {self.blue.name} beat {self.red.name}!")
            os._exit(0)
            del self
    
    def logUpdate(self, text):
        while len(self.log) > 5:
            self.log.pop(0)
        self.log.append(text)

    def start(self):
        while True:
            os.system('clear')
            print('-------------------------------------------------')
            print(f"Opponent: {self.red.name} - {self.red.health} HP")
            print("\n")
            print(f"You: {self.blue.name} - {self.blue.health} HP")
            print("\n")
            print("===")
            for line in self.log:
                print(line)
            print("===")
            print("These are your moves - ")
            for count, move in enumerate(self.blue.moves):
                print(f"{count+1}. {move.name}")
            while True:
                try:
                    curr_move = int(input("Enter move number: "))
                    if curr_move > len(self.blue.moves):
                        raise ValueError
                except ValueError:
                    print("Please enter a valid number")
                else:
                    break
            self.logUpdate(self.blue.moves[curr_move-1].use(self.red))
            self.logUpdate(self.red.moves[random.randint(0, len(self.red.moves)-1)].use(self.blue))
            # os.system('clear')
            self.check_state()

def exitProgram(signal, frame):
    print("\nExiting Battle System")
    os._exit(0)

# window = Tk()
# window.title("Battle System ")

if __name__ == "__main__":
    signal(SIGINT, exitProgram)
    signal(SIGTERM, exitProgram)
    new = Battle(chris, thomas)
