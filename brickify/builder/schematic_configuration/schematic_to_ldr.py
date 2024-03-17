from brickify.builder.styles import arm_style_options, eyes_style_options, facial_hair_style_options, hair_style_options, inner_top_style_options, outer_top_style_options, legs_style_options
from brickify.builder.styles import arms, eyes, facial_hair, hair, inner_top, outer_top, legs
from brickify.builder.builder import get_component_string, load_json_from_folders
from brickify.builder.colours import Colour
import os 

json_files_content = load_json_from_folders("brickify/builder/schematics")

print(json_files_content)

style_type_to_default = {
    arm_style_options.name: arms.long_sleeves,
    eyes_style_options.name: eyes.blank,
    facial_hair_style_options.name: facial_hair.blank,
    hair_style_options.name: hair.marty_mcfly,
    inner_top_style_options.name: inner_top.button_up_shirt,
    outer_top_style_options.name: outer_top.open_blazer,
    legs_style_options.name: legs.long_pants,    
}

style_type_name_to_default_string = dict()


for style_type, default_style in style_type_to_default.items():
    components = default_style.components

    colour_mapping = {"skin": Colour.BLACK}
    for comp in components:
        print(comp.name)
        colour_mapping[comp.name] = Colour.BLACK

    raw_name = default_style.raw_name

    path = style_type
    print(style_type)
    if style_type == inner_top_style_options.name:
        raw_name += "__inner_only"
        path = "torso"

    elif style_type == outer_top_style_options.name:
        path = "torso"

    
    print(colour_mapping)
    component_string = get_component_string(colour_mapping, path, raw_name)

    print(component_string)

    style_type_name_to_default_string[style_type] = component_string


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

    folder_path = f"brickify/builder/schematic_source/{style_name}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    base_style_list = []

    for default_style_type, default_string in style_type_name_to_default_string.items():
        if default_style_type == style_name:
            continue
        
        base_style_list += default_string

    print(base_style_list)
    base_style_str = "\n".join(base_style_list)
    
    print(style_type.styles)
    for style in style_type.styles:
        if style is None:
            continue
        print(style.raw_name)
        with open(f"{folder_path}/{style.raw_name}.ldr", 'w') as file:
            # Write the content to the file
            file.write(base_style_str)