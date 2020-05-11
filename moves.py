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
            cat=Move.ATK, 
            dmg=10,  
            uses=10
            )

class BitchSlap(Move):
    def __init__(self):
        super().__init__(
            name="Bitch Slap", 
            element=None, 
            cat=Move.ATK, 
            dmg=30,  
            uses=5
            )

class Heal(Move):
    def __init__(self):
        super().__init__(
            name="Heal", 
            element=None, 
            cat=Move.REG, 
            heal=20,  
            uses=10
            )