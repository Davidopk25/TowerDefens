from ursina import *

class Archer(Entity):
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model='cube',
            color=color.green,
            scale=(8, 14, 8),
            position=position,
            **kwargs
        )
        self.speed = 70
        self.attack_speed = 0.8
        self.health = 150
        self.damage = 35
        self.price = 60