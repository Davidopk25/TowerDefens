from ursina import Button, color, Entity, camera
from .unit.__init__ import Archer,Giant,Swordsman

class Menu(Entity):

    def __init__(self, game):

        super().__init__(parent=camera.ui)

        self.game = game

        menu_1 = Entity()
        menu_2 = Entity()

        Button(
            parent=menu_1,
            color=color.rgba(55,55,55,256),
            # radius=(1,1),
            position=(0,0),
            scale=(5,5),
            # on_click=switch(menu_1)
        )

        Button(
             parent=menu_1,
            color=color.rgba(55,55,55,256),
            # radius=(1,1),
            position=(5,0),
            scale=(5,5),
            on_click=lambda: setattr( 'enabled', False),
        )

        Button(
             parent=menu_1,
            color=color.rgba(55,55,255,256),
            # radius=(1,1),
            position=(-5,0),
            scale=(5,5),
            on_click=lambda: setattr( 'enabled', False),
        )

        Button(
            parent= menu_2,
            texture="icons\Меч.png",
            on_click=lambda:Swordsman(self.game,0,0)
        )

        Button(
            parent= menu_2,
            texture="icons\Лук.png",
            on_click=lambda:Archer(self.game,0,0)
        )

        Button(
            parent= menu_2,
            texture="icons\Гигант.png",
            on_click=lambda: Giant(self.game,0,0)
        )

        def switch():
            menu_1.disable()
            menu_2.enable()
