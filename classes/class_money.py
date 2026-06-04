from ursina import time

class Money:
    def __init__(self, game, start_amount=0):
        self.game = game
        self.amount = start_amount
        self.passive_income_timer = 0
        self.passive_income_per_second = 5

    def update(self):
        self.passive_income_timer += time.dt
        if self.passive_income_timer >= 1:
            self.add(self.passive_income_per_second)
            self.passive_income_timer = 0

    def add(self, value):
        self.amount += value
        self.game.money_text.text = f'{self.amount}'

    def spend(self, value):
        if self.amount >= value:
            self.amount -= value
            self.game.money_text.text = f'{self.amount}'
            return True
        return False