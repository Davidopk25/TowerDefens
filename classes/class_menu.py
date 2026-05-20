
from .unit.class_Knight import Knight
from .unit.class_Archer import Archer
from .unit.class_Giant import Giant
from ursina import *

class Menu(Entity):
    def __init__(self, game, field):
        super().__init__(parent=field)
        self.groups = []
        self.field = field
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

        blank_right = Button(
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

        blank_center = Button(
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

        blank_left = Button(
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
        unit = None
        if unit_type == "Knight":
            Knight(position=spawn_position)
        elif unit_type == "Bow":
            Archer(position=spawn_position)
        elif unit_type == "Giant":
            Giant(position=spawn_position)
        if unit:
            print(self.field.enemy_tower)
            unit.enemy_tower = self.enemy_tower
