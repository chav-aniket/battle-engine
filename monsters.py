"""
Monsters Module
Includes:
    - Monster Class
"""

from classes import Element, Monster
from moves import *

class Turtwig(Monster):
    def __init__(self):
        super().__init__(
            name="Turtwig", 
            element=Element.GRASS, 
            hlth=55, 
            atk=68, 
            dfn=64, 
            spd=31
            )
        self.learnMove(Tackle())
        self.learnMove(Absorb())

class Chimchar(Monster):
    def __init__(self):
        super().__init__(
            name="Chimchar", 
            element=Element.FIRE, 
            hlth=44, 
            atk=58, 
            dfn=44, 
            spd=61
            )
        self.learnMove(Leer())
        self.learnMove(Scratch())
        self.learnMove(Ember())
