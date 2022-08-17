from enum import Enum



class HEXDIRECTION(Enum):
    DIAR  = [+1, +1]
    UP    = [00, -1]
    LEFT  = [-1, 00]
    DIAL  = [-1, -1]
    DOWN  = [00, +1]
    RIGHT = [+1, 00]