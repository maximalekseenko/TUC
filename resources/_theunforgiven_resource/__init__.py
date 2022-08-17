"""Resource of The Unforgiven Fraction Expansion."""


import assets as Assets



# add assets
Assets.ASSETS.append(__name__)



# add fraction
from .fraction import FractionTheunforgiven
Assets.FRACTIONS.append(FractionTheunforgiven)
