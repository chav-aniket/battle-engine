"""
Classes Module
Includes
    - Monster Class
    - Move Class
"""
import os
import random

from error import useError


class Element:
    '''
    Element class
    '''
    NONE        = -1
    BASIC       = 0
    FIRE        = 1
    WATER       = 2
    GRASS       = 3
    ELECTRIC    = 4
    WIND        = 5
    EARTH       = 6
    ROCK        = 7
    ICE         = 8
    POISON      = 9
    METAL       = 10
    FIGHTING    = 11
    MYSTIC      = 12
    LIGHT       = 13
    DARK        = 14

    MATCHUPS = [
        [1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 0.5, 1, 1, 1, 1],  # BASIC
        [1, 0.5, 0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # FIRE
        [1, 2, 0.5, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # WATER
        [1, 0.5, 2, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # GRASS
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # ELECTRIC
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # WIND
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # EARTH
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # ROCK
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # ICE
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # POISON
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # METAL
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # FIGHTING
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # MYSTIC
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # LIGHT
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]       # DARK
    ]

    @classmethod
    def multiplier(cls, type1, type2):
        return cls.MATCHUPS[type1][type2]

class Monster:
    '''
    Monster class constructor
    '''
    def __init__(self, name, element=Element.BASIC, hlth=500, atk=10, dfn=10, spd=50):
        self.name = name
        self.level = 1
        self.exp = 0
        self.element = element
        self.max_health = hlth
        self.health = hlth
        self.stats = [atk, dfn, spd]
        self.buffs = [0, 0, 0]
        self.moves = []
        self.status = Status.NONE

    def buff(self, stat, numStages):
        self.buffs[stat] += numStages

    @property
    def attack(self):
        if self.buffs[0] > 0:
            return self.stats[0] * ((2+self.buffs[0])/2)
        else:
            return self.stats[0] * (2/(-2+self.buffs[0]))

    @property
    def defence(self):
        if self.buffs[2] > 0:
            return self.stats[1] * ((2+self.buffs[0])/2)
        else:
            return self.stats[1] * (2/(-2+self.buffs[0]))

    @property
    def speed(self):
        if self.buffs[2] > 0:
            return self.stats[2] * ((2+self.buffs[0])/2)
        else:
            return self.stats[2] * (2/(-2+self.buffs[0]))

    def take(self, val):
        self.health -= val
        if self.health < 0:
            self.health = 0

    def heal(self, val):
        self.health += val
        if self.health > self.max_health:
            self.health = self.max_health
    
    def clear_stats(self):
        self.buffs = [0, 0, 0]
        for move in self.moves:
            move.uses = move.max_uses

    def learnMove(self, move):
        self.moves.append(move)
        move.addOwner(self)

class Status:
    NONE    = 0
    STUN    = 1
    BURN    = 2
    SLEEP   = 3
    STATIC  = 4
    POISON  = 5
    COUNTER = 6

    @classmethod
    def status(cls, monster: Monster, status):
        if status == cls.NONE:
            pass
        elif status == cls.STUN:
            pass

class Move:
    '''
    Move class constructor
    '''
    PHYS = 0
    SPEC = 1
    STAT = 2

    def __init__(self, name, element=Element.BASIC, cat=PHYS, dmg=0, heal=0, accuracy=100, priority=False, uses=10):
        self.name = name
        self.owner = None
        self.category = cat
        self.element = element
        self.damage = dmg
        self.heal = heal
        self.accuracy = accuracy
        self.priority = priority
        self.max_uses = uses
        self.uses = uses

    def addOwner(self, owner: Monster):
        self.owner = owner

    def useCheck(self):
        if self.uses == 0:
            print("This move has no uses left!")
            raise useError

    def damageCalc(self, opponent: Monster):
        mul = Element.multiplier(self.element, opponent.element)
        dmg = round((7 + (self.owner.level/200) * self.damage * (self.owner.attack/opponent.defence)) * mul)
        return dmg

class Battle():
    def __init__(self, blue: Monster, red: Monster):
        self.turn = 0
        self.blue = blue
        self.red = red
        self.log = []
        # while True:
        #     self.
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

    def blueMove(self):
        print("These are your moves - ")
        for count, move in enumerate(self.blue.moves):
            print(f"{count+1}. {move.name} {move.uses} Uses Left")

        while True:
            try:
                curr_move = int(input("Enter move number: "))
                if curr_move > len(self.blue.moves):
                    raise ValueError
            except ValueError:
                print("Please enter a valid number")
            else:
                move = self.blue.moves[curr_move-1]
                try:
                    move.useCheck()
                except useError:
                    pass
                else:
                    return move

    def redMove(self):
        while True:
            try:
                move = self.red.moves[random.randint(0, len(self.red.moves)-1)]
            except useError:
                pass
            else:
                return move

    def blueFirst(self, blue_move: Move, red_move: Move):
        blue_move.use(self.red)
        self.checkState()
        red_move.use(self.blue)
        self.checkState()

    def redFirst(self, blue_move: Move, red_move: Move):
        red_move.use(self.blue)
        self.checkState()
        blue_move.use(self.red)
        self.checkState()

    def display(self):
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

    def decide(self):
        blue_move = self.blueMove()
        red_move = self.redMove()
        if blue_move.priority and not red_move.priority:
            self.blueFirst(blue_move, red_move)
        elif red_move.priority and not blue_move.priority:
            self.redFirst(blue_move, red_move)
        else:
            if self.blue.speed > self.red.speed:
                self.blueFirst(blue_move, red_move)
            else:
                self.redFirst(blue_move, red_move)
