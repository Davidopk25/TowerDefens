from ursina import *
import random

class FallingCoin(Button):
    def __init__(self, game, field, **kwargs):
        self.game = game
        self.field = field
        half_x = field.scale_x / 2
        half_z = field.scale_z / 2
        x = random.uniform(field.x - half_x, field.x + half_x)
        z = random.uniform(field.z - half_z, field.z + half_z)
        super().__init__(
            parent=scene,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.white,
            model='models/Coin.obj',
            texture='models/Coin.png',
            scale=10,
            position=(x, 100, z),
            rotation_x = 90,
            collider='box',
            **kwargs
        )
        self.rotation_speed = 270
        self.fall_speed = 100
        self.grounded = False
        invoke(self.remove_coin, delay=10)

    def update(self):
        if not self.grounded:
            self.y -= time.dt * self.fall_speed
            if self.y <= 13:
                self.y = 13
                self.grounded = True
        self.rotation_y += time.dt * self.rotation_speed

    def on_click(self):
        self.game.money.add(50)
        destroy(self)

    def remove_coin(self):
        if self.enabled:
            destroy(self)