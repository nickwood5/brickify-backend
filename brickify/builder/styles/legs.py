from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleName, ComponentConfigurationMode
from brickify.builder.colours import Colour

class LegsStyle(Style):
    def __init__(self, **kwargs):
        super().__init__(name=StyleName.LEGS, **kwargs)

long_pants = LegsStyle(
    source="long_pants",
    components=[
        Component(
            name="primary",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="shoes",
            default_colour=Colour.RED
        ),
        
    ]
)

short_pants = LegsStyle(
    source="shorts",
    components = [
        Component(
            name="primary",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="shoes",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="skin",
            default_colour=Colour.LIGHT_BEIGE,
            configuration_mode=ComponentConfigurationMode.GLOBAL
        ),
    ]
    
)

legs_styles = [
    long_pants,
    short_pants
]

legs_style_options = StyleOptions(
    styles=legs_styles,
)