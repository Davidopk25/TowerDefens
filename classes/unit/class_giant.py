from ursina import *

class Giant(Entity):
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model='cube',
            position=position,
            scale=(18, 25, 18),
            **kwargs
        )
        self.speed = 30
        self.attack_speed = 2.0
        self.health = 900
        self.damage = 65
        self.price = 150