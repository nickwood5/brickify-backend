from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleName, ComponentConfigurationMode
from brickify.builder.colours import Colour

class HairStyle(Style):
    def __init__(self, **kwargs):
        super().__init__(name=StyleName.HAIR, **kwargs)

very_short_curly = HairStyle(
    source="very_short_curly",
    components=[
        Component(
            name="hair",
            hidden_names={"hair_top"}
        ),
        Component(
            name="skull",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

bushy_hair_with_bangs__female = HairStyle(
    source="bushy_hair_with_bangs__female",
    components=[
        Component(
            name="hair",
            hidden_names={"hair_top"}
        ),
        Component(
            name="skull",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

bushy_hair_without_bangs__female = HairStyle(
    source="bushy_hair_without_bangs__female",
    components=[
        Component(
            name="hair",
            hidden_names={"hair_top"}
        ),
        Component(
            name="skull",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

marty_mcfly = HairStyle(
    source="marty_mcfly",
    prompt_name="Male short, wavy, tousled, 80s-style with pushed-back front (like Marty McFly)",
    components=[
        Component(
            name="hair",
            hidden_names={"hair_top"}
        ),
        Component(
            name="skull",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL
        ),
    ]
)

doc_brown = HairStyle(
    source="doc_brown",
    prompt_name="Male shoulder-length, wild and unkempt style with wiry, white hair standing out in various directions (example: Doc Brown)",
    components=[
        Component(
            name="hair",
            hidden_names={"hair_top"}
        ),
        Component(
            name="any",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL
        ),
    ]
)

elsa = HairStyle(
    source="elsa",
    prompt_name="Female sleek, platinum blonde braid that sweeps over one shoulder, with a long, side-swept bang framing her face (example: Elsa)",
    components=[
        Component(
            name="hair",
            hidden_names={"hair_top"}
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL
        ),
        Component(
            name="any",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

afro = HairStyle(
    source="afro",
    components=[
        Component(
            name="hair",
            hidden_names={"hair_top"}
        ),
        Component(
            name="any",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

bald = HairStyle(
    source="bald",
    components=[]
)

hair_styles = [
    very_short_curly,
    bushy_hair_with_bangs__female,
    bushy_hair_without_bangs__female,
    marty_mcfly,
    elsa,
    afro,
    bald,
    doc_brown
]

hair_style_options = StyleOptions(hair_styles)