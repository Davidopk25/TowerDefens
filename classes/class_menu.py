from .unit.class_Knight import Knight
from .unit.class_archer import Archer
from .unit.class_giant import Giant
from ursina import *

class Menu(Entity):
    def __init__(self, game, field, enemy_tower):
        super().__init__(parent=field)
        self.game = game
        self.field = field
        self.enemy_tower = enemy_tower
        self.groups = []
        self.lane_offsets = [88, 0, -88]

        right_group = []

        sword_right = Button(
            parent=self,
            model='quad',
            texture='icons/Sword.png',
            position=(16, 6, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Knight", 2)
        )

        bow_right = Button(
            parent=self,
            model='quad',
            texture='icons/Bow.png',
            position=(13.75, 5, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Bow", 2)
        )

        giant_right = Button(
            parent=self,
            model='quad',
            texture='icons/Giant.png',
            position=(12.5, 1.5, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Giant", 2)
        )

        right_group.extend([sword_right, bow_right, giant_right])

        Button(
            parent=self,
            model='quad',
            texture='icons/Blank.png',
            position=(6.8, 27, 9),
            scale=(2.5, 2.5),
            billboard=True,
            color=color.rgba(255, 255, 255, 0),
            highlight_color=color.rgba(255, 255, 255, 0),
            pressed_color=color.rgba(255, 255, 255, 0),
            text='',
            on_click=lambda: self.toggle_group(right_group)
        )

        center_group = []

        sword_center = Button(
            parent=self,
            model='quad',
            texture='icons/Sword.png',
            position=(3, 6, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Knight", 1)
        )

        bow_center = Button(
            parent=self,
            model='quad',
            texture='icons/Bow.png',
            position=(0, 8, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Bow", 1)
        )

        giant_center = Button(
            parent=self,
            model='quad',
            texture='icons/Giant.png',
            position=(-3, 6, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Giant", 1)
        )

        center_group.extend([sword_center, bow_center, giant_center])

        Button(
            parent=self,
            model='quad',
            texture='icons/Blank.png',
            position=(0, 27, 8),
            scale=(2.5, 2.5),
            billboard=True,
            color=color.rgba(255, 255, 255, 0),
            highlight_color=color.rgba(255, 255, 255, 0),
            pressed_color=color.rgba(255, 255, 255, 0),
            text='',
            on_click=lambda: self.toggle_group(center_group)
        )

        left_group = []

        sword_left = Button(
            parent=self,
            model='quad',
            texture='icons/Sword.png',
            position=(-16, 6, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Knight", 0)
        )

        bow_left = Button(
            parent=self,
            model='quad',
            texture='icons/Bow.png',
            position=(-13.75, 5, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Bow", 0)
        )

        giant_left = Button(
            parent=self,
            model='quad',
            texture='icons/Giant.png',
            position=(-12.5, 1.5, -8),
            scale=(2.5, 2.5),
            billboard=True,
            enabled=False,
            color=color.white,
            highlight_color=color.light_gray,
            pressed_color=color.gray,
            text='',
            on_click=lambda: self.spawn_unit("Giant", 0)
        )

        left_group.extend([sword_left, bow_left, giant_left])


        self.enabled = False

        Button(
            parent=self,
            model='quad',
            texture='icons/Blank.png',
            position=(-6.8, 27, 9),
            scale=(2.5, 2.5),
            billboard=True,
            color=color.rgba(255, 255, 255, 0),
            highlight_color=color.rgba(255, 255, 255, 0),
            pressed_color=color.rgba(255, 255, 255, 0),
            text='',
            on_click=lambda: self.toggle_group(left_group)
        )

    def toggle_group(self, group):
        visible = not group[0].enabled
        for button in group:
            button.enabled = visible

    def spawn_unit(self, unit_type, lane_index):
        lane_x = self.lane_offsets[lane_index]
        spawn_position = (
            lane_x,
            10,
            self.field.player_spawn_z
        )
        unit_class = None
        if unit_type == "Knight":
            unit_class = Knight
        elif unit_type == "Bow":
            unit_class = Archer
        elif unit_type == "Giant":
            unit_class = Giant
        if unit_class is None:
            return
        if not self.game.money.spend(unit_class.price):
            print("Не хватает монет")
            return
        unit = unit_class(position=spawn_position)
        unit.enemy_tower = self.enemy_tower
        if '__main__' in sys.modules and hasattr(sys.modules['__main__'], 'active_units'):
           sys.modules['__main__'].active_units.append(unit)