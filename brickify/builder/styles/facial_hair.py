from brickify.builder.styles.style_utils import Style, StyleOptions, Component, StyleType

class FacialHairStyle(Style):
    pass


blank = FacialHairStyle(
    source="none",
    components=[]
)

only_mustache = FacialHairStyle(
    source="only_mustache",
    components=[
        Component(name="mustache")
    ]
)

archer_beard = FacialHairStyle(
    source="archer_beard",
    components=[
        Component(name="beard")
    ]
)

short_beard = FacialHairStyle(
    source="short_beard",
    components=[
        Component(name="beard")
    ]
)

medium_beard = FacialHairStyle(
    source="medium_beard",
    components=[
        Component(name="beard")
    ]
)

long_beard = FacialHairStyle(
    source="long_beard",
    components=[
        Component(name="beard")
    ]
)

facial_hair_styles = [
    blank,
    only_mustache,
    archer_beard,
    short_beard,
    medium_beard,
    long_beard
]

facial_hair_style_options = StyleOptions(facial_hair_styles, name=StyleType.FACIAL_HAIR)