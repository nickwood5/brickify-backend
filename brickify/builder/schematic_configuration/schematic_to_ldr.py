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

    for component_name in default_style.static_components.keys():
        default_style.static_components[component_name] = Colour.TRANS_LIGHT_BLUE

    
    style_name_to_default_configured_style[style_type] = ConfiguredStyle(style=default_style, components=components)



style_types = [
    arm_style_options,
    eyes_style_options,
    facial_hair_style_options,
    hair_style_options,
    inner_top_style_options,
    outer_top_style_options,
    legs_style_options,
]

for style_type in style_types:
    
    style_name = style_type.name

    #configured_styles_map.pop(style_name)
    
    folder_path = f"brickify/builder/schematic_source/{style_name}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for style in style_type.styles:
        style_variants = style.variants

        all_component_names = style.all_component_names

        
        
        for style_variant_name, style_variant in style_variants.items():
            print(style.static_components)
            style = deepcopy(style)
            configured_styles_map = deepcopy(style_name_to_default_configured_style)

            default_colours = style.default_colours

            print(style.prompt_name)
            components = {name: style.default_colours[name] for name in all_component_names}

            configured_styles_map[style.name] = ConfiguredStyle(style=style, components=components)

            configured_styles = apply_overrides(configured_styles_map)
            all_pieces = construct_final_model(configured_styles)

            res = "\n".join(all_pieces)

            with open(f"{folder_path}/{style_variant_name}.ldr", 'w') as file:
                # Write the content to the file
                file.write(res)
        

    