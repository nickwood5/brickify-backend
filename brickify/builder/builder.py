from typing import Optional
from django.core.files.uploadedfile import UploadedFile
from brickify.common.utils import AutoStringEnum
from enum import auto
import concurrent.futures
from brickify.builder.styles import skin_colour_options, legs_style_options, facial_hair_style_options, arm_style_options, eyes_style_options, hair_style_options, inner_top_style_options, outer_top_style_options
from brickify.builder.styles.style_utils import StyleOverrideCondition
from brickify.builder.test import do
import os
import base64
from brickify.builder.utils import load_json_from_folders
import json
from brickify.builder.colours import Colour

class BuildingMode(AutoStringEnum):
    FROM_IMAGE_FILE = auto()
    FROM_IMAGE_URL = auto()

class ResolverType(AutoStringEnum):
    COMPONENT = auto()
    GLOBAL_COLOUR = auto()


import os
from collections import defaultdict
import json

def load_json_from_folders(main_folder):
    # Iterate through all items in the main folder
    res = dict()
    for item in os.listdir(main_folder):
        res[item] = dict()
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

json_files_content = load_json_from_folders("brickify/builder/schematics")

print(json_files_content)

def get_component_string(colour_mapping, component_type, name):

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

SUPPORTED_IMAGE_TYPES = {
    "image/png",
    "image/jpeg",
    "image/gif",
    "image/webp"
}

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
    print(f"Mime_type is {mime_type}")
    if mime_type not in SUPPORTED_IMAGE_TYPES:
        raise ValueError("Unsupported image type")
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


    def resolve_skin_colour(self):
        skin_colour = skin_colour_options.get_configured_style(self.image_url)

        return {"skin": skin_colour}, ResolverType.GLOBAL_COLOUR

    def resolve_legs(self):
        return legs_style_options.get_configured_style(self.image_url), ResolverType.COMPONENT
        name, colours = legs_style_options.get_configured_style_config(self.image_url)


        call = (colours, "legs", name)

        return [call], ResolverType.COMPONENT
    
    def resolve_facial_hair(self):
        print("Start resolving facial hair")
        return facial_hair_style_options.get_configured_style(self.image_url), ResolverType.COMPONENT
        name, colours = facial_hair_style_options.get_configured_style_config(self.image_url)
        if name is None:
            return []

        call = (colours, "facial_hair", name)
        #print(call)
        print("Finish resolving facial hair")
        return [call], ResolverType.COMPONENT
    
    def resolve_arms(self):
        print("Start resolving arms")
        return arm_style_options.get_configured_style(self.image_url), ResolverType.COMPONENT
        name, colours = arm_style_options.get_configured_style_config(self.image_url)



        call = (colours, "arms", name)
        print("Finish resolving arms")
        return [call], ResolverType.COMPONENT




    def resolve_torso(self):
        
        print(f"Start resolving torso")

        inner_top_name, inner_top_colours, outer_top_name, outer_top_colours = do(self.image_url)

        configs = []
        if inner_top_colours is not None:
            inner_top_colours["arm_connector"] = Colour.BLACK
            inner_top_colours["pin"] = Colour.BLACK
            configs.append((inner_top_colours, "torso", inner_top_name))

        #print(outer_top_name)
        #print(outer_top_colours)

        if outer_top_name:
            outer_top_colours["arm_connector"] = Colour.BLACK
            configs.append((outer_top_colours, "torso", outer_top_name))

        print("Finish resolving torso")
        return configs, ResolverType.COMPONENT
    
    def resolve_inner_top(self):
        return inner_top_style_options.get_configured_style(self.image_url), ResolverType.COMPONENT
    
    def resolve_outer_top(self):
        return outer_top_style_options.get_configured_style(self.image_url), ResolverType.COMPONENT
    
    def resolve_eyes(self):
        print("test", eyes_style_options.get_configured_style(self.image_url).components)
        return eyes_style_options.get_configured_style(self.image_url), ResolverType.COMPONENT
        name, colours = eyes_style_options.get_configured_style_config(self.image_url)


        call = (colours, "eyes", name)
        print("Finish resolving arms")
        return [call], ResolverType.COMPONENT
    
    def resolve_hair(self):
        configured_style = hair_style_options.get_configured_style(self.image_url)

        return configured_style, ResolverType.COMPONENT
        name, colours = hair_style_options.get_configured_style_config(self.image_url)

        hair_top = colours["hair"] if colours["hair"] is not None else None

        if hair_top is not None:
            colours["hair_top"] = hair_top

        print("hair is " + name)
        call = (colours, "hair", name)
        print("Finish resolving hair")
        return [call], ResolverType.COMPONENT


    def get_component_resolvers(self) -> list:
        return [
            #self.resolve_legs,
            #self.resolve_facial_hair,
            #self.resolve_arms,       
            #self.resolve_inner_top,
            #self.resolve_outer_top, 
            #self.resolve_eyes,
            self.resolve_hair,
            self.resolve_skin_colour,
        ]

    def build(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit each function to the executor
            futures = [executor.submit(resolver) for resolver in self.get_component_resolvers()]

            results = [future.result() for future in futures]

        all_pieces = []


        global_colours = dict()

        call_args_list = []

        configured_styles_map = dict()
        for data, resolver_type in results:
            if resolver_type == ResolverType.GLOBAL_COLOUR:
                global_colours.update(data)
                continue
            elif resolver_type == ResolverType.COMPONENT:
                configured_styles_map[data.style.name] = data
                pass
            #for comp in data:
            #    call_args_list.append(comp)
            #    print(comp)
            #    #print(components)

        print(configured_styles_map)



        for style_name, configured_style in configured_styles_map.items():
            style_override = configured_style.style.override

            if style_override is None:
                continue

            target_style_name =  style_override.style_type
            configured_styles_map[target_style_name]

            if style_override.condition == StyleOverrideCondition.IS_NOT:
                if configured_styles_map[target_style_name].style.source == style_override.value:
                    configured_styles_map[target_style_name].style.source += style_override.suffix_added

        for style_name, configured_style in configured_styles_map.items():
            all_pieces += configured_style.style.get_coloured(configured_style.components, global_colours)

        print(f"All pieces {all_pieces}")

        from uuid import uuid4
        id = uuid4()
        filename = f"brickify/generated_models/{id}.ldr"

        with open(f"{filename}", 'w') as file:
            # Join the array elements with a newline character and write to the file
            lines = f"{base}\n" + "\n".join(all_pieces)
            file.write(lines)

        print(f"Built {filename}")
        print(global_colours)

        return id