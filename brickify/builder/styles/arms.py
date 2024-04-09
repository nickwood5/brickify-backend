from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleName, ComponentConfigurationMode
from brickify.builder.colours import Colour

class ArmStyle(Style):
    def __init__(self, **kwargs):
        super().__init__(name=StyleName.ARMS, **kwargs)

long_sleeves = ArmStyle(
    source="long_sleeves",
    prompt_name="Long Sleeves",
    components=[
        Component(
            name="primary",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        ),
    ]
)

short_sleeves = ArmStyle(
    source="short_sleeves",
    prompt_name="Short Sleeves",
    components=[
        Component(
            name="primary",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        ),
    ]
)


sleeveless = ArmStyle(
    source="sleeveless",
    prompt_name="Sleeveless",
    components=[Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        ),],
)

arm_styles = [
    long_sleeves,
    short_sleeves,
    sleeveless,
]

arm_style_options = StyleOptions(arm_styles)