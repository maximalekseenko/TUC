from .enums import ENTITY_TAG
from .entity import Entity


class Planet_Entity(Entity):
    NAME = "Basic Planet"
    ID = "PLANET"
    TAGS = [ENTITY_TAG.PLANET]