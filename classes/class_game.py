from ursina import *
from . import *

# settings = Settings()

class Game:
    pass
    # def setup(self):
    #     if settings.game_over:
    #         self.btn_start = ButtonStart()
    #         self.btn_exit = ButtonExit()
    #         self.text_live = TextLive()
    #         self.text_score = TextScore()
    #         self.player = Player()
    #         settings.game_over = False
    #         self.enemies = [Enemy() for _ in range(40)]
    #         self.resources = [Resources() for _ in range(15)]
    #         self.collisions = Collisions()
    #         self.sounds = Sounds()


    # def update(self):

    #     self.text_live.update()
    #     self.text_score.update()
    #     self.collisions.check_collide(
    #         player=self.player,
    #         enemies=self.enemies,
    #         resources=self.resources,
    #         text_live=self.text_live,
    #         text_score=self.text_score,
    #         sounds=self.sounds
    #     )