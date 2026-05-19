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
        self.health = 900
        self.damage = 65
        self.price = 150
        self.enemy_tower = None

    def update(self):
        self.z += self.speed * time.dt
        if self.z >= 550:
            if self.enemy_tower:
                self.enemy_tower.take_damage(self.damage)
            destroy(self)