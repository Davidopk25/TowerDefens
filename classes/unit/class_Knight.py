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
        self.health = 300
        self.damage = 40
        self.price = 50
        self.enemy_tower = None

    def update(self):
        self.z += self.speed * time.dt
        if self.z >= 550:
            if self.enemy_tower:
                self.enemy_tower.take_damage(self.damage)
            destroy(self)