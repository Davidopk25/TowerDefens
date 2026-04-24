from ursina import *
from ursina import camera
from . import *

class Game:
    def __init__(self):
        self.money = 0

        self.coin_icon = Entity(
            parent=camera.ui,
            model='quad',
            texture='icons/coin.png',
            position=(-0.31, 0.465),
            scale=(0.07, 0.04)
        )

        self.money_text = Text(
            text=f'{self.money}',
            parent=camera.ui,
            position=(-0.29, 0.48),
            origin=(-0.5, 0.5),
            scale=1.5,
            color=color.yellow
        )

    def add_money(self, amount):
        self.money += amount
        self.money_text.text = f'{self.money}'