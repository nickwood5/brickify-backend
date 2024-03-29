from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleName, ComponentConfigurationMode
from brickify.builder.colours import Colour

class EyesStyle(Style):
    def __init__(self, **kwargs):
        super().__init__(name=StyleName.EYES, **kwargs)

glasses = EyesStyle(
    source="glasses",
    components=[
        Component(name="primary"),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL
        ),
    ]
)

blank = EyesStyle(
    source="blank",
    components=[
        Component(name="eyes", default_colour=Colour.BLACK, configuration_mode=ComponentConfigurationMode.STATIC),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL
        ),
    ]
)

eyes_styles = [
    glasses,
    blank,
]

eyes_style_options = StyleOptions(eyes_styles)