from brickify.common.utils import AutoStringEnum
from brickify.builder.styles.style_utils import ColourStyle, StyleOptions
from enum import auto
from brickify.builder.colours import Colour


skin_colour_options = ColourStyle(
    description="skin", 
    colour_description_to_colour={
        "Fair": Colour.LIGHT_BEIGE,
        "Medium Brown": Colour.NOUGAT,
        "Dark Brown": Colour.REDDISH_BROWN,
    }
)
