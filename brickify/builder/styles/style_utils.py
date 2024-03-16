from typing import Optional
from brickify.builder.colours import COLOUR_MAPPINGS, valid_colours_string, Colour
from brickify.builder.acc import client, Model
import json

class Style:
    def __init__(self, raw_name: str, components: list[str], is_null: bool=False,  prompt_name: Optional[str]=None, default_colours: Optional[dict]={}) -> None:
        if prompt_name is None:
            prompt_name = ' '.join(word.capitalize() for word in raw_name.split('_'))

        self.raw_name = raw_name
        self.prompt_name = prompt_name
        self.components = components
        self.default_colours = default_colours

        self.components_set = set(components)
        self.is_null = is_null

    def to_string(self):
        components_string = ", ".join(self.components)
        return f"{self.prompt_name} ({components_string})"
    
class ColourStyle:
    def __init__(self, description: str, colour_description_to_colour: dict[str, Colour]) -> None:
        self.description = description
        self.colour_description_to_colour = colour_description_to_colour

    def get_prompt(self):
        self.code_to_colour_description = {
            f"{i+1}": colour_description for i, colour_description in enumerate(self.colour_description_to_colour.keys())
        }

        code_to_colour_description_list = [
            f"{code}: {colour_description}" for code, colour_description in self.code_to_colour_description.items()
        ]
        colours_string = "\n".join(code_to_colour_description_list)

        return f"""
        Considering the image, choose the most appropriate colour for {self.description}.
        The options are:

        {colours_string}

        Return only the code preceeding the colour with no explaination
        """
    
    def get_configured_style(self, image_url: str):
        prompt = self.get_prompt()

        messages = [
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": "high",
                }
            },
            {"type": "text", "text": prompt},
        ]
        response = client.get_response(messages, Model.GPT_4_VISION)

        colour_description = self.code_to_colour_description[response]
        return self.colour_description_to_colour[colour_description]

        

class ConfiguredComponent:
    
    def __init__(self, default_colour: Colour, component_name: str, component_colour: str) -> None:
        self.component_name = component_name

        if component_colour is None:
            self.colour_code = default_colour
            return


        colour_code = COLOUR_MAPPINGS.get(component_colour)

        if colour_code is None:
            component_colour = client.get_closest(component_colour, list(COLOUR_MAPPINGS.keys()))
            colour_code = COLOUR_MAPPINGS.get(component_colour)

            if colour_code is None:
                colour_code = default_colour

        self.colour_code = colour_code

class ConfiguredStyle:
    def __init__(self, style: Style, components: Optional[dict]=None) -> None:
        self.style = style

        self.configured_components = []

        if components is not None:
            for name, colour in components.items():
                default_colour = style.default_colours.get(name)
                if default_colour is None:
                    default_colour = Colour.BLACK

                self.configured_components.append(ConfiguredComponent(default_colour, name, colour))
            return


    def to_colour_config(self):

        return {config.component_name: config.colour_code for config in self.configured_components}


class StyleOptions:
    def __init__(self, styles: list[Style], name: str, none_option: Optional[str]=None, prefix: str="") -> None:
        self.styles = styles
        self.none_option = none_option
        self.name = name

        all_styles = [style.to_string() for style in styles]

        if none_option is not None:
            all_styles.insert(0, none_option)
            styles.insert(0, None)

        self.style_codes = {f"{prefix}{i+1}": style for i, style in enumerate(all_styles)}
        self.style_code_mappings = {f"{prefix}{i+1}": style for i, style in enumerate(styles)}

    def resolve_config(self, config: dict) -> Optional[ConfiguredStyle]:
        style_key = str(config["style"])
        components = config["components"]

        style = self.style_code_mappings[style_key]


        print(style.components_set)
        print(style.components)
        if style is not None:
            if len(style.components) > 0:
                config_components_set = set(components)

                assert config_components_set == style.components_set
            return ConfiguredStyle(style, components)

        return None

    def to_string(self):
        style_strings = [f"{key}: {style}" for key, style in self.style_codes.items()]
        return "\n".join(style_strings)

    def get_prompt(self):

        return f"""
        Considering the image, choose an {self.name} style that best represent the individuals current appearance

        Specify colours for each of the component types in parentheses. Valid colours are: {valid_colours_string}

        {self.name} styles:
        {self.to_string()}

        Return the response as a JSON string without any ``` or \n formatting, in the format:
        {{
            "style": ${self.name}_style,
            "components": ${self.name}_colour_mappings
        }},

        where ${self.name}_style is the code preceeding the selected style
        and ${self.name}_colour_mappings is a dict of colour mappings; if there are no colours, set the value to null
        """

    def get_configured_style(self, image_url: str) -> Optional[ConfiguredStyle]:
        prompt = self.get_prompt()

        messages = [
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": "high",
                }
            },
            {"type": "text", "text": prompt},
        ]
        response = client.get_response(messages, Model.GPT_4_VISION)

        print(prompt)
        if response.startswith("```json"):
            response = response.lstrip("```json").rstrip("```")

        config = json.loads(response)

        print(f"Config for {self.name}: {config}")

        configured_style = self.resolve_config(config)

        return configured_style

    def get_configured_style_config(self, image_url: str):
        configured_style = self.get_configured_style(image_url)

        if configured_style is None:
            return None, None
        colours = configured_style.to_colour_config()

        return configured_style.style.raw_name, colours