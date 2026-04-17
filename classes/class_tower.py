from ursina import *

class Tower(Entity):
    def __init__(self, **kwargs): #team
                super().__init__(
                    position= (0, 0, 0),
                    rotation=(0, -180, 0),
                    scale=10,
                    model="models\Tower.obj",
                    texture="models\Tower.png",
                    # color=color.white,
                    **kwargs
                    # color=color.blue, if team == 'player' else color.red,
                    )
                # self.team = team
                # self.hp = 1000
                # self.y = -7 if team == 'player' else 7
        # self.health_bar = Entity(parent=self, model='quad', color=color.green, scale=(1.5, 0.2), y=1.2)

        # def update(self):
        #     self.health_bar.scale_x = (self.hp / 1000) * 1.5
        #     if self.hp <= 0:
        #         print(f"{self.team} tower destroyed!")
        #         destroy(self)
            # Тут можно добавить экран победы/поражения

    # def on_click(self):
    #     if self.team == 'player':
    #         spawn_menu.enabled = not spawn_menu.enabled








# from ursina import *
# from unit import Unit

# class Tower(Entity):

#     def __init__(self, game, position):

#         super().__init__(
#             model='cube',
#             scale=2,
#             position=position,
#             color=color.dark_gray
#         )

#         self.game = game

#     def update(self):

#         for unit in self.game.units:

#             if distance(self, unit) < 10:

#                 unit.hp -= 5 * time.dt