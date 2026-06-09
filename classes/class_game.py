from ursina import *
from classes.class_money import Money
from ursina.models.procedural.quad import Quad
from . import *

class Game:
    def __init__(self):
        self.money = Money(self)

        self.ui_container = Entity(parent=camera.ui)

        self.money_background = Entity(
            parent=self.ui_container,
            model=Quad,
            color=color.rgba(0, 0, 0, 55),
            position=(-0.250, 0.455, 1),
            scale=(0.15, 0.065)
        )

        self.coin_icon = Entity(
            parent=self.ui_container,
            model='quad',
            texture='icons/Coin.png',
            position=(-0.295, 0.455),
            scale=(0.1, 0.055),
        )

        self.money_text = Text(
            text=f'{self.money.amount}',
            parent=self.ui_container,
            position=(-0.275, 0.462),
            origin=(-0.75, 0.3),
            scale=1.4,
            color=color.yellow
        )

    def add_money(self, amount):
        self.money_text.text = f'{self.money.amount}'