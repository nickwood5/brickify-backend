from typing import Optional
from django.core.files.uploadedfile import UploadedFile
from brickify.common.utils import AutoStringEnum
from enum import auto
import concurrent.futures
from brickify.builder.styles import legs_style_options, facial_hair_style_options, arm_style_options, eyes_style_options, hair_style_options
from brickify.builder.test import do
import os
import base64
import json
from brickify.builder.colours import Colour

class BuildingMode(AutoStringEnum):
    FROM_IMAGE_FILE = auto()
    FROM_IMAGE_URL = auto()

import os
from collections import defaultdict

def load_json_from_folders(main_folder):
    # Iterate through all items in the main folder
    res = defaultdict(dict)
    for item in os.listdir(main_folder):
        item_path = os.path.join(main_folder, item)
        # Check if the item is a folder
        if os.path.isdir(item_path):
            # Iterate through all items in the subfolder
            for sub_item in os.listdir(item_path):
                sub_item_path = os.path.join(item_path, sub_item)
                # Check if the sub item is a file
                if os.path.isfile(sub_item_path):
                    with open(sub_item_path, 'r') as file:
                        data = json.load(file)
                    res[item][os.path.basename(sub_item_path)[:-5]] = data
    return res


# Replace 'path_to_main_folder' with the path to your main folder
# print_contents_of_files_in_subfolders('path

json_files_content = load_json_from_folders("brickify/builder/schematics")
print(f"The content is {json_files_content}")

def get_component_string(colour_mapping, component_type, name):
    print(json_files_content.keys())
    print(json_files_content[component_type].keys())
    lookup = json_files_content[component_type][name]

    all_pieces = []
    #print(lookup)
    #print(colour_mapping)
    for colour, pieces in lookup.items():
        #print(colour, pieces)
        for piece in pieces:
            colour_code = Colour.LIGHT_BLUISH_GRAY if colour == "any" else colour_mapping[colour]
            all_pieces.append(piece.format(colour_code))

    return all_pieces
base = """
0 Untitled Model
0 Name:  Untitled Model
0 Author:
0 CustomBrick
0 NumOfBricks:  85

"""

def encode_image(uploaded_file: UploadedFile):
    """
    This function takes a Django UploadedFile object,
    reads its content, and encodes it to a base64 string
    with the appropriate data URL prefix using the file's MIME type.
    """
    # Read the content of the uploaded file
    file_content = uploaded_file.read()
    # Get MIME type from the UploadedFile object
    mime_type = uploaded_file.content_type
    if not mime_type.startswith('image/'):
        raise ValueError("Unsupported file type")
    # Encode the file content to base64
    base64_encoded = base64.b64encode(file_content).decode('utf-8')
    return f"data:{mime_type};base64,{base64_encoded}"


class ImageSource:
    def __init__(self, image_url: Optional[str]=None, image_file: Optional[UploadedFile]=None) -> None:
        if image_url is None and image_file is None:
            raise Exception("One of image_url or image_file must be provided")
        
        if image_url is not None and image_file is not None:
            raise Exception("Only one of image_url or image_file should be provided")
        
        if image_url is not None:
            self.image_url = image_url
            self.building_mode = BuildingMode.FROM_IMAGE_URL
        else:
            self.image_file = image_file
            self.building_mode = BuildingMode.FROM_IMAGE_FILE

    def get_image_url(self):
        if self.building_mode == BuildingMode.FROM_IMAGE_FILE:
            base64_image = encode_image(self.image_file)
            print(base64_image)
            return base64_image
    
        elif BuildingMode.FROM_IMAGE_URL:
            return self.image_url


class Builder:
    def __init__(self, image_source: ImageSource) -> None:
        self.image_url = image_source.get_image_url()

        self.skin_colour = Colour.LIGHT_BEIGE

    def resolve_legs(self):
        name, colours = legs_style_options.get_configured_style_config(self.image_url)

        colours["skin"] = self.skin_colour

        call = (colours, "legs", name)

        return [call]
    
    def resolve_facial_hair(self):
        print("Start resolving facial hair")
        name, colours = facial_hair_style_options.get_configured_style_config(self.image_url)
        if name is None:
            return []

        colours["skin"] = self.skin_colour
        call = (colours, "lower_face", name)
        #print(call)
        print("Finish resolving facial hair")
        return [call]
    
    def resolve_arms(self):
        print("Start resolving arms")
        name, colours = arm_style_options.get_configured_style_config(self.image_url)

        colours["skin"] = self.skin_colour

        call = (colours, "arms", name)
        print("Finish resolving arms")
        return [call]




    def resolve_torso(self):
        
        print(f"Start resolving torso")

        inner_top_name, inner_top_colours, outer_top_name, outer_top_colours = do(self.image_url)

        configs = []
        if inner_top_colours is not None:
            inner_top_colours["arm_connector"] = Colour.BLACK
            inner_top_colours["skin"] = self.skin_colour
            inner_top_colours["pin"] = Colour.BLACK
            configs.append((inner_top_colours, "torso", inner_top_name))

        #print(outer_top_name)
        #print(outer_top_colours)

        if outer_top_name:
            outer_top_colours["arm_connector"] = Colour.BLACK
            outer_top_colours["skin"] = self.skin_colour
            configs.append((outer_top_colours, "torso", outer_top_name))

        print("Finish resolving torso")
        return configs
    
    def resolve_eyes(self):
        name, colours = eyes_style_options.get_configured_style_config(self.image_url)

        colours["skin"] = self.skin_colour

        call = (colours, "eyes", name)
        print("Finish resolving arms")
        return [call]
    
    def resolve_hair(self):
        name, colours = hair_style_options.get_configured_style_config(self.image_url)

        colours["skin"] = self.skin_colour

        call = (colours, "hair", name)
        print("Finish resolving arms")
        return [call]


    def get_component_resolvers(self) -> list:
        return [
            self.resolve_legs,
            self.resolve_facial_hair,
            self.resolve_arms,       
            self.resolve_torso, 
            self.resolve_eyes,
            self.resolve_hair
        ]

    def build(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit each function to the executor
            futures = [executor.submit(resolver) for resolver in self.get_component_resolvers()]

            results = [future.result() for future in futures]

        all_pieces = []
        for components in results:
            for comp in components:
                print(comp)
                #print(components)
                all_pieces += get_component_string(*comp)
        from uuid import uuid4
        id = uuid4()
        filename = f"{id}.ldr"

        with open(f"{filename}", 'w') as file:
            # Join the array elements with a newline character and write to the file
            lines = f"{base}\n" + "\n".join(all_pieces)
            file.write(lines)