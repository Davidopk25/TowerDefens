from classes.class_FallingCoin import FallingCoin
from ursina import *
import random

from classes.__init__ import (
    Game,
    Field,
    Tower,
)

if __name__ == "__main__":
    app = Ursina(size=(720, 1080))
    window.vsync = False
    window.title = "Tower Defense"
    window.borderless = False
    # camera.position = (0, 350, -290)
    # camera.rotation = (40, 0, 0)
    EditorCamera()
    game = Game()
    field = Field()
    tower = Tower()
    ground = Entity(
        model='plane',
        scale=(275, 1, 400),
        position=(0, 0, 300),
        visible=False,
        color=color.blue,
        collider='box'
    )

    def update():
        if held_keys['space']:
            game.add_money(1)

    def spawn_coin():
        FallingCoin(game=game, field=ground)
        invoke(spawn_coin, delay=random.uniform(4, 8))

    spawn_coin()
    app.run()