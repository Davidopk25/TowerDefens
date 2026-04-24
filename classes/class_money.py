class Money:
    def __init__(self, game, start_amount=0):
        self.game = game
        self.amount = start_amount

    def add(self, value):
        self.amount += value
        self.game.add_money(value)

    def spend(self, value):
        if self.amount >= value:
            self.amount -= value
            self.game.money -= value
            self.game.money_text.text = f'Money: {self.game.money}'
            return True
        return False