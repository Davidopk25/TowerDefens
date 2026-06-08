from ursina import *
 
class Ballista(Entity):
    def __init__(self, target_team, lane_x, custom_scale = 7.5, **kwargs):
        super().__init__(
            model='models/Ballista.obj',
            scale=custom_scale,
            **kwargs
        )
        self.target_team = target_team  # 'player' или 'enemy'
        self.lane_x = lane_x
        self.attack_range = 150
        self.damage = 30
        self.cooldown = 1.5
        self.timer = 0
        
        # Стрела (как дочерний объект)
        self.arrow = Entity(parent=self, model='models/Strela.obj', scale=1, enabled=False)
 
    def update(self):
        self.timer += time.dt
        if self.timer >= self.cooldown:
            units = sys.modules['__main__'].active_units
            target = self.find_target(units)
            if target:
                self.shoot(target)
                self.timer = 0
                print(f"{self.target_team.capitalize()} ballista shoots at {target.name}")
 
    def find_target(self, all_units):
        for unit in all_units:
            if not unit or getattr(unit, 'destroyed', False):
                continue

            if abs(unit.x - self.lane_x) < 40:

                dist_to_tower = abs(unit.z - (self.enemy_tower.z if hasattr(self, 'enemy_tower') else 0))

                if unit.enemy_tower and hasattr(unit.enemy_tower, 'z'):
                    dist_to_tower = abs(unit.z - unit.enemy_tower.z)

                    is_attacking_tower = dist_to_tower <= unit.attack_range
                    
                    if is_attacking_tower:

                        if self.target_team == 'player' and unit.speed < 0:
                            return unit
                        elif self.target_team == 'enemy' and unit.speed > 0:
                            return unit
        return None
 
    def shoot(self, target):
        projectile = Entity(
            model='models/Strela.obj',
            position=self.world_position + Vec3(0, 10, 0),
            scale=5,
            color=color.white
        )
        
        projectile.look_at(target.world_position)

        projectile.animate_position(target.world_position + Vec3(0, 5, 0), duration=0.5, curve=curve.linear)

        invoke(lambda: self.deal_damage(target, projectile), delay=0.5)
        
    def deal_damage(self, target, projectile):
        destroy(projectile)
        if target:
            target.health -= self.damage
            if target.health <= 0:
                destroy(target)
                
    @classmethod
    def spawn_ballistas(cls, tower_position, team, enemy_tower, z_offset):
        # Настройки смещения: теперь их легко править
        spawn_x = [-135, 0, 135]
        spawn_y = [75, 100, 75]  # Высота для каждой из 3-х баллист
        
        lane_offsets = [-88, 0, 88]
        ballistas = []
    
        scales = [7.5, 10, 7.5]
        for i in range(len(spawn_x)):
            rotation_y = 180 if team == 'player' else 0
    
            # Собираем позицию: к координатам башни добавляем смещение
            pos = (
                tower_position.x + spawn_x[i],
                tower_position.y + spawn_y[i],
                tower_position.z + z_offset
            )
    
            ballista = cls(
                target_team=team,
                lane_x=lane_offsets[i],
                custom_scale=scales[i],
                enemy_tower=enemy_tower,
                position=pos,
                rotation=(0, rotation_y, 0)
            )
            ballistas.append(ballista)
        return ballistas