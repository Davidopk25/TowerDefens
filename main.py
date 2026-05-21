import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from classes.class_FallingCoin import FallingCoin
from classes.class_field import Field
from classes.class_tower import Tower
from classes.class_menu import Menu
from classes.class_game import Game
from classes.class_bot import Bot
from classes.unit import class_Knight
from classes.unit import class_Archer
from classes.unit import class_Giant
from ursina import *
import random

if __name__ == "__main__":
    app = Ursina(size=(720, 1080))
    window.vsync = False
    window.title = "Tower Defense"
    window.borderless = False
    # camera.position = (0, 475, -200)
    # camera.rotation_x = 45
    EditorCamera()
    game = Game()
    field = Field(game=game)
    player_tower = Tower(team='player')
    enemy_tower = Tower(team='enemy')
    class_Knight.enemy_tower = player_tower
    class_Archer.enemy_tower = player_tower
    class_Giant.enemy_tower = player_tower
    field.player_tower = player_tower
    field.enemy_tower = enemy_tower
    menu = Menu(game=app, field=field)
    my_bot = Bot(field)

    sky = Sky(Texture="sky_sunset")
    ground = Entity(
        model='plane',
        scale=(275, 1, 400),
        position=(0, 0, 300),
        visible=False,
        color=color.blue,
        collider='box'
    )

    def update():
        game.money.update()
        my_bot.update()

    def spawn_coin():
        FallingCoin(game=game, field=ground)
        invoke(spawn_coin, delay=random.uniform(13, 13))

    spawn_coin()
    app.run()