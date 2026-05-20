# import time
# import threading

# import random

# class Bots:
# # Добавление монет боту
#     coins = 100
#     # def add_coins():
#     #     global coins
#     #     while True:
#     #         time.sleep(5)
#     #         coins += 1

#     # threading.Thread(target=add_coins, daemon=True).start()

#     def Bot():
#         global unit
#         global coins
#         unit = random.randint(1, 3)
#         print (coins)
#         if unit == 1:
#             if (coins / 2) >= 10:
#                 print ("Меч")
#                 coins = -10
#             else:
#                 Bots.Bot()
#         elif unit == 2:
#             if (coins / 2) >= 20:
#                 print ("Лучник")
#                 coins = -20
#             else:
#                 Bots.Bot()
#         elif unit == 3:
#             if (coins / 2) >= 30:
#                 print ("Гигант")
#                 coins = -30
#             else:
#                 Bots.Bot()

# bots = Bots()

# while True:
#     time_bot = random.randint(1, 10)
#     time.sleep(time_bot)
#     Bots.Bot()

import time
import threading
import random

class Bot:
    """
    Класс, представляющий одного бота-игрока.
    """
    def __init__(self):
        # Баланс монет для каждого бота индивидуален
        self.coins = 100
        self.is_running = True

        # Запускаем поток для пополнения монет
        self._start_coins_thread()

    def _start_coins_thread(self):
        """Запускает поток, который добавляет монеты."""
        def add_coins():
            while self.is_running:
                # Добавляем случайное количество монет от 1 до 5 каждые несколько секунд
                time.sleep(random.randint(2, 5))
                self.coins += random.randint(1, 5)
                print(f"Монеты пополнены! Текущий баланс: {self.coins}")

        # Поток будет завершаться вместе с основной программой
        thread = threading.Thread(target=add_coins, daemon=True)
        thread.start()

    def buy_unit(self):
        """Попытка купить юнита."""
        prices = {1: 10, 2: 20, 3: 30}
        ways = {1: (10, 10), 2: (10, 20), 3: (10, 30)}
        unit_type = random.randint(1, 3)
        unit_way = random.randint(1, 3)
        while True:
            price = prices[unit_type]
            way = ways[unit_way]
            # Проверяем, хватает ли монет на покупку
            if self.coins >= price:
                unit_names = {1: "Меч", 2: "Лучник", 3: "Гигант"}
                print(f"Куплен юнит: {unit_names[unit_type]}. Цена: {price} монет. Поставлен на {way}")
                self.coins -= price
                break  # Выходим из цикла после успешной покупки
            else:
                # Если не хватает, ждем немного и пробуем снова
                print(f"Не хватает {price - self.coins} монет для покупки. Ждем...")
                time.sleep(1)

    def stop(self):
        """Останавливает работу бота."""
        self.is_running = False

# --- Основная программа ---
if __name__ == "__main__":
    # Создаем экземпляр бота
    my_bot = Bot()

    try:
        # Бесконечный цикл основной логики
        while True:
            # Боты действуют с разной частотой
            time.sleep(random.randint(1, 5))
            my_bot.buy_unit()

    except KeyboardInterrupt:
        # Позволяет корректно остановить программу по Ctrl+C
        print("\nОстановка симуляции...")
        my_bot.stop()




