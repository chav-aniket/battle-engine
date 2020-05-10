"""
Battle Engine V1.0
Developed by: Aniket Chavan
Start Date: 11-05-20
"""

import os
from threading import Thread

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
        return f"{self.owner.name} dealt {self.val} damage!"

class RegenMove(Move):
    '''
    Healing move class constructor
    '''
    def __init__(self, name, val):
        super().__init__(name, val)
    
    def use(self, opponent):
        self.owner.heal()
        print(f"{self.owner.name} healed for {self.val}!")

bitch_slap = AttackMove("Bitch Slap", 30)
poke = AttackMove("Poke", 10)
heal = RegenMove("Heal", 10)

class Monster:
    '''
    Monster class constructor
    '''
    def __init__(self, name):
        self.name = name
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

Chris = Monster("Chris")
Chris.learnMove(bitch_slap)
Chris.learnMove(poke)
Thomas = Monster("Thomas")
Thomas.learnMove(poke)

class Battle(Thread):
    def __init__(self, blue, red):
        Thread.__init__(self)
        self.turn = 0
        self.blue = blue
        self.red = red
        self.log = []
        self.start()

    def check_state(self):
        if self.blue.health <= 0:
            print('Better luck next time!')
            os._exit(0)
        elif self.red.health <= 0:
            print('Congratulations!')
            os._exit(0)

    def start(self):
        while True:
            print('-------------------------------------------------')
            print(f"Opponent: {self.red.name} - {self.red.health} HP")
            print("\n")
            print(f"You: {self.blue.name} - {self.blue.health} HP")
            print("\n")
            print("===")
            print("These are your moves - ")
            for count, move in enumerate(self.blue.moves):
                print(f"{count+1}. {move.name}")
            try:
                curr_move = int(input("Enter move number: "))
            except ValueError:
                print("Please enter a valid number")
                curr_move = int(input("Enter move number:"))
            self.log.append(self.blue.moves[curr_move - 1].use(self.red))
            # os.system('clear')
            for line in self.log:
                print(line)
            self.check_state()

if __name__ == "__main__":
    new = Battle(Chris, Thomas)
