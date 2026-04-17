# class FallingCoin(Button):
#     def init(self):
#         super().init(
#             parent=scene,
#             model='circle',
#             color=color.gold,
#             scale=0.8,
#             position=(random.uniform(-4, 4), random.uniform(-4, 4), -1),
#             highlight_color=color.yellow
#         )
#         self.glow = PointLight(parent=self, color=color.yellow)
#         self.animate_scale(1, duration=0.5)
#         # Исчезнет через 5 сек если не нажать (20 сек ожидания)
#         invoke(self.remove_coin, delay=5)

#     def remove_coin(self):
#         if self: destroy(self)

#     def on_click(self):
#         global player_money
#         player_money += 20
#         update_money_ui()
#         destroy(self)