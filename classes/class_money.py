from ursina import *

class Money(Entity):
    def __init__(self,
                 add_to_scene_entities=True,
                 enabled=False,
                 position=None,
                 rotation=None, scale=1,
                 model='',
                 collider=None,
                 eternal=True,
                 name='Монета',
                 **kwargs):

        super().__init__(add_to_scene_entities,
                         enabled,
                         position,
                         rotation,
                         scale,
                         model,
                         color,
                         collider,
                         eternal,
                         name,
                         **kwargs)














from ursina import *
import random

class Coin(Entity):

    def __init__(self, game):

        super().__init__(
            model='sphere',
            color=color.yellow,
            scale=0.5,
            position=(
                random.uniform(-10,10),
                1,
                random.uniform(-10,10),
            )
        )

        self.game = game

    def input(self, key):

        if self.hovered and key == 'left mouse down':

            self.game.money += 1
            destroy(self)