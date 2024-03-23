from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleName
from brickify.builder.colours import Colour

class LegsStyle(Style):
    def __init__(self, **kwargs):
        super().__init__(name=StyleName.LEGS, **kwargs)

long_pants = LegsStyle(
    source="long_pants",
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
    source="shorts",
    components = ["primary", "shoes"]
    
)

legs_styles = [
    long_pants,
    short_pants
]

legs_style_options = StyleOptions(
    styles=legs_styles,
)