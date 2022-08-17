import pyglet



from field import Field
from primitives import *
from settings import *


class Field_Window(pyglet.window.Window):
    '''Pyglet Window-based window that shows given window.'''


    def __init__(self, field:Field, *args, **kwargs):
        self.field = field

        # super key arguments
        if "width" not in kwargs: kwargs["width"] = FIELD_WINDOW_WIDTH
        if "height" not in kwargs: kwargs["height"] = FIELD_WINDOW_HEIGHT
        if "caption" not in kwargs: kwargs["caption"] = None
        if "resizable" not in kwargs: kwargs["resizable"] = True
        if "style" not in kwargs: kwargs["style"] = None
        if "fullscreen" not in kwargs: kwargs["fullscreen"] = FIELD_WINDOW_FULLSCREEN
        if "visible" not in kwargs: kwargs["visible"] = True
        if "vsync" not in kwargs: kwargs["vsync"] = True
        if "file_drops" not in kwargs: kwargs["file_drops"] = False
        if "display" not in kwargs: kwargs["display"] = None
        if "screen" not in kwargs: kwargs["screen"] = None
        if "config" not in kwargs: kwargs["config"] = None
        if "context" not in kwargs: kwargs["context"] = None
        if "mode" not in kwargs: kwargs["mode"] = None

        # self parameters
        self.tile = pyglet.sprite.Sprite(HEXIMAGE)
        self.tile2 = pyglet.sprite.Sprite(HEXIMAGE2)
        self.tile3 = pyglet.sprite.Sprite(HEXIMAGE3)
        self._scale = FIELD_WINDOW_SCALE_DEFAULT
        self.camera_x = 0# self.field.size//2 * FIELD_TILE_W * 0.75
        self.camera_y = 0# self.field.size//2 * FIELD_TILE_H + (self.field.size // 2 - self.field.size//2) * FIELD_TILE_H / 2

        # super
        super().__init__(*args, **kwargs)


    @property
    def scale(self) -> float:
        return (-min(0, self._scale) + 1) / (max(0, self._scale) + 1)


    def Convert_Index_To_Pixel(self, index_x:int, index_y:int):

        # convert
        pixel_x = index_x * FIELD_TILE_W * 0.75
        pixel_y = index_y * FIELD_TILE_H + (self.field.center - index_x) * FIELD_TILE_H / 2
        
        # move by tile center
        pixel_x -= FIELD_TILE_W // 2
        pixel_y -= FIELD_TILE_H // 2

        # move by camera
        pixel_x -= self.camera_x
        pixel_y -= self.camera_y

        # scale
        pixel_x *= self.scale
        pixel_y *= self.scale

        # move by window center
        pixel_x += self.get_size()[0] // 2
        pixel_y += self.get_size()[1] // 2

        # return
        return pixel_x, pixel_y      


    def on_draw(self):
        self.clear()

        for x, y in self.field.Yield_Indexes():

            # check if coordinates are on field
            if not self.field.Is_Valid_Position(x, y): continue

            # convert index to pixels
            self.tile.scale = self.scale
            self.tile.x, self.tile.y = self.Convert_Index_To_Pixel(x, y)
            self.tile2.scale = self.scale
            self.tile2.x, self.tile2.y = self.Convert_Index_To_Pixel(x, y)
            self.tile3.scale = self.scale
            self.tile3.x, self.tile3.y = self.Convert_Index_To_Pixel(x, y)

            # render
            if (x, y) == (self.field.center, self.field.center): self.tile.draw()
            elif (x, y) in self.field.start_tiles: self.tile2.draw()
            elif (x, y) in self.field.border_tiles: self.tile3.draw()
            else: self.tile.draw()


    def oAn_draw(self):
        self.clear()
        for index_x in range(10):
            for index_y in range(10):
                pixel_x = index_x * FIELD_TILE_W
                pixel_y = index_y * FIELD_TILE_H
                
                # move by tile center
                # pixel_x -= FIELD_TILE_W // 2
                # pixel_y -= FIELD_TILE_H // 2

                # move by camera
                pixel_x -= self.camera_x
                pixel_y -= self.camera_y

                # scale
                pixel_x *= self.scale
                pixel_y *= self.scale

                # move by window center
                pixel_x += self.get_size()[0] / 2
                pixel_y += self.get_size()[1] / 2


                # SQUAREIMAGE.scale = self.scale
                # SQUAREIMAGE.x, SQUAREIMAGE.y = pixel_x, pixel_y
                # print(pixel_x, pixel_y)

                # render
                # SQUAREIMAGE.draw()
                pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                        ('v2i', (int(pixel_x), int(pixel_y))),
                        ('c3B', (255, 255, 255)))
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (self.get_size()[0] // 2, self.get_size()[1] // 2)),
                ('c3B', (255, 0, 0)))
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (self.get_size()[0] // 2 + int(FIELD_TILE_W*2), self.get_size()[1] // 2 + int(FIELD_TILE_H*2))),
                ('c3B', (0,0,255)))


        pyglet.text.Label(f"S {self.scale} {1/self.scale}",
                    font_size=10,
                    ).draw()
                

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        old_scale = self.scale

        self._scale += scroll_y / 10 * FIELD_WINDOW_SCALE_SPEED

        # validate scale
        if self._scale <= FIELD_WINDOW_SCALE_MIN: self._scale = FIELD_WINDOW_SCALE_MIN
        elif self._scale >= FIELD_WINDOW_SCALE_MAX: self._scale = FIELD_WINDOW_SCALE_MAX

        # move camera if needed
        if scroll_y:
        
            # get delta (distance from mouse to screen center)
            delta_x = x - self.get_size()[0] / 2
            delta_y = y - self.get_size()[1] / 2

            # multiply delta by formula
            delta_x *= 1 / old_scale - 1 / self.scale
            delta_y *= 1 / old_scale - 1 / self.scale

            # apply delta on camera
            self.camera_x += delta_x
            self.camera_y += delta_y

    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == FIELD_WINDOW_CAMERA_MOVE_BUTTON:
            self.camera_x -= dx / self.scale
            self.camera_y -= dy / self.scale
