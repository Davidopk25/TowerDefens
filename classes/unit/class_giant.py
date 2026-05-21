from ursina import *
enemy_tower = None

class Giant(Entity):
    price = 150
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model = 'models\Giant1.glb',
            scale=(15, 20, 15),
            rotation=(0, 180, 0),
            position=position,
            **kwargs
        )
        self.speed = 30
        self.health = 900
        self.damage = 65
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