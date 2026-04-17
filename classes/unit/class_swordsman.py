from ursina import *

class Swordsman(Entity):
    def __init__(self):
        super().__init__(
            model='',
            speed=60,
            attack_speed=1.2,
            health=300,
            damage=40,
            price=50
            )