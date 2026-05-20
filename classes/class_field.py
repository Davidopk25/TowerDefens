from ursina import *

class Field(Entity):
    def __init__(self, **kwargs):
        self.player_spawn_z = 80
        self.enemy_spawn_z = 520
        super().__init__(
            position=(0, 0, 0),
            rotation=(0, -180, 0),
            scale=10,
            model="models/Field.obj",
            color=color.gray,
            collider='box',
            **kwargs
        )
        self.path_z_start = 0
        self.path_z_end = 600
        lane_offsets = [-88, 0, 88]
        self.lanes = []

        for offset in lane_offsets:
            lane = Entity(
                parent=scene,
                model='cube',
                color=color.rgba(255, 255, 255, 120),
                position=(offset, 0.05, (self.path_z_start + self.path_z_end) /2),
                scale=(2, 0.02, self.path_z_end - self.path_z_start),
            )
            self.lanes.append(lane)
