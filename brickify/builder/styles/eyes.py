from brickify.builder.styles.style_utils import Style, StyleOptions

class EyesStyle(Style):
    pass

glasses = EyesStyle(
    raw_name="glasses",
    components=["primary"],
)

blank = EyesStyle(
    raw_name="blank",
    components=["primary", "eyes"],
)

eyes_styles = [
    glasses,
    blank,
]

eyes_style_options = StyleOptions(eyes_styles, name="eyes")