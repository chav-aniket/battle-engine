"""
Moves Module

Includes:
    - Move Class
    - Use Error Class
"""

from classes import Element, Monster, Move

class Leer(Move):
    def __init__(self):
        super().__init__(
            name="Leer",  
            cat=Move.STAT, 
            uses=30
            )
    
    def use(self, opponent: Monster):
        opponent.buff(1, -1)
        self.uses -= 1
        return f"{self.owner.name} used {self.name}, it lowered {opponent.name}'s defence!"

class Scratch(Move):
    def __init__(self):
        super().__init__(
            name="Scratch", 
            cat=Move.PHYS, 
            dmg=40,  
            uses=35
            )
    
    def use(self, opponent: Monster):
        dmg = self.damageCalc(opponent)
        opponent.take(dmg)
        self.uses -= 1
        return f"{self.owner.name} used {self.name} and dealt {dmg} damage!"

class Tackle(Move):
    def __init__(self):
        super().__init__(
            name="Tackle", 
            cat=Move.PHYS, 
            dmg=40,  
            uses=35
            )
    def use(self, opponent: Monster):
        dmg = self.damageCalc(opponent)
        opponent.take(dmg)
        self.uses -= 1
        return f"{self.owner.name} used {self.name} and dealt {dmg} damage!"

class Absorb(Move):
    def __init__(self):
        super().__init__(
            name="Absorb", 
            element=Element.GRASS, 
            cat=Move.PHYS, 
            dmg=25, 
            uses=25
            )

    def use(self, opponent: Monster):
        dmg = self.damageCalc(opponent)
        opponent.take(dmg)
        reg = self.owner.heal(dmg*0.65)
        self.uses -= 1
        return f"{self.owner.name} used {self.name} and dealt {dmg} damage!\n{self.owner.name} got healed!"

class Ember(Move):
    def __init__(self):
        super().__init__(
            name="Ember", 
            element=Element.FIRE, 
            cat=Move.SPEC, 
            dmg=40,  
            uses=25
            )
    def use(self, opponent: Monster):
        dmg = self.damageCalc(opponent)
        opponent.take(dmg)
        self.uses -= 1
        return f"{self.owner.name} used {self.name} and dealt {dmg} damage!"
