"""
Monsters Module
Includes:
    - Monster Class
"""

from classes import Monster
from moves import *

class Thomas(Monster):
    def __init__(self):
        super().__init__(
            name="Thomas", 
            hlth=500, 
            atk=10, 
            dfn=50, 
            spd=50
            )
        self.learnMove(BitchSlap())
        self.learnMove(Poke())
        self.learnMove(Heal())

class Chris(Monster):
    def __init__(self):
        super().__init__(
            name="Chris", 
            hlth=1000, 
            atk=20, 
            dfn=60, 
            spd=10
            )
        self.learnMove(BitchSlap())
        self.learnMove(Poke())
        self.learnMove(Heal())
