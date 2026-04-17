from ursina import *

class Archer(Entity):
    def __init__(self):
        super().__init__(
            model='',
            speed=70,
            attack_speed=0.8,
            health=150,
            damage=35,
            price=60
            )