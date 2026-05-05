from ursina import *

class Field(Entity):
    def __init__(self,**kwargs):
                 super().__init__(
                    position=(0,0,0),
                    rotation=(0,-180,0),
                    scale=10,
                    model="models/Field.obj",
                    color=color.green,
                    collider='box',
                    **kwargs
                    )