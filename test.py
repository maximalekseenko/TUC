print("REPENT, YOU, SCUM")
print()



import resources



# game
from game import Game

game = Game()
game.Generate_Data(
    tile_size = 3,
    game_size = 1
)

        # if "width" not in kwargs: kwargs["width"] = None
        # if "height" not in kwargs: kwargs["height"] = None
        # if "caption" not in kwargs: kwargs["caption"] = None
        # if "resizable" not in kwargs: kwargs["resizable"] = False
        # if "style" not in kwargs: kwargs["style"] = None
        # if "fullscreen" not in kwargs: kwargs["fullscreen"] = False
        # if "visible" not in kwargs: kwargs["visible"] = True
        # if "vsync" not in kwargs: kwargs["vsync"] = True
        # if "file_drops" not in kwargs: kwargs["file_drops"] = False
        # if "display" not in kwargs: kwargs["display"] = None
        # if "screen" not in kwargs: kwargs["screen"] = None
        # if "config" not in kwargs: kwargs["config"] = None
        # if "context" not in kwargs: kwargs["context"] = None
        # if "mode" not in kwargs: kwargs["mode"] = None


#
is_running = True



# pyglet
import pyglet

from field.window import Field_Window
window = Field_Window(game.FIELD)


# ret = str()
# row = 0
# for x, y in game.FIELD.Yield_Indexes():
#     if row != y:
#         row = y
#         ret += '\n'
#         ret += ' ' * (x+game.FIELD.size//2)

#     if False: pass
#     elif (x, y) == (game.FIELD.center, game.FIELD.center): ret += 'C'
#     elif (x, y) in game.FIELD.start_tiles: ret += 'S'
#     elif (x, y) in game.FIELD.border_tiles: ret += 'A'
#     else: ret += '*'
# print(ret)
from primitives import *

window.camera_x = 0
window.camera_y = 0

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.A: window.on_mouse_scroll(
        window.get_size()[0]/2+FIELD_TILE_W*2,
        window.get_size()[1]/2+FIELD_TILE_H*2, 
        0, 1)
    if symbol == pyglet.window.key.D: window.on_mouse_scroll(
            window.get_size()[0]/2+FIELD_TILE_W*2,
            window.get_size()[1]/2+FIELD_TILE_H*2, 
            0, -1)
    # window.on_mouse_scroll(
    #     window.get_size()[0]/2+FIELD_TILE_W*2,
    #     window.get_size()[1]/2+FIELD_TILE_H*2, 
        # 0, 0)

pyglet.app.run()
