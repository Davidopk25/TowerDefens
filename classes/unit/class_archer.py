from ursina import *
enemy_tower = None

class Archer(Entity):
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model='models\Knight.glb',
            scale=(8, 14, 8),
            position=position,
            **kwargs
        )
        self.speed = 70
        self.health = 150
        self.damage = 35
        self.price = 60
        self.enemy_tower = None

    def update(self):
        self.z += self.speed * time.dt
        if self.z >= 550:
            if enemy_tower:
                enemy_tower.take_damage(self.damage)
            destroy(self)