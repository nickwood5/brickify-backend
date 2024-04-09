import json
from brickify.common.utils import get_json
from brickify.builder.styles import STYLE_NAME_TO
from brickify.builder.styles.style_utils import StyleName
from brickify.builder.colours import Colour

def convert_to_dict_with_placeholder(file_path):
    # Initialize an empty dictionary to store the parts grouped by color codes
    parts_dict = {}
    
    # Open the file
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into components
            parts = line.strip().split(' ')
            # Check if the line represents a part (starts with '1')
            if parts[0] == '1':
                # Extract the color code
                color_code = int(parts[1])
                # Replace the color code with '{}' in the line
                parts[1] = '{}'
                modified_line = ' '.join(parts)
                # Add the modified line to the list in the dictionary under the key of the color code
                if color_code not in parts_dict:
                    parts_dict[color_code] = []
                parts_dict[color_code].append(modified_line)
    
    return parts_dict


file = input("Enter file name: ")

schematic_type, schematic_name = file.split(".")

a = convert_to_dict_with_placeholder(f"brickify/builder/schematic_source/{schematic_type}/{schematic_name}.ldr")

base_name = schematic_name.split("__")[0]

existing_config = STYLE_NAME_TO[StyleName.from_string(schematic_type)][base_name].default_colours

from brickify.builder.colours import COLOUR_MAPPINGS

colour_code_to_name = {
    colour_code: name for name, colour_code in COLOUR_MAPPINGS.items()
}

res = dict()
for colour_code, components in a.items():
    if colour_code == Colour.TRANS_LIGHT_BLUE:
        continue

    colour_code = int(colour_code)
    colour_name = colour_code_to_name.get(colour_code)

    if colour_name is None:
        colour_name = colour_code

    component_name = input(f"Enter a name for colour: {colour_name}: ")

    res[component_name] = components

output_file_name = input("Enter output filename: ")

# Open a file for writing
with open(f'{output_file_name}.json', 'w') as file:
    # Use json.dump to write the dictionary to the file
    json.dump(res, file, indent=4)

print(res)