"""
Moves Module

Includes:
    - Move Class
    - Use Error Class
"""

from classes import Element, Move

class Leer(Move):
    def __init__(self):
        super().__init__(
            name="Leer",  
            cat=Move.STAT, 
            uses=30
            )

class Scratch(Move):
    def __init__(self):
        super().__init__(
            name="Scratch", 
            cat=Move.PHYS, 
            dmg=40,  
            uses=35
            )

class Tackle(Move):
    def __init__(self):
        super().__init__(
            name="Tackle", 
            cat=Move.PHYS, 
            dmg=40,  
            uses=35
            )

class Absorb(Move):
    def __init__(self):
        super().__init__(
            name="Absorb", 
            element=Element.GRASS, 
            cat=Move.PHYS, 
            dmg=25, 
            heal=0.65*25, 
            uses=25
            )

class Ember(Move):
    def __init__(self):
        super().__init__(
            name="Ember", 
            element=Element.FIRE, 
            cat=Move.SPEC, 
            dmg=40,  
            uses=25
            )