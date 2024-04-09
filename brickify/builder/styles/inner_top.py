from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleName, StyleOverride, ComponentConfigurationMode,  StyleOverrideCondition, StyleOverrideEffect, StyleOverrideConditionEffect
from brickify.builder.colours import Colour

class InnerTopStyle(Style):
    def __init__(self, **kwargs):
        super().__init__(name=StyleName.INNER_TOP, **kwargs)


DEFAULT_OVERRIDE = StyleOverride(
    style_type=StyleName.OUTER_TOP,
    condition_effects=[
  
        StyleOverrideConditionEffect(
            condition=StyleOverrideCondition.IS,
            effect=StyleOverrideEffect.DELETE,
            value={"striped_shirt"}
        ),
        StyleOverrideConditionEffect(
            condition=StyleOverrideCondition.IS_NOT,
            effect=StyleOverrideEffect.ADD_SUFFIX,
            value={None},
            suffix_added="__inner_only"
        ),

    ]
)

blank_shirt = InnerTopStyle(
    source="blank_shirt",
    prompt_name="Blank Shirt",
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
        Component(
            name="arm_connector",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        )
    ]
)

striped_shirt = InnerTopStyle(
    source="striped_shirt",
    prompt_name="Striped Shirt with Equally Thin Stripes",
    components=[
        Component(
            name="stripe_1",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="stripe_2",
            default_colour=Colour.RED
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        )
    ],
    override=DEFAULT_OVERRIDE
)

thick_and_thin_striped_shirt = InnerTopStyle(
    source="thick_striped_shirt",
    prompt_name="Striped Shirt with Thick and Thin Stripes",
    components=[
        Component(
            name="thick_stripe",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="thin_stripe",
            default_colour=Colour.RED
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        )
    ],
    override=DEFAULT_OVERRIDE
    
)

thick_striped_shirt = InnerTopStyle(
    source="only_thick_striped_shirt",
    prompt_name="Striped Shirt with Equally Thick Stripes",
    components=[
        Component(
            name="stripe_1",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="stripe_2",
            default_colour=Colour.RED
        ),
        Component(
            name="skin",
            default_colour=Colour.LIGHT_BEIGE
        )
    ],
    override=DEFAULT_OVERRIDE
)

blank_shirt_with_tie = InnerTopStyle(
    source="blank_shirt_with_tie",
    prompt_name="Blank Shirt with Tie",
    components=[
        Component(
            name="primary",
            default_colour=Colour.WHITE
        ),
        Component(
            name="tie",
            default_colour=Colour.RED
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        ),
        Component(
            name="pin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        )
    ],
    override=DEFAULT_OVERRIDE
)

blank_shirt_with_bow_tie = InnerTopStyle(
    source="blank_shirt_with_bow_tie",
    prompt_name="Blank Shirt with Bow Tie",
    components=[
        Component(
            name="primary",
            default_colour=Colour.WHITE
        ),
        Component(
            name="bow_tie",
            default_colour=Colour.RED
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        )
    ],
    override=DEFAULT_OVERRIDE
)

polka_dot_shirt = InnerTopStyle(
    source="polka_dot_shirt",
    prompt_name="Polka Dot Shirt",
    components=[
        Component(
            name="primary",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="dots",
            default_colour=Colour.RED
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        ),
        Component(
            name="any",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        )
    ],
    #override=DEFAULT_OVERRIDE
)

button_up_shirt = InnerTopStyle(
    source="button_up_shirt",
    components=[
        Component(
            name="buttons",
            default_colour=Colour.BLACK
        ),
        Component(
            name="shirt",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        ),
        Component(
            name="any",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        )
    ],
    override=DEFAULT_OVERRIDE
)

striped_turtleneck = InnerTopStyle(
    source="striped_turtleneck",
    prompt_name="Striped Turtleneck with Equally Thin Stripes",
    components=[
        Component(
            name="stripe_1",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="stripe_2",
            default_colour=Colour.RED
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        )
    ],
    #override=DEFAULT_OVERRIDE
)

striped_crop_top = InnerTopStyle(
    source="striped_crop_top",
    prompt_name="Striped Crop Top with Equally Thin Stripes",
    components=[
        Component(
            name="stripe_1",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="stripe_2",
            default_colour=Colour.RED
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        )
    ],
    ##override=DEFAULT_OVERRIDE
)

blank_crop_top = InnerTopStyle(
    source="blank_crop_top",
    components=[
        Component(
            name="crop_top",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        )
    ],
    override=DEFAULT_OVERRIDE
)

pocket_blank_shirt = InnerTopStyle(
    source="pocket_blank_shirt",
    prompt_name="T-Shirt with Pocket",
    components=[
        Component(
            name="shirt",
            default_colour=Colour.WHITE
        ),
        Component(
            name="pocket",
            default_colour=Colour.BLACK
        ),
        Component(
            name="skin",
            configuration_mode=ComponentConfigurationMode.GLOBAL,
            default_colour=Colour.LIGHT_BEIGE
        ),
        Component(
            name="any",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.LIGHT_BLUISH_GRAY
        )
    ],
    #override=DEFAULT_OVERRIDE
)

not_visisble = InnerTopStyle(
    source=None,
    prompt_name="Not Visible"
)


inner_top_styles = [
    blank_shirt,
    button_up_shirt,
    striped_shirt,
    thick_and_thin_striped_shirt,
    blank_shirt_with_tie,
    blank_shirt_with_bow_tie,
    polka_dot_shirt,
    striped_turtleneck,
    blank_crop_top,
    striped_crop_top,
    pocket_blank_shirt,
    thick_striped_shirt,
    not_visisble
]

inner_top_style_options = StyleOptions(inner_top_styles, prefix="I")