from brickify.builder.styles.inner_top import inner_top_style_options
from brickify.builder.styles.outer_top import outer_top_style_options, StyleDependencyType
from brickify.builder.acc import client, Model
import json
from brickify.builder.colours import Colour, valid_colours_string

def do(image_url):
    example = """
    {
        "inner": {
            "style": $inner_top_style,
            "components": $inner_colour_mappings
        },
        "outer": {
            "style": $outer_top_style,
            "components": $outer_colour_mappings
        }
    }
    where $inner_top_style and $outer_top_style are the codes preceeding the selected style
    and $inner_colour_mappings and $outer_colour_mappings are dicts of colour mappings; if there are no colours, set the value to null
    """

    prompt = f"""

    Considering the image, choose an inner top and outer top style that best represent the individuals current appearance.

    Specify colours for each of the component types in parentheses. Valid colours are: {valid_colours_string}


    Inner top styles:
    {inner_top_style_options.to_string()}

    Outer top styles:
    {outer_top_style_options.to_string()}

    Return the response as a JSON string without any ``` or \n formatting, in the format:

    {example}

    Only choose from the valid colours listed above
    """

    #print("aaaaa")
    #print(prompt)

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

    top_config = json.loads(response)

    inner_top_config = top_config["inner"]
    outer_top_config = top_config["outer"]

    inner_top_configured_style = inner_top_style_options.resolve_config(inner_top_config)
    outer_top_configured_style = outer_top_style_options.resolve_config(outer_top_config)


    if inner_top_configured_style is None:
        # Validate that outer top style doesn't require an inner top
        assert outer_top_configured_style.style.inner_dependency_type is not StyleDependencyType.REQUIRED
        inner_top_name, inner_top_colours = None, None
    else:
        inner_top_name = inner_top_configured_style.style.source
        inner_top_colours = {config.component_name: config.colour_code for config in inner_top_configured_style.configured_components}

    outer_top_name = None
    outer_top_colours = None

    if outer_top_configured_style is not None:
        outer_top_name = outer_top_configured_style.style.source
        if inner_top_name is not None:
            inner_top_name += "__inner_only"
        elif outer_top_configured_style.style.inner_dependency_type is StyleDependencyType.OPTIONAL:
            outer_top_name += "__full"

        outer_top_colours = {config.component_name: config.colour_code for config in outer_top_configured_style.configured_components}

    #print(inner_top_name)
    #print(outer_top_name)
    #print(inner_top_colours)
    #print(outer_top_colours)

    print(f"Torso: {inner_top_name}, {outer_top_name}")
    return inner_top_name, inner_top_colours, outer_top_name, outer_top_colours

