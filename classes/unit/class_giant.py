from ursina import *

class Giant(Entity):
    def __init__(self):
        super().__init__(
            model='models\Gigant.blend',
            speed=30,
            attack_speed=2.0,
            health=900,
            damage=65,
            price=150
            )