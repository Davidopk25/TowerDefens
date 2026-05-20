from ursina import *

from classes.__init__ import (
    Game,
    Field,
    Tower,
    # Menu
    )

if __name__ == "__main__":
    app = Ursina(size=(720, 1080))

    window.vsync = False
    window.title = "Tower Defense"
    window.borderless = False

    camera.position = (0, 525, -200)
    camera.rotation_x = 45
    # EditorCamera()


    game = Game()

    field = Field()

    tower = Tower()
    player_tower = Tower(team='player')
    bot_tower = Tower(team='bot')

    sky = Sky(Texture="sky_sunset")

    # menu = Menu(game)

    app.run()


# 1. Добавить небо, окружение
# 2. Сделать запекание
# 3. Добавить team
# 4. Добавить монеты (их кол-во)








# from ursina import *
# import random


# # --- ПЕРЕМЕННЫЕ ИГРЫ ---
# game_active = True
# player_money = 100
# lanes = [-3, 0, 3] # Координаты линий: Слева, Центр, Справа

# # Текст денег
# money_text = Text(text=f'Gold: {player_money}', position=(-0.45, 0.45), scale=2, origin=(0, 0), background=True)

# # --- КЛАССЫ ---



# # --- ИНТЕРФЕЙС И ЛОГИКА ---

# def update_money_ui():
#     money_text.text = f'Gold: {player_money}'

# def spawn_unit(u_type, cost):
#     global player_money
#     if player_money >= cost:
#         player_money -= cost
#         update_money_ui()
#         # Спавним юнита в случайной линии или выбранной (сейчас рандом для простоты)
#         lane = random.choice(lanes)
#         GameUnit(team='player', u_type=u_type, lane_x=lane)
#         spawn_menu.enabled = False
#     else:
#         print("Not enough gold!")

# # Меню спавна (изначально скрыто)
# spawn_menu = Entity(parent=camera.ui, enabled=False, position=(0, -0.3))
# bg_menu = Entity(parent=spawn_menu, model='quad', scale=(0.8, 0.3), color=color.black66)
# b_melee = Button(parent=spawn_menu, text='Melee\n15g', scale=0.15, x=-0.25, color=color.green, on_click=lambda: spawn_unit('melee', 15))
# b_range = Button(parent=spawn_menu, text='Range\n25g', scale=0.15, x=0, color=color.lime, on_click=lambda: spawn_unit('range', 25))
# b_giant = Button(parent=spawn_menu, text='Giant\n60g', scale=0.15, x=0.25, color=color.azure, on_click=lambda: spawn_unit('giant', 60))

# # --- СОЗДАНИЕ МИРА ---

# # Фон и поле
# ground = Entity(model='quad', scale=(10, 16), color=color.rgb(34, 139, 34), z=1)
# center_line = Entity(model='quad', scale=(10, 0.1), color=color.black, z=0.9)
# enemy_zone_line = Entity(model='quad', scale=(10, 0.05), y=4, color=color.red, z=0.9)
# player_zone_line = Entity(model='quad', scale=(10, 0.05), y=-4, color=color.green, z=0.9)


# # Баллисты (декор + базовая логика урона может быть добавлена как в классе Unit)
# for x_pos in [-2, 0, 2]:
#     Entity(model='cube', scale=0.5, color=color.brown, position=(x_pos, -6.5, -0.5))

# # --- ФОНОВЫЕ ЗАДАЧИ ---

# def passive_income():
#     global player_money
#     player_money += 10
#     update_money_ui()
#     invoke(passive_income, delay=2) # Каждые 2 секунды

# def spawn_falling_coin():
#     FallingCoin()
#     invoke(spawn_falling_coin, delay=random.randint(10, 30))

# def enemy_ai():
#     # Простой ИИ: спавнит рандомного юнита каждые 3-6 секунд
#     if game_active:
#         u_type = random.choice(['melee', 'range'])
#         GameUnit(team='enemy', u_type=u_type, lane_x=random.choice(lanes))
#     invoke(enemy_ai, delay=random.uniform(3, 6))

# # Запуск таймеров
# passive_income()
# spawn_falling_coin()
# enemy_ai()

# app.run()


