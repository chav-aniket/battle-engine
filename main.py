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

VERSION = 0.1
# tkinter.Tcl().eval('info patchlevel')

class useError(Exception):
    '''
    Catches errors for if a move cannot be used anymore
    '''
    pass

class Move:
    '''
    Move class constructor

    Categories:
        - ATK / 0
        - REG / 1
        - ATKREG / 2
    '''
    ATK = 0
    REG = 1
    ATKREG = 2

    def __init__(self, name, element=None, cat=ATK, dmg=0, heal=0, uses=10):
        self.name = name
        self.category = cat
        self.element = element
        self.owner = None
        self.damage = dmg
        self.heal = heal
        self.max_uses = uses
        self.uses = uses
    
    def addOwner(self, owner):
        self.owner = owner
    
    def use(self, opponent):
        if self.uses == 0:
            raise useError
        self.uses -= 1
        if self.category == Move.ATK:
            dmg = self.use_attack(opponent)
            return f"{self.owner.name} used {self.name} and dealt {dmg} damage!"
        elif self.category == Move.REG:
            heal = val = self.use_regen()
            return f"{self.owner.name} used {self.name} to heal for {heal}!"
        elif self.category == Move.ATKREG: 
            dmg = self.use_attack(opponent)
            heal = self.use_regen()

    def use_attack(self, opponent):
        dmg = (self.owner.attack * self.damage) * (100/(100+opponent.defence))
        opponent.take(dmg)
        return dmg

    def use_regen(self):
        self.owner.heal(self.heal)
        return self.heal

class Monster:
    '''
    Monster class constructor
    '''
    def __init__(self, name, hlth=500, atk=10, dfn=10, spd=50):
        self.name = name
        self.level = 1
        self.exp = 0
        self.health = hlth
        self.attack = atk
        self.atk_buff = 0
        self.defence = dfn
        self.def_buff = 0
        self.speed = spd
        self.spd_buff = 0
        self.moves = []

    def take(self, val):

        self.health -= val

    def heal(self, val):
        self.health += val
    
    def clear_stats(self):
        self.atk_buff = 0
        self.def_buff = 0
        self.spd_buff = 0
        for move in self.moves:
            move.uses = move.max_uses

    def learnMove(self, move):
        self.moves.append(move)
        move.addOwner(self)

chris = Monster("Chris", atk=5, dfn=100)
chris.learnMove(Move("Bitch Slap", cat=Move.ATK, dmg=30))
chris.learnMove(Move("Poke", cat=Move.ATK, dmg=10))
chris.learnMove(Move("Photosynthesis", cat=Move.REG, heal=20))

thomas = Monster("Thomas", atk=5, dfn=100)
thomas.learnMove(Move("Bitch Slap", cat=Move.ATK, dmg=30))
thomas.learnMove(Move("Poke", cat=Move.ATK, dmg=10))
thomas.learnMove(Move("Photosynthesis", cat=Move.REG, heal=20))

class Battle(Thread):
    def __init__(self, blue, red):
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
