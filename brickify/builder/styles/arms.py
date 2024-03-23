from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleName

class ArmStyle(Style):
    def __init__(self, **kwargs):
        super().__init__(name=StyleName.ARMS, **kwargs)

long_sleeves = ArmStyle(
    source="long_sleeves",
    prompt_name="Long Sleeves",
    components=[
        Component(
            name="primary"
        )
    ]
)

short_sleeves = ArmStyle(
    source="short_sleeves",
    prompt_name="Short Sleeves",
    components=[
        Component(
            name="primary"
        )
    ]
)


sleeveless = ArmStyle(
    source="sleeveless",
    prompt_name="Sleeveless",
    components=[],
)

arm_styles = [
    long_sleeves,
    short_sleeves,
    sleeveless,
]

arm_style_options = StyleOptions(arm_styles)