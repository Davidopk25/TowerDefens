import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from classes.class_FallingCoin import FallingCoin
from classes.class_field import Field
from classes.class_tower import Tower1, Tower2
from classes.class_menu import Menu
from classes.class_game import Game
from classes.class_bot import Bot
from classes.splach_screens import SplashScreen
from classes.unit import class_Knight, class_Archer, class_Giant
from classes.class_ballista import Ballista
from ursina import *
import random

active_units = []
active_coins = []

ui_overlay = None
ui_text = None
ui_restart_btn = None

game_is_over = False
game_started = False

main_menu_panel = None

def init_game():
    """ Функция полной инициализации и перезапуска игры до заводских настроек """
    global game, field, player_tower, enemy_tower, menu, my_bot, active_units, active_coins, game_is_over, game_started

    game_is_over = False
    game_started = False

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
    game.ui_container.enabled = False

    player_tower = Tower1(team='enemy')  # Ваша башня
    enemy_tower = Tower2(team='player')  # Башня бота
    
    Ballista.spawn_ballistas(player_tower.position, 'player', enemy_tower=player_tower, z_offset=20)
    Ballista.spawn_ballistas(enemy_tower.position, 'enemy', enemy_tower=enemy_tower,z_offset=-20)

    class_Knight.enemy_tower = player_tower
    class_Archer.enemy_tower = player_tower
    class_Giant.enemy_tower = player_tower

    field.player_tower = player_tower
    field.enemy_tower = enemy_tower

    menu = Menu(game=game, field=field, enemy_tower=enemy_tower)
    menu.enemy_tower = enemy_tower
    menu.enabled = False

    # Перезапускаем бота
    my_bot = Bot(field)
    my_bot.money = 100

def create_main_menu():
    """ Создает маленькую панель главного меню с кнопками Играть и Выйти """
    global main_menu_panel

    main_menu_panel = Entity(
        parent=camera.ui,
        model='quad',
        color=color.rgba(0, 0, 0, 180),
        scale=(0.8, 1),
        position=(0, 0),
        collider='box'
    )

    # Кнопка Играть
    Button(
        parent=main_menu_panel,
        text='Играть',
        scale=(0.275, 0.075),
        position=(0, 0.055, -1),
        color=color.cyan,
        text_color=color.black,
        on_click=start_battle
    )

    # Кнопка Выйти
    Button(
        parent=main_menu_panel,
        text='Выйти',
        scale=(0.2, 0.065),
        position=(0, -0.055, -1),
        color=color.red,
        text_color=color.white,
        on_click=application.quit
    )

def start_battle():
    """ Вызывается при нажатии кнопки 'Играть' в Главном Меню """
    global game_started, main_menu_panel, menu, game

    game_started = True

    destroy(main_menu_panel)

    menu.enabled = True
    game.ui_container.enabled = True

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

    # После рестарта снова выводим главное меню
    create_main_menu()

if __name__ == "__main__":
    app = Ursina(size=(720, 1080))
    window.vsync = False
    window.title = "Tower Defense"
    window.borderless = False

    camera.position = (0, 475, -200)
    camera.rotation_x = 45
    # EditorCamera()
# s
    field = Field(game=None)

    sky = Sky(Texture="sky_sunset")
    ground = Entity(
        model='plane',
        scale=(275, 1, 400),
        position=(0, 0, 300),
        visible=False,
        color=color.blue,
        collider='box'
    )

    init_game()

    splash = SplashScreen(on_complete=create_main_menu)

    splash_duration = 5.0
    splash_timer = 0.0
    current_step_index = 0

    def update():
        global splash, splash_timer, current_step_index

        if splash is not None:
            splash_timer += time.dt
            progress_ratio = splash_timer / splash_duration

            if hasattr(splash, 'logo') and splash.logo:
                splash.logo.scale_x = window.aspect_ratio

            if progress_ratio >= 1.0:
                splash.progress_bar.scale_x = 0.5
                splash.finish()
                splash = None
                return

            splash.progress_bar.scale_x = progress_ratio * 0.5

            step_index = int(progress_ratio * len(splash.loading_steps))
            step_index = min(step_index, len(splash.loading_steps) - 1)

            if step_index != current_step_index:
                current_step_index = step_index
                splash.loading_text.text = splash.loading_steps[step_index]

            return

        if game_started and not game_is_over:
            game.money.update()
            my_bot.update()

    def spawn_coin():
        if game_started and not game_is_over:
            FallingCoin(game=game, field=ground)

        invoke(spawn_coin, delay=random.uniform(13, 13))

    spawn_coin()
    app.run()