from brickify.builder.styles import arm_style_options, eyes_style_options, facial_hair_style_options, hair_style_options, inner_top_style_options, outer_top_style_options, legs_style_options
from brickify.builder.styles import arms, eyes, facial_hair, hair, inner_top, outer_top, legs
from brickify.builder.builder import get_component_string, load_json_from_folders
from brickify.builder.colours import Colour
from brickify.builder.builder import apply_overrides, construct_final_model
from brickify.builder.styles.style_utils import ConfiguredStyle, Style
from copy import deepcopy
import os

json_files_content = load_json_from_folders("brickify/builder/schematics")

print(json_files_content)

style_type_to_default: dict[str, Style] = {
    arm_style_options.name: arms.long_sleeves,
    eyes_style_options.name: eyes.blank,
    facial_hair_style_options.name: facial_hair.blank,
    hair_style_options.name: hair.marty_mcfly,
    inner_top_style_options.name: inner_top.button_up_shirt,
    outer_top_style_options.name: outer_top.open_blazer,
    legs_style_options.name: legs.long_pants,    
}

style_name_to_default_configured_style = dict()

for style_type, default_style in style_type_to_default.items():
    all_component_names = default_style.all_component_names

    components = {
        name: Colour.TRANS_LIGHT_BLUE for name in all_component_names
    }

    for component_name in all_component_names:
        default_style.static_components[component_name] = Colour.TRANS_LIGHT_BLUE

    
    style_name_to_default_configured_style[style_type] = ConfiguredStyle(style=default_style, components=components)


style_type_name_to_default_string = dict()


for style_type, default_style in style_type_to_default.items():

    style_type_name_to_default_string[style_type] = default_style.get_as_single_colour(Colour.BLACK)


style_types = [
    arm_style_options,
    eyes_style_options,
    facial_hair_style_options,
    hair_style_options,
    inner_top_style_options,
    outer_top_style_options,
    legs_style_options,
]

for style, configured_style in style_name_to_default_configured_style.items():
    print(configured_style.style.source)


configured_styles = apply_overrides(style_name_to_default_configured_style)
print('bre')
for s in configured_styles:
    print(s.style.prompt_name)
    print(s.style.source)
    print(s.source)
all_pieces = construct_final_model(configured_styles)

res = "\n".join(all_pieces)

with open(f"test.ldr", 'w') as file:
    # Write the content to the file
    file.write(res)


    