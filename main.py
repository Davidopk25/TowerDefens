# from classes.class_FallingCoin import FallingCoin
from classes.class_menu import Menu
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
    camera.position = (0, 475, -200)
    camera.rotation_x = 45
    # EditorCamera()
    game = Game()
    field = Field()
    menu = Menu(game, field)
    tower = Tower()
    player_tower = Tower(team='player')
    bot_tower = Tower(team='bot')
    sky = Sky(Texture="sky_sunset")
    # ground = Entity(
    #     model='plane',
    #     scale=(275, 1, 400),
    #     position=(0, 0, 300),
    #     visible=False,
    #     color=color.blue,
    #     collider='box'
    # )


    app.run()


