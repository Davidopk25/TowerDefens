# from ursina import *

# class GameUnit(Entity):
#     def init(self, team, u_type, lane_x):
#         super().init()
#         self.team = team # 'player' или 'enemy'
#         self.u_type = u_type # 'melee', 'range', 'giant'
#         self.x = lane_x

#         # Настройки в зависимости от типа
#         if self.u_type == 'melee':
#             self.model = 'cube'
#             self.hp = 100
#             self.damage = 20
#             self.speed = 1.5
#             self.attack_speed = 1.0
#             self.range = 1
#             self.color = color.green if team == 'player' else color.red
#             self.scale = 0.8

#         elif self.u_type == 'range':
#             self.model = 'sphere'
#             self.hp = 60
#             self.damage = 15
#             self.speed = 2.0
#             self.attack_speed = 1.2
#             self.range = 4
#             self.color = color.lime if team == 'player' else color.orange
#             self.scale = 0.6

#         elif self.u_type == 'giant':
#             self.model = 'cube'
#             self.hp = 400
#             self.damage = 50
#             self.speed = 0.8
#             self.attack_speed = 2.0
#             self.range = 1.5
#             self.color = color.azure if team == 'player' else color.pink
#             self.scale = 1.5

#         # Позиция спавна
#         start_y = -6 if team == 'player' else 6
#         self.y = start_y
#         self.z = 0

#         self.target = None
#         self.attack_cooldown = 0

#         # Анимация "ходьбы" (покачивание)
#         self.animate_rotation_z(5, duration=0.5, loop=True, curve=curve.linear)

#     def update(self):
#         global player_money
#         if not game_active: return

#         # Движение
#         direction = 1 if self.team == 'player' else -1

#         # Поиск врагов
#         enemies = [e for e in scene.entities if isinstance(e, (GameUnit, Tower)) and e.team != self.team]
#         if not enemies:
#             self.y += self.speed * time.dt * direction
#             return



#         # Найти ближайшего врага
#         closest = min(enemies, key=lambda e: distance(e, self))
#         dist = distance(closest, self)

#         if dist <= self.range:
#             # Атака
#             self.attack_cooldown -= time.dt
#             if self.attack_cooldown <= 0:
#                 closest.hp -= self.damage
#                 self.animate_scale(self.scale * 1.2, duration=0.1) # Эффект удара
#                 self.animate_scale(self.scale, duration=0.1, delay=0.1)
#                 self.attack_cooldown = self.attack_speed

#                 if closest.hp <= 0:
#                     if self.team == 'player' and not isinstance(closest, Tower):
#                         player_money += 15 # Награда за убийство
#                         update_money_ui()
#                     destroy(closest)
#         else:
#             # Идти вперед
#             self.y += self.speed * time.dt * direction