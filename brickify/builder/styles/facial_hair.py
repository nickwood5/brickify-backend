from brickify.builder.styles.style_utils import Style, StyleOptions

class FacialHairStyle(Style):
    pass


blank = FacialHairStyle(
    raw_name="none",
    components=[]
)

only_mustache = FacialHairStyle(
    raw_name="only_mustache",
    components=["mustache"]
)

archer_beard = FacialHairStyle(
    raw_name="archer_beard",
    components=["beard"]
)

short_beard = FacialHairStyle(
    raw_name="short_beard",
    components=["beard"]
)

medium_beard = FacialHairStyle(
    raw_name="medium_beard",
    components=["beard"]
)

long_beard = FacialHairStyle(
    raw_name="long_beard",
    components=["beard"]
)

facial_hair_styles = [
    blank,
    only_mustache,
    archer_beard,
    short_beard,
    medium_beard,
    long_beard
]

facial_hair_style_options = StyleOptions(facial_hair_styles, name="facial_hair")