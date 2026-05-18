from ursina import *

class Tower(Entity):
    def __init__(self, team='player',  **kwargs):
            z_position = 600 if team == 'player' else 0
            y_rotation = 0 if team == 'player' else 180

            super().__init__(
                position= (0, -0.5, z_position),
                rotation=(0, y_rotation, 0),
                scale=10,
                model="models/Tower.obj",
                texture="models/Tower.png",
                **kwargs,
                )
            self.team = team
            self.hp = 1500

            self.health_bar = Entity(
                parent=self,
                model='quad',
                color=color.green,
                scale=(0.1, 30),
                position=(0, 15, -5),
                rotation=(0, 0, 90)
                )

            self.health_text = Text(
                parent=self,
                text=str(self.hp),
                position=(0, 14.9, -5.3),
                rotation=(0, 0, 0),
                scale=65,
                color=color.white,
                origin=(0,0)
            )

    def update(self):
        self.health_bar.scale_x = (self.hp / 1500) * 1.5
        self.health_text.text = str(max(0, int(self.hp)))

        if self.hp <= 0:
            print(f"{self.team} tower destroyed!")
            destroy(self)

    def take_damage(self, amount):
        self.hp -= amount

        if self.hp < 0:
            self.hp = 0

        # def on_click(self):
        #     if self.team == 'player':
        #         spawn_menu.enabled = not spawn_menu.enabled