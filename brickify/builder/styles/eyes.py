from brickify.builder.styles.style_utils import Style, StyleOptions, Component
from brickify.builder.colours import Colour

class EyesStyle(Style):
    pass

glasses = EyesStyle(
    raw_name="glasses",
    components=[
        Component(name="primary")
    ]
)

blank = EyesStyle(
    raw_name="blank",
    components=[
        Component(name="eyes", default_colour=Colour.BLACK, configurable=False)
    ]
)

eyes_styles = [
    glasses,
    blank,
]

eyes_style_options = StyleOptions(eyes_styles, name="eyes")