from ursina import *
enemy_tower = None

class Archer(Entity):
    price = 60
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model='models\Knight.glb',
            scale=(8, 14, 8),
            position=position,
            **kwargs
        )
        self.speed = 70
        self.health = 30
        self.damage = 50
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