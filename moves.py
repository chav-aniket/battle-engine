"""
Moves Module

Includes:
    - Move Class
    - Use Error Class
"""

from classes import Move

class Poke(Move):
    def __init__(self):
        super().__init__(
            name="Poke", 
            element=None, 
            cat=Move.PHYS, 
            dmg=10, 
            uses=25
            )

class BitchSlap(Move):
    def __init__(self):
        super().__init__(
            name="Bitch Slap", 
            element=None, 
            cat=Move.PHYS, 
            dmg=30,  
            uses=20
            )

class Heal(Move):
    def __init__(self):
        super().__init__(
            name="Heal", 
            element=None, 
            cat=Move.STAT, 
            heal=20,  
            uses=20
            )