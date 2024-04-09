from typing import Optional
from brickify.builder.colours import COLOUR_MAPPINGS, valid_colours_string, Colour
from brickify.builder.acc import client, Model
import json
from dataclasses import dataclass
from typing import Union
from brickify.common.utils import LowerAutoStringEnum, AutoStringEnum, get_json
from enum import auto, Enum


class StyleName(LowerAutoStringEnum):
    ARMS = auto()
    EYES = auto()
    FACIAL_HAIR = auto()
    HAIR = auto()
    INNER_TOP = auto()
    LEGS = auto()
    OUTER_TOP = auto()



class StyleOverrideCondition(AutoStringEnum):
    IS_NOT = auto()
    IS = auto()

class StyleOverrideEffect(AutoStringEnum):
    ADD_SUFFIX = auto()
    DELETE = auto()

class ComponentConfigurationMode(AutoStringEnum):
    STATIC = auto() # Colour is specified in component configuration
    GLOBAL = auto() # Colour comes from a globally defined colour
    DYNAMIC = auto() # Colour is chosen by vision model

@dataclass
class StyleOverrideConditionEffect:
    condition: StyleOverrideCondition
    effect: StyleOverrideEffect
    value: set[str]
    suffix_added: Optional[str]=None

    def __post_init__(self) -> None:
        if self.effect == StyleOverrideEffect.ADD_SUFFIX and self.suffix_added is None:
            raise Exception("Must provide suffix_added if effect is ADD_SUFFIX")

@dataclass
class StyleOverride:
    style_type: StyleName
    condition_effects: list[StyleOverrideConditionEffect]


@dataclass
class Component:
    name: str
    hidden_names: Optional[set[str]] = None
    default_colour: Optional[Colour] = None
    configuration_mode: ComponentConfigurationMode = ComponentConfigurationMode.DYNAMIC
    

    def __post_init__(self) -> None:
        if self.configuration_mode == ComponentConfigurationMode.STATIC and self.default_colour is None:
            raise Exception("Must provide default colour if component is static")




class Style:
    def __init__(self, name: StyleName, source: str, components: Optional[list[Union[Component, str]]] = None, is_null: bool=False,  prompt_name: Optional[str]=None, override: Optional[StyleOverride] = None) -> None:
        if prompt_name is None:
            prompt_name = ' '.join(word.capitalize() for word in source.split('_'))

        self.name = name
        self.source = source
        self.prompt_name = prompt_name
        self.is_null = is_null
        self.override = override

        self.variants = dict()

        if self.source is not None:
            self.variants[self.source] = get_json(f"brickify/builder/schematics/{name}/{source}.json")

            if override is not None:
                for condition_effect in override.condition_effects:
                    if condition_effect.effect == StyleOverrideEffect.ADD_SUFFIX:
                        variant_name = f"{self.source}{condition_effect.suffix_added}"
                        self.variants[variant_name] = get_json(f"brickify/builder/schematics/{name}/{variant_name}.json")

        print(f"Variants are: {self.variants}")
        
        if source is None and components is not None:
            raise Exception("components should not be provided if source is None")

        if components is None:
            self.string = f"{self.prompt_name}"
            self.all_component_names = {}
            return

        cleaned_components = []
        for component in components:
            if isinstance(component, str):
                component = Component(name=component)
                
            cleaned_components.append(component)

        self.globally_configured_components = {
            component.name: component for component in cleaned_components if component.configuration_mode == ComponentConfigurationMode.GLOBAL
        }

        self.components = cleaned_components

        self.all_component_names = {component.name for component in self.components}

        self.component_name_to_component = {
            comp.name: comp for comp in self.components 
        }
       

        self.configurable_components = [component for component in cleaned_components if component.configuration_mode == ComponentConfigurationMode.DYNAMIC]

        self.configurable_component_names = [component.name for component in self.configurable_components]
        
        self.configurable_components_set = set(self.configurable_component_names) 

        components_string = ", ".join(self.configurable_component_names)
        self.string = f"{self.prompt_name} ({components_string})"

        self.data = get_json(f"brickify/builder/schematics/{name}/{source}.json")

        for variant in self.variants.values():
            variant_components = set(variant.keys())

        assert variant_components <= self.all_component_names, f"Got {self.all_component_names}, expected {variant_components}"


        self.default_colours = {
            component.name: component.default_colour for component in cleaned_components if component.default_colour is not None
        }

        self.static_components = {
            component.name: component.default_colour for component in cleaned_components if component.configuration_mode == ComponentConfigurationMode.STATIC
        }

        



     

    def get_data(self):
        return get_json(f"brickify/builder/schematics/{self.name}/{self.source}.json")


    def to_string(self):
        return self.string
    
    def get_as_single_colour(self, colour: Colour) -> list[str]:
        res = []
        for component_parts in self.get_data().values():
            for part in component_parts:
                res.append(part.format(colour))

        return res

    
    def get_coloured(self, component_name_to_colour: dict[str, Colour], source: str) -> list[str]:
        #assert self.configurable_components_set == set(component_name_to_colour.keys()), f"Expected {self.configurable_components_set}, got {set(component_name_to_colour.keys())}"

        print(f"Getting coloured for {self.prompt_name}")

        print(component_name_to_colour)
        res = []

        if source is None:
            return []
        
        component_names = set()

        res.append(f"0 Type: {self.name}, Source: {self.prompt_name}, {source}")

        data = self.variants[source]
        for component_name in self.configurable_component_names:
            colour_code = component_name_to_colour[component_name]

            if component_name not in data.keys():
                continue

            component_names.add(component_name)

            component_parts = data[component_name]

            res.append(f"0 Component: {component_name}, colour = {colour_code}")
            for component_part in component_parts:
                res.append(component_part.format(colour_code))

        for component_name in self.globally_configured_components.keys():
            colour_code = component_name_to_colour[component_name]
            print(self.prompt_name)
            component_parts = data[component_name]
            component_names.add(component_name)

            for component_part in component_parts:
                res.append(component_part.format(colour_code))
        
        default_components_list = []

        for component_name, default_colour in self.static_components.items():
            component_parts = data.get(component_name)
            if component_parts is None:
                continue

            component_names.add(component_name)

            for component_part in component_parts:
                default_components_list.append(component_part.format(default_colour))

        assert set(data.keys()) >= component_names, f"{source} has {set(data.keys())}, got {component_names}"

        return res + default_components_list

        #for component_name, colour in component_name_to_colour.items():
    
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
    def __init__(self, style: Style, components: dict[str, Colour]={}) -> None:
        self.style = style
        self.components = components
        self.source = None

 

    def retrive_global_colours(self, global_colours):
        for component in self.style.globally_configured_components.keys():
            self.components[component] = global_colours[component]



    def to_colour_config(self):

        return {config.component_name: config.colour_code for config in self.configured_components}

from typing import TypeVar
StyleSubclass = TypeVar("StyleSubclass", bound=Style)

class StyleOptions:
    def __init__(self, styles: list[StyleSubclass], prefix: str="") -> None:
        self.styles = styles

        style_name_set = {style.name for style in styles}
        assert len(style_name_set) == 1

        self.name = styles[0].name

        all_styles = [style.to_string() for style in styles]
       
        self.style_codes = {f"{prefix}{i+1}": style for i, style in enumerate(all_styles)}
        self.style_code_mappings = {f"{prefix}{i+1}": style for i, style in enumerate(styles)}

    def resolve_config(self, config: dict) -> Optional[ConfiguredStyle]:
        style_key = str(config["style"])

        components = config["components"] if config["components"] is not None else {}

        style = self.style_code_mappings[style_key]

        if style.source is not None:
            if len(style.components) > 0:
                config_components_set = set(components)
                
                assert config_components_set == style.configurable_components_set

                components.update(style.default_colours)
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

        if response.startswith("```json"):
            response = response.lstrip("```json").rstrip("```")

        config = json.loads(response)

        configured_style = self.resolve_config(config)

        return configured_style

    def get_configured_style_config(self, image_url: str):
        configured_style = self.get_configured_style(image_url)

        if configured_style is None:
            return None, None
        colours = configured_style.to_colour_config()

        return configured_style.style.source, colours
    

