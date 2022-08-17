import pygame.image
class Entity:
    """"""


    NAME:str = "Basic entity"
    '''Human readable name of this entity type.'''

    ID:str = "ENTITY"
    '''Id of this entity type.'''

    TAGS:list[str] = []
    '''Tags of this entity type.'''


    def __init__(self) -> None:
        self.name = Entity.NAME
        self.id   = Entity.ID
        self.tags = Entity.TAGS