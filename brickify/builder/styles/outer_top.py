from brickify.common.utils import AutoStringEnum
from brickify.builder.colours import Colour
from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleType
from brickify.builder.styles.inner_top import inner_top_style_options
from enum import auto

class StyleDependencyType(AutoStringEnum):
    REQUIRED = auto()
    NOT_REQUIRED = auto()
    OPTIONAL = auto()

class OuterTopStyle(Style):
    def __init__(self, inner_dependency_type: StyleDependencyType, **kwargs) -> None:
        super().__init__(**kwargs)
        self.inner_dependency_type = inner_dependency_type


closed_blazer = OuterTopStyle(
    raw_name="closed_blazer",
    prompt_name="Closed Blazer",
    inner_dependency_type=StyleDependencyType.REQUIRED,
    components=[
        "primary", Component(
            name="arm_connector",
            configurable=False,
            default_colour=Colour.BLACK
        )
    ]
)

open_blazer = OuterTopStyle(
    raw_name="open_blazer",
    prompt_name="Open Blazer",
    inner_dependency_type=StyleDependencyType.REQUIRED,
    components=[
        "blazer", Component(
            name="arm_connector",
            configurable=False,
            default_colour=Colour.BLACK
        )
    ]
)

sweater = OuterTopStyle(
    raw_name="sweater",
    prompt_name="Sweater",
    inner_dependency_type=StyleDependencyType.NOT_REQUIRED,
    components=[
        "primary"
    ]
)

striped_sweater = OuterTopStyle(
    raw_name="striped_shirt",
    prompt_name="Striped Sweater",
    inner_dependency_type=StyleDependencyType.NOT_REQUIRED,
    components=[
        "stripe_1", "stripe_2"
    ]
)

sweater_with_shirt_showing = OuterTopStyle(
    raw_name="sweater_with_shirt_showing",
    prompt_name="Sweater with Shirt Showing",
    inner_dependency_type=StyleDependencyType.NOT_REQUIRED,
    components=[
        "primary", "shirt"
    ]
)

zip_hoodie = OuterTopStyle(
    raw_name="zip_hoodie",
    prompt_name="Zip Hoodie",
    inner_dependency_type=StyleDependencyType.OPTIONAL,
    components=[
        "primary"
    ]
)

puffy_jacket = OuterTopStyle(
    raw_name="puffy_jacket",
    prompt_name="Puffy Jacket",
    inner_dependency_type=StyleDependencyType.OPTIONAL,
    components=[
        "primary", "zipper"
    ]
)

closed_cardigan = OuterTopStyle(
    raw_name="closed_cardigan",
    inner_dependency_type=StyleDependencyType.REQUIRED,
    components=["cardigan"]
)

open_cardigan = OuterTopStyle(
    raw_name="open_cardigan",
    inner_dependency_type=StyleDependencyType.REQUIRED,
    components=["cardigan"]
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
]

outer_top_style_options = StyleOptions(outer_top_styles, none_option="None", prefix="O", name=StyleType.OUTER_TOP)