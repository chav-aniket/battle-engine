"""
Classes Module
Includes
    - Monster Class
    - Move Class
"""

from error import useError

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

    def learnMove(self, move: Move):
        self.moves.append(move)
        move.addOwner(self)
