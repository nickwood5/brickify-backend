from brickify.builder.styles.style_utils import Style, StyleOptions

class InnerTopStyle(Style):
    pass


blank_shirt = InnerTopStyle(
    raw_name="blank_shirt",
    prompt_name="Blank Shirt",
    components=["primary"]
)

striped_shirt = InnerTopStyle(
    raw_name="striped_shirt",
    prompt_name="Striped Shirt with Equally Thin Stripes",
    components=["stripe_1", "stripe_2"]
)

thick_and_thin_striped_shirt = InnerTopStyle(
    raw_name="thick_striped_shirt",
    prompt_name="Striped Shirt with Thick and Thin Stripes",
    components=["thick_stripe", "thin_stripe"]
)

thick_striped_shirt = InnerTopStyle(
    raw_name="only_thick_striped_shirt",
    prompt_name="Striped Shirt with Equally Thick Stripes",
    components=["stripe_1", "stripe_2"]
)

blank_shirt_with_tie = InnerTopStyle(
    raw_name="blank_shirt_with_tie",
    prompt_name="Blank Shirt with Tie",
    components=["primary", "tie"]
)

blank_shirt_with_bow_tie = InnerTopStyle(
    raw_name="blank_shirt_with_bow_tie",
    prompt_name="Blank Shirt with Bow Tie",
    components=["primary", "bow_tie"]
)

polka_dot_shirt = InnerTopStyle(
    raw_name="polka_dot_shirt",
    prompt_name="Polka Dot Shirt",
    components=["primary", "dots"]
)

button_up_shirt = InnerTopStyle(
    raw_name="button_up_shirt",
    components=["buttons", "shirt"]
)

striped_turtleneck = InnerTopStyle(
    raw_name="striped_turtleneck",
    prompt_name="Striped Turtleneck with Equally Thin Stripes",
    components=["stripe_1", "stripe_2"]
)

striped_crop_top = InnerTopStyle(
    raw_name="striped_crop_top",
    prompt_name="Striped Crop Top with Equally Thin Stripes",
    components=["stripe_1", "stripe_2"]
)

blank_crop_top = InnerTopStyle(
    raw_name="blank_crop_top",
    components=["crop_top"]
)

pocket_blank_shirt = InnerTopStyle(
    raw_name="pocket_blank_shirt",
    prompt_name="T-Shirt with Pocket",
    components=["shirt", "pocket"]
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
    thick_striped_shirt
]

inner_top_style_options = StyleOptions(inner_top_styles, none_option="Not Visible", prefix="I", name="inner_top")