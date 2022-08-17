from game import Game
from field import Field



from .fraction import FractionNone



def Generate(game:Game, **parameters) -> None:
    '''Initial base generate function for the game.'''

    _Gen_Field(game, **parameters)

    game.Add_Fraction(FractionNone)



def _Gen_Field(game:Game, **parameters):

    # get parameters
    tile_size = parameters["tile_size"]
    game_size = parameters["game_size"]
    field_size = tile_size + tile_size * game_size - game_size

    # create field
    game.FIELD = Field(field_size)

    # get tiles
    game.FIELD.start_tiles = []
    game.FIELD.border_tiles = []

    # loop through tiles
    for x, y in game.FIELD.Yield_Indexes():
        
        # is tile center?
        if y % (tile_size // 2) != 0: continue
        if (x - (game.FIELD.center - y + tile_size // 2) % (tile_size + tile_size // 2 - 1)) % (tile_size // 2 * 3) != 0: continue
        
        # is border tile?
        if   not game.FIELD.Is_Valid_Position(x+1,y): game.FIELD.border_tiles.append((x, y))
        elif not game.FIELD.Is_Valid_Position(x-1,y): game.FIELD.border_tiles.append((x, y))
        elif not game.FIELD.Is_Valid_Position(x,y+1): game.FIELD.border_tiles.append((x, y))
        elif not game.FIELD.Is_Valid_Position(x,y-1): game.FIELD.border_tiles.append((x, y))

        # else start tile
        else: game.FIELD.start_tiles.append((x, y))