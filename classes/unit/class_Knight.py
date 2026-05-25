from ursina import *

class Knight(Entity):
    price = 50
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model='models/Knight.glb',
            scale=(15, 20, 15),
            position=position,
            **kwargs
        )
        self.speed = 60
        self.health = 300
        self.damage = 40
        self.enemy_tower = None

    def update(self):
        self.z += self.speed * time.dt
        if self.speed > 0 and self.z >= 550:
            if self.enemy_tower:
                self.enemy_tower.take_damage(self.damage)
            destroy(self)
        elif self.speed < 0 and self.z <= 50:
            if self.enemy_tower:
                self.enemy_tower.take_damage(self.damage)
            destroy(self)