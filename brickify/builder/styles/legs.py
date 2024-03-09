from brickify.builder.styles.style_utils import Style, StyleOptions
from brickify.builder.colours import Colour

class LegsStyle(Style):
    pass

long_pants = LegsStyle(
    raw_name="long_pants",
    components=["primary", "shoes"],
    default_colours={
        "shoes": Colour.BLACK
    }
)

short_pants = LegsStyle(
    raw_name="shorts",
    components=["primary", "shoes"],
    default_colours={
        "shoes": Colour.BLACK
    }
)

legs_styles = [
    long_pants,
    short_pants
]

legs_style_options = StyleOptions(
    styles=legs_styles,
    name="legs"
)