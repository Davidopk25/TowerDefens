from ursina import *

class Knight(Entity):
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model='cube',
            color=color.red,
            scale=(10, 15, 10),
            position=position,
            **kwargs
        )
        self.speed = 60
        self.attack_speed = 1.2
        self.health = 300
        self.damage = 40
        self.price = 50