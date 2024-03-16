from brickify.builder.styles.style_utils import Style, StyleOptions, Component
from brickify.builder.colours import Colour

class HairStyle(Style):
    pass

very_short_curly = HairStyle(
    raw_name="very_short_curly",
    components=[
        Component(
            name="hair",
            hidden_names="hair_top"
        ),
        Component(
            name="skull",
            configurable=False,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

bushy_hair_with_bangs__female = HairStyle(
    raw_name="bushy_hair_with_bangs__female",
    components=[
        Component(
            name="hair",
            hidden_names="hair_top"
        ),
        Component(
            name="skull",
            configurable=False,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

bushy_hair_without_bangs__female = HairStyle(
    raw_name="bushy_hair_without_bangs__female",
    components=[
        Component(
            name="hair",
            hidden_names="hair_top"
        ),
        Component(
            name="skull",
            configurable=False,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

marty_mcfly = HairStyle(
    raw_name="marty_mcfly",
    prompt_name="Male short, wavy, tousled, 80s-style with pushed-back front (like Marty McFly)",
    components=[
        Component(
            name="hair",
            hidden_names="hair_top"
        ),
        Component(
            name="skull",
            configurable=False,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

marty_mcfly = HairStyle(
    raw_name="doc_brown",
    prompt_name="Male shoulder-length, wild and unkempt style with wiry, white hair standing out in various directions (example: Doc Brown)",
    components=[
        Component(
            name="hair",
            hidden_names="hair_top"
        ),
        Component(
            name="skull",
            configurable=False,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

elsa = HairStyle(
    raw_name="elsa",
    prompt_name="Female sleek, platinum blonde braid that sweeps over one shoulder, with a long, side-swept bang framing her face (example: Elsa)",
    components=[
        Component(
            name="hair",
            hidden_names="hair_top"
        ),
        Component(
            name="skull",
            configurable=False,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

afro = HairStyle(
    raw_name="afro",
    components=[
        Component(
            name="hair",
            hidden_names="hair_top"
        ),
        Component(
            name="skull",
            configurable=False,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        ),
    ]
)

bald = HairStyle(
    raw_name="bald",
    components=[]
)

hair_styles = [
    very_short_curly,
    bushy_hair_with_bangs__female,
    bushy_hair_without_bangs__female,
    marty_mcfly,
    elsa,
    afro,
    bald
]

hair_style_options = StyleOptions(hair_styles, name="hair")