"""Resource with Base game assets."""


# imports
import assets as Assets
import primitives as Primitives



# save asset import fact
Assets.ASSETS.append(__name__)



# add generation function
from .function_generate import Generate
Primitives.GENERATE_FUNCTIONS.append(Generate)