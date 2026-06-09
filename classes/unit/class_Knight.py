from ursina import *

class Knight(Entity):
    price = 50
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__(
            model='models/Knight.glb',
            scale=(15, 20, 15),
            rotation=(0, 180, 0),
            position=position,
            collider='box',
            **kwargs
        )
        self.speed = 65
        self.health = 60
        self.damage = 20
        self.enemy_tower = None
        self.attack_cooldown = 0.8
        self.attack_timer = 0 # Таймер для отсчета времени до следующего удара
        self.max_health = 60
        self.attack_range = 45
        self.health_bar = Entity(
            parent=self,
            model='quad',
            color=color.green,
            scale=(1.5, 0.15),
            position=(0, 1.5, 0),
            billboard=True
        )
    def update(self):
        if hasattr(self, 'max_health') and self.max_health > 0:
            base_scale = 1.5 if self.__class__.__name__ == 'Knight' else (2.0 if self.__class__.__name__ == 'Giant' else 1.5)
            self.health_bar.scale_x = (self.health / self.max_health) * base_scale

        if self.health <= 0:
            destroy(self)
            return

        distance_to_tower = 9999
        if self.enemy_tower and hasattr(self.enemy_tower, 'z'):
            distance_to_tower = abs(self.z - self.enemy_tower.z)

        if distance_to_tower <= self.attack_range:
            self.attack_timer += time.dt
            if self.attack_timer >= self.attack_cooldown:
                if self.enemy_tower:
                    self.enemy_tower.take_damage(self.damage)
                self.attack_timer = 0
            return

        direction = (0, 0, 1) if self.speed > 0 else (0, 0, -1)

        ignore_list = [self, self.health_bar]
        if hasattr(self, 'my_tower') and self.my_tower:
            ignore_list.append(self.my_tower)
        elif hasattr(self, 'friendly_tower') and self.friendly_tower:
            ignore_list.append(self.friendly_tower)

        hit_info = raycast(self.world_position + Vec3(0, 2, 0), direction, distance=80, ignore=ignore_list)

        if hit_info.hit and hit_info.entity:
            target = hit_info.entity

            if hasattr(target, 'speed') and (self.speed * target.speed < 0):

                dist_to_enemy = abs(self.z - target.z)

                if dist_to_enemy > self.attack_range:

                    pass
                else:
                    self.attack_timer += time.dt
                    if self.attack_timer >= self.attack_cooldown:
                        target.health -= self.damage
                        self.attack_timer = 0
                        if target.health <= 0:
                            destroy(target)
                    return

        self.attack_timer = 0
        self.z += self.speed * time.dt