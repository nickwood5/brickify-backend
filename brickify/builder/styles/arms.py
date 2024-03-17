from brickify.builder.styles.style_utils import Style, StyleOptions, Component

class ArmStyle(Style):
    pass

long_sleeves = ArmStyle(
    raw_name="long_sleeves",
    prompt_name="Long Sleeves",
    components=[
        Component(
            name="primary"
        )
    ]
)

short_sleeves = ArmStyle(
    raw_name="short_sleeves",
    prompt_name="Short Sleeves",
    components=[
        Component(
            name="primary"
        )
    ]
)


sleeveless = ArmStyle(
    raw_name="sleeveless",
    prompt_name="Sleeveless",
    components=[],
)

arm_styles = [
    long_sleeves,
    short_sleeves,
    sleeveless,
]

arm_style_options = StyleOptions(arm_styles, name="arms")