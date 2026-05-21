from ursina import *
from .unit.class_Knight import Knight
from .unit.class_Archer import Archer
from .unit.class_Giant import Giant
import random

class Bot:
    def __init__(self, field):
        self.field = field
        self.money = 100
        self.passive_income_timer = 0
        self.passive_income_per_second = 5
        self.action_timer = random.uniform(3, 8)
        self.lane_offsets = [88, 0, -88]
        self.units = [
            Knight,
            Archer,
            Giant
        ]

    def update(self):
        self.passive_income_timer += time.dt
        if self.passive_income_timer >= 1:
            self.money += self.passive_income_per_second
            self.passive_income_timer = 0
        self.action_timer -= time.dt
        if self.action_timer <= 0:
            self.try_spawn_unit()
            self.action_timer = random.uniform(3, 8)

    def try_spawn_unit(self):
        unit_class = random.choice(self.units)
        if self.money < unit_class.price:
            print("Боту не хватает монет")
            return
        self.money -= unit_class.price
        lane_index = random.randint(0, 2)
        lane_x = self.lane_offsets[lane_index]
        spawn_position = (
            lane_x,
            10,
            self.field.enemy_spawn_z
        )
        unit = unit_class(
            position=spawn_position,
            rotation=(0, 0, 0)
        )
        unit.speed = -abs(unit.speed)
        unit.enemy_tower = self.field.enemy_tower
        print(
            f"Бот заспавнил {unit_class.__name__} "
            f"на линии {lane_index}"
        )