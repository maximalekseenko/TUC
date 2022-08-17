import pyglet
import os

GENERATE_FUNCTIONS = []



# field
# FIELD_TILE_W = 120
# FIELD_TILE_H = 100
FIELD_TILE_W = 130 / 4
FIELD_TILE_H = 110 / 4
 
HEXIMAGE = pyglet.image.load(os.path.join(os.getcwd(),"resources","_base_resource","hex.png"))
HEXIMAGE2 = pyglet.image.load(os.path.join(os.getcwd(),"resources","_base_resource","hex2.png"))
HEXIMAGE3 = pyglet.image.load(os.path.join(os.getcwd(),"resources","_base_resource","hex3.png"))
SQUAREIMAGE = pyglet.image.load(os.path.join(os.getcwd(),"resources","_base_resource","square.jpg"))
SQUAREIMAGE = pyglet.sprite.Sprite(SQUAREIMAGE)