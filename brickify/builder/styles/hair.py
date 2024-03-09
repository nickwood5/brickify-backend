from brickify.builder.styles.style_utils import Style, StyleOptions

class HairStyle(Style):
    pass

very_short_curly = HairStyle(
    raw_name="very_short_curly",
    components=["hair"],
)

bushy_hair_with_bangs__female = HairStyle(
    raw_name="bushy_hair_with_bangs__female",
    components=["hair"],
)

bushy_hair_without_bangs__female = HairStyle(
    raw_name="bushy_hair_without_bangs__female",
    components=["hair"],
)

marty_mcfly = HairStyle(
    raw_name="bushy_hair_without_bangs__female",
    prompt_name="Male short, wavy, tousled, 80s-style with pushed-back front (like Marty McFly)",
    components=["hair"],
)

marty_mcfly = HairStyle(
    raw_name="doc_brown",
    prompt_name="Male shoulder-length, wild and unkempt style with wiry, white hair standing out in various directions (example: Doc Brown)",
    components=["hair"],
)

elsa = HairStyle(
    raw_name="elsa",
    prompt_name="Female sleek, platinum blonde braid that sweeps over one shoulder, with a long, side-swept bang framing her face (example: Elsa)",
    components=["hair"],
)

afro = HairStyle(
    raw_name="afro",
    components=["hair"],
)

bald = HairStyle(
    raw_name="bald",
    components=["hair"],
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