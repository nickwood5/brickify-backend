from brickify.builder.styles.arms import arm_style_options
from brickify.builder.styles.facial_hair import facial_hair_style_options
from brickify.builder.styles.inner_top import inner_top_style_options
from brickify.builder.styles.legs import legs_style_options
from brickify.builder.styles.outer_top import outer_top_style_options
from brickify.builder.styles.eyes import eyes_style_options
from brickify.builder.styles.hair import hair_style_options
from brickify.builder.styles.skin import skin_colour_options


STYLE_OPTIONS_LIST = [
    arm_style_options,
    facial_hair_style_options,
    inner_top_style_options,
    legs_style_options,
    outer_top_style_options,
    eyes_style_options,
    hair_style_options,
]

STYLE_NAME_TO = dict()

for style_options in STYLE_OPTIONS_LIST:
    STYLE_NAME_TO[style_options.name] = dict()

    for style in style_options.styles:
        STYLE_NAME_TO[style_options.name][style.source] = style
