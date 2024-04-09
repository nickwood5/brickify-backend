from brickify.common.utils import AutoStringEnum
from brickify.builder.colours import Colour
from brickify.builder.styles.style_utils import StyleOverrideEffect, Style, StyleOptions, Component, StyleName, StyleOverride, StyleOverrideCondition, StyleOverrideConditionEffect, ComponentConfigurationMode
from brickify.builder.styles.inner_top import inner_top_style_options
from enum import auto

class StyleDependencyType(AutoStringEnum):
    REQUIRED = auto()
    NOT_REQUIRED = auto()
    OPTIONAL = auto()

class OuterTopStyle(Style):
    def __init__(self, inner_dependency_type: StyleDependencyType, **kwargs) -> None:
        super().__init__(name=StyleName.OUTER_TOP, **kwargs)###
        self.inner_dependency_type = inner_dependency_type

print("g")
OUTER_OVERRIDE = StyleOverride(
    style_type=StyleName.INNER_TOP,
    condition_effects=[
        StyleOverrideConditionEffect(
            condition=StyleOverrideCondition.IS_NOT,
            effect=StyleOverrideEffect.ADD_SUFFIX,
            value=set([None]),
            suffix_added="__outer_only"
        )
    ]
)

closed_blazer = OuterTopStyle(
    source="closed_blazer",
    prompt_name="Closed Blazer",
    inner_dependency_type=StyleDependencyType.REQUIRED,
    components=[
        Component(name="primary", default_colour=Colour.DARK_BLUE),
        Component(
            name="arm_connector",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.BLACK
        )
    ],
)

open_blazer = OuterTopStyle(
    source="open_blazer",
    prompt_name="Open Blazer",
    inner_dependency_type=StyleDependencyType.REQUIRED,
    components=[
        Component(
            name="blazer",
            default_colour=Colour.DARK_BLUE
        ),
        Component(
            name="any",
            configuration_mode=ComponentConfigurationMode.STATIC,
            default_colour=Colour.BLACK
        )
    ],
)##

sweater = OuterTopStyle(
    source="sweater",
    prompt_name="Sweater",
    inner_dependency_type=StyleDependencyType.NOT_REQUIRED,
    components=[
        Component(name="primary", default_colour=Colour.DARK_BLUE)
    ],
    #override=OUTER_OVERRIDE
)

striped_sweater = OuterTopStyle(
    source="striped_shirt",
    prompt_name="Striped Sweater",
    inner_dependency_type=StyleDependencyType.NOT_REQUIRED,
    components=[
        Component(
            name="stripe_1",
            default_colour=Colour.DARK_BLUE,
        ),
        Component(
            name="stripe_2",
            default_colour=Colour.RED,
        )
    ]
)



sweater_with_shirt_showing = OuterTopStyle(
    source="sweater_with_shirt_showing",
    prompt_name="Sweater with Shirt Showing",
    inner_dependency_type=StyleDependencyType.NOT_REQUIRED,
    components=[
        Component(
            name="primary",
            default_colour=Colour.DARK_BLUE,
        ),
        Component(
            name="shirt",
            default_colour=Colour.RED,
        )
    ]
)

zip_hoodie = OuterTopStyle(
    source="zip_hoodie",
    prompt_name="Zip Hoodie",
    inner_dependency_type=StyleDependencyType.OPTIONAL,
    components=[
        Component(
            name="primary",
            default_colour=Colour.DARK_BLUE,
        ),
    ],
    override=OUTER_OVERRIDE
)

puffy_jacket = OuterTopStyle(
    source="puffy_jacket",
    prompt_name="Puffy Jacket",
    inner_dependency_type=StyleDependencyType.OPTIONAL,
    components=[
        Component(
            name="primary",
            default_colour=Colour.DARK_BLUE,
        ),
        Component(
            name="zipper",
            default_colour=Colour.BLACK,
        ), 
    ],
    override=OUTER_OVERRIDE
)

closed_cardigan = OuterTopStyle(
    source="closed_cardigan",
    inner_dependency_type=StyleDependencyType.NOT_REQUIRED,
    components=[Component(
        name="cardigan", default_colour=Colour.DARK_BLUE
    )]
    #override=OUTER_OVERRIDE
)

open_cardigan = OuterTopStyle(
    source="open_cardigan",
    inner_dependency_type=StyleDependencyType.REQUIRED,
    components=[Component(
        name="cardigan", default_colour=Colour.DARK_BLUE
    )]
    #override=OUTER_OVERRIDE
)

none = OuterTopStyle(
    source=None,
    prompt_name="None",
    inner_dependency_type=StyleDependencyType.REQUIRED,
)



outer_top_styles = [
    closed_blazer,
    open_blazer,
    sweater,
    sweater_with_shirt_showing,
    zip_hoodie,
    puffy_jacket,
    closed_cardigan,
    open_cardigan,
    striped_sweater,
    none,
]

outer_top_style_options = StyleOptions(outer_top_styles, prefix="O")