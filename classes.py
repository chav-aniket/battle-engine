"""
Classes Module
Includes
    - Monster Class
    - Move Class
"""
import os
import random

from error import useError


class Monster:
    '''
    Monster class constructor
    '''
    def __init__(self, name, hlth=500, atk=10, dfn=10, spd=50):
        self.name = name
        self.level = 1
        self.exp = 0
        self.health = hlth
        self.stats = [atk, dfn, spd]
        self.buffs = [0, 0, 0]
        self.moves = []
    
    @property
    def attack(self):
        return self.stats[0] + self.buffs[0]

    @property
    def defence(self):
        return self.stats[1] + self.buffs[1]
    
    @property
    def speed(self):
        return self.stats[2] + self.buffs[2]

    def take(self, val):
        self.health -= val
        if self.health < 0:
            self.health = 0

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
    
    def addOwner(self, owner: Monster):
        self.owner = owner
    
    def use(self, opponent: Monster):
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

    def use_attack(self, opponent: Monster):
        dmg = (self.owner.attack * self.damage) * (100/(100+opponent.defence))
        opponent.take(dmg)
        return dmg

    def use_regen(self):
        self.owner.heal(self.heal)
        return self.heal

class Battle():
    def __init__(self, blue: Monster, red: Monster):
        self.turn = 0
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

    def moveOrder(self):
        if self.blue.speed > self.red.speed:
            self.blue_move()
            self.red_move()
        else:
            self.red_move()
            self.blue_move()

    def blue_move(self):
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

    def red_move(self):
        while True:
            try:
                self.logUpdate(self.red.moves[random.randint(0, len(self.red.moves)-1)].use(self.blue))
            except useError:
                pass
            else:
                break

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
            self.moveOrder()
