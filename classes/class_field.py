from ursina import *

class Field(Entity):
    def __init__(self, game, **kwargs):
        self.player_spawn_z = 30
        self.enemy_spawn_z = 560
        super().__init__(
            position=(0, 0, 0),
            rotation=(0, -180, 0),
            scale=10,
            model="models/Field.obj",
            color=color.gray,
            collider='box',
            **kwargs
        )
        self.game = game
        self.path_z_start = 0
        self.path_z_end = 600
        lane_offsets = [-88, 0, 88]
        self.lanes = []

        for offset in lane_offsets:
            lane = Entity(
                parent=scene,
                model='quad',
                color=color.rgba(255, 255, 255, 120),
                position=(offset, 1, (self.path_z_start + self.path_z_end) /2),
                rotation=(90, 0, 0),
                scale=(2, self.path_z_end - self.path_z_start),
            )
            if lane.texture:
                lane.texture.filtering = 'mipmap'

            self.lanes.append(lane)