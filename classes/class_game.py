from ursina import *
from classes.class_money import Money
from ursina.models.procedural.quad import Quad
from . import *

class Game:
    def __init__(self):
        self.money = Money(self)

        self.money_border = Entity(
            parent=camera.ui,
            model=Quad(radius=0.2),
            color=color.rgba(255, 255, 55, 255),
            position=(-0.28, 0.465, 2),
            scale=(0.27, 0.09)
        )

        self.money_background = Entity(
            parent=camera.ui,
            model=Quad(radius=0.2),
            color=color.rgba(0, 0, 0, 55),
            position=(-0.28, 0.465, 1),
            scale=(0.25, 0.07)
        )

        self.coin_icon = Entity(
            parent=camera.ui,
            model='quad',
            texture='icons/Coin.png',
            position=(-0.31, 0.465),
            scale=(0.07, 0.04),
        )

        self.money_text = Text(
            text=f'{self.money.amount}',
            parent=camera.ui,
            position=(-0.29, 0.4815),
            origin=(-0.5, 0.5),
            scale=1.5,
            color=color.yellow
        )

    def add_money(self, amount):
        self.money_text.text = f'{self.money.amount}'