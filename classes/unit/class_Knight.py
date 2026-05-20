from ursina import *
enemy_tower = None

class Knight(Entity):
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model='models\Knight.glb',
            scale=(15, 20, 15),
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
            if enemy_tower:
                enemy_tower.take_damage(self.damage)
            destroy(self)