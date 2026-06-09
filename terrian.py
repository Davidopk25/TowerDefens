from ursina import *

window.vsync = False

app = Ursina()

ter_list = [
    'models/dezert.jpg'
    # 'models/p2.jpg',
    # 'models/river.jpg',
    # 'models/wood.jpg'
]



obj = Terrain(heightmap=ter_list[0], skip=25)

terrian = Entity(model=obj, scale=(20, 2, 10), texture=ter_list[0])


EditorCamera()


app.run()