import primitives as Primitives



from field import Field
from entity import Entity
from fraction import Fraction



class Game:
    def __init__(self) -> None:
        self.FIELD = Field(1)
        self.FRACTIONS = list()


    def Set_Data(self, data:dict) -> None:
        pass


    def Get_Data(self) -> dict:
        pass


    def Generate_Data(self, **generation_parameters) -> None:
        '''Generates new data for this game.'''

        # activate all generation functions
        for func in Primitives.GENERATE_FUNCTIONS: func(self, **generation_parameters)


    def Add_Fraction(self, fraction:Fraction, **fraction_arguments):
        '''Creates and adds a new <fraction> with <fraction_arguments>.'''
        self.FRACTIONS.append(fraction(**fraction_arguments))


    def Add_Entity(self, entity:Entity, **entity_arguments):
        '''Creates and adds a new <entity> with <entity_arguments>'''