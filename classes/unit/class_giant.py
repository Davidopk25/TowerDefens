from ursina import *
enemy_tower = None

class Giant(Entity):
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model = 'models\Giant1.glb',
            scale=(15, 22, 15),
            rotation=(0, 180, 0),
            position=position,
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
            if enemy_tower:
                enemy_tower.take_damage(self.damage)
            destroy(self)