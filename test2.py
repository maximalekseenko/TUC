import pyglet

import pyglet

window = pyglet.window.Window()
window2 = pyglet.window.Window()
print(window.get_size())
# image = pyglet.resource.image('kitten.jpg')

label = pyglet.text.Label('KILL MUTANT',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
label2 = pyglet.text.Label('BURN HERETIC',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')



@window.event
def on_draw():
    window.clear()
    label.draw()

@window2.event
def on_draw():
    window2.clear()
    label2.draw()
    

pyglet.app.run()