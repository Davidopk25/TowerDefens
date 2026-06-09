from ursina import *

window.vsync = False

app = Ursina()

ter_list = [
    'models/dezert.jpg',
    'models/p2.jpg',
    'models/river.jpg',
    'models/wood.jpg'
]



obj = Terrain(heightmap=ter_list[0], skip=10)

terrian = Entity(model=obj, scale=(20, 4, 10), texture=ter_list[0])

hv = terrian.model.height_values

player = Entity(model='sphere', scale=.2, color=Vec4(1, 0, 0, 1), position=(0, 5, 0), collider='sphere')

camera.position = player.position + (0, 5, -15)
camera.rotation_x = 25

def update():
    direction = Vec3(held_keys['d'] - held_keys['a'], 0, held_keys['w'] -  held_keys['s']).normalized()

    player.position += direction * 2 * time.dt

    y = terraincast(player.position, terrian, hv)

    if y:
        player.y = y + .1




app.run()