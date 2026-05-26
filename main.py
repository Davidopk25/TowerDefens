import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from classes.class_FallingCoin import FallingCoin
from classes.class_field import Field
from classes.class_tower import Tower1, Tower2
from classes.class_menu import Menu
from classes.class_game import Game
from classes.class_bot import Bot
from classes.unit import class_Knight, class_Archer, class_Giant
from ursina import *
import random

active_units = []
active_coins = []

ui_overlay = None
ui_text = None
ui_restart_btn = None

game_is_over = False

def init_game():
    """ Функция полной инициализации и перезапуска игры до заводских настроек """
    global game, field, player_tower, enemy_tower, menu, my_bot, active_units, active_coins, game_is_over

    game_is_over = False

    for unit in active_units:
        if unit and not id(unit) == id(None):
            destroy(unit)
    active_units.clear()

    for coin in active_coins:
        if coin:
            destroy(coin)
    active_coins.clear()

    if 'player_tower' in globals() and player_tower: destroy(player_tower)
    if 'enemy_tower' in globals() and enemy_tower: destroy(enemy_tower)
    if 'menu' in globals() and menu: destroy(menu)
    if 'game' in globals() and game and hasattr(game, 'ui_container'):
       destroy(game.ui_container)


    game = Game()
    game.money.amount = 100
    game.money_text.text = f'{game.money.amount}'

    player_tower = Tower1(team='enemy')  # Ваша башня
    enemy_tower = Tower2(team='player')  # Башня бота

    class_Knight.enemy_tower = player_tower
    class_Archer.enemy_tower = player_tower
    class_Giant.enemy_tower = player_tower

    field.player_tower = player_tower
    field.enemy_tower = enemy_tower

    menu = Menu(game=game, field=field, enemy_tower=enemy_tower)
    menu.enemy_tower = enemy_tower

    # Перезапускаем бота
    my_bot = Bot(field)
    my_bot.money = 100


def trigger_game_over(winner):
    """ Вызывается из класса башни, когда у неё 0 ХП """
    global ui_overlay, ui_text, ui_restart_btn, game_is_over

    if game_is_over:
        return
    game_is_over = True

    menu.enabled = False

    ui_overlay = Entity(
        parent=camera.ui,
        model='quad',
        color=color.rgba(0, 0, 0, 200),
        scale=(2, 2),
        z=-10
    )

    if winner == 'player':
        msg = "ПОБЕДА"
        msg_color = color.green
    else:
        msg = "ПОРАЖЕНИЕ"
        msg_color = color.red

    ui_text = Text(
        text=msg,
        parent=camera.ui,
        origin=(0, 0),
        scale=4,
        color=msg_color,
        position=(0, 0.15),
        z=-11
    )

    ui_restart_btn = Button(
        parent=camera.ui,
        model='quad',
        texture='icons/Restart.png',
        scale=(0.25, 0.25),
        position=(0, -0.05),
        color=color.white,
        highlight_color=color.light_gray,
        pressed_color=color.gray,
        z=-11,
        on_click=restart_game
    )


def restart_game():
    """ Очищает элементы UI конца игры и перезапускает мир """
    global ui_overlay, ui_text, ui_restart_btn

    destroy(ui_overlay)
    destroy(ui_text)
    destroy(ui_restart_btn)

    init_game()


if __name__ == "__main__":
    app = Ursina(size=(720, 1080))
    window.vsync = False
    window.title = "Tower Defense"
    window.borderless = False

    camera.position = (0, 475, -200)
    camera.rotation_x = 45
    # EditorCamera()

    field = Field(game=None)

    init_game()

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
        if not game_is_over:
            game.money.update()
            my_bot.update()

            global active_units, active_coins
            active_units = [u for u in active_units if u and u.enabled]
            active_coins = [c for c in active_coins if c and c.enabled]

    def spawn_coin():
        if not game_is_over:
            FallingCoin(game=game, field=ground)
        invoke(spawn_coin, delay=random.uniform(13, 13))

    spawn_coin()
    app.run()