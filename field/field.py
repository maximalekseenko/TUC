from .enums import HEXDIRECTION



import debug as Debug
from primitives import *



class Field:
    def __init__(self, size:int) -> None:
        # validate parameters
        if size % 2 == 0: Debug.Raise("Field.__init__()", ValueError("Even Field size"))

        #
        self.loop = True
        self.size = size

        # constants
        self.CENTER = 0
        self.START = -self.size//2 + 1
        self.END = self.size//2 + 1

    
    def Yield_Indexes(self):
        '''Yields all valid indexes.'''
        for y in range(self.START, self.END):
            for x in range(self.START, self.END):
                if self.Is_Valid_Position(x, y):
                    yield x, y


    def Is_Valid_Position(self, x:int, y:int) -> bool:
        '''Checks if position is on field.'''

        if self.END + x - y <= self.CENTER: return False
        if self.END - x + y <= self.CENTER: return False
        if x < self.START or x >= self.END: return False
        if y < self.START or y >= self.END: return False
        return True


    def Get_In_Direction(self, x:int, y:int, direction:HEXDIRECTION) -> tuple:
        '''Get next hex in `direction` from hex[`x`, `y`]'''

        # get new 
        new_x = x + direction.value[0]
        new_y = y + direction.value[1]

        if self.Is_Valid_Position(new_x, new_y): return (new_x, new_y)
        elif self.loop: 
            if False:pass
            elif direction == HEXDIRECTION.DIAR: new_x, new_y = self.size   - new_y, self.size   - new_x
            elif direction == HEXDIRECTION.DIAL: new_x, new_y = self.size-2 - new_y, self.size-2 - new_x
            elif direction == HEXDIRECTION.RIGHT:new_x = max(new_y - self.size // 2, 0)
            elif direction == HEXDIRECTION.DOWN: new_y = max(new_x - self.size // 2, 0)
            elif direction == HEXDIRECTION.LEFT: new_x = min(new_y + self.size // 2, self.size-1)
            elif direction == HEXDIRECTION.UP:   new_y = min(new_x + self.size // 2, self.size-1)

            return (new_x, new_y)
        else: return


    def Get_Heighbours(self, x:int, y:int) -> list:
        '''Get all six neighbours of hex[`x`, `y`].'''

        return [self.Get_In_Direction(x, y, direction) for direction in HEXDIRECTION]


    def __repr__(self) ->str:
        ret = str()
        for y in range(self.size):
            for x in range(self.size):
                ret += '*' if self.Is_Valid_Position(x,y) else ' '
            ret += '\n'
        return ret