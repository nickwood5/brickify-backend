from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleType
from brickify.builder.colours import Colour

class LegsStyle(Style):
    pass

long_pants = LegsStyle(
    raw_name="long_pants",
    components=[
        Component(
            name="primary"
        ),
        Component(
            name="shoes"
        )
    ]
)

short_pants = LegsStyle(
    raw_name="shorts",
    components = ["primary", "shoes"]
    
)

legs_styles = [
    long_pants,
    short_pants
]

legs_style_options = StyleOptions(
    styles=legs_styles,
    name=StyleType.LEGS
)