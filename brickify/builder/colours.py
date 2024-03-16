
class Colour:
    BLACK = 0
    LIGHT_BEIGE = 19
    DARK_BLUE = 272
    WHITE = 15
    ORANGE = 25
    BROWN = 6
    REDDISH_BROWN = 70
    NOUGAT = 92
    MEDIUM_NOUGAT = 84
    DARK_BLUISH_GRAY = 72
    RED = 4
    LIGHT_BLUE = 9
    LIGHT_BLUISH_GRAY = 71
    YELLOW = 14
    BRIGHT_LIGHT_YELLOW = 226
    LIGHT_FLESH = 78
    BLUE = 1
    LIGHT_PURPLE = 69
    SAND_GREEN = 378
    GREEN = 2
    DARK_GREEN = 288

COLOUR_MAPPINGS = {
    "Orange": Colour.ORANGE,
    "Light Beige": Colour.LIGHT_BEIGE,
    "Fair": Colour.LIGHT_FLESH,
    "White": Colour.WHITE,
    "Navy Blue": Colour.DARK_BLUE,
    "Black": Colour.BLACK,
    "Dark Brown": Colour.REDDISH_BROWN,
    "Medium Brown": Colour.NOUGAT,
    "Dark Grey": Colour.DARK_BLUISH_GRAY,
    "Red": Colour.RED,
    "Brown": Colour.REDDISH_BROWN,
    "Light Blue": Colour.LIGHT_BLUE,
    "Dark Blue": Colour.DARK_BLUE,
    "Light Grey": Colour.LIGHT_BLUISH_GRAY,
    "Beige": Colour.LIGHT_BEIGE,
    "Yellow": Colour.YELLOW,
    "Grey": Colour.LIGHT_BLUISH_GRAY,
    "Blond": Colour.BRIGHT_LIGHT_YELLOW,
    "Light Brown": Colour.MEDIUM_NOUGAT,
    "Reddish Brown": Colour.REDDISH_BROWN,
    "Blue": Colour.BLUE,
    "Purple": Colour.LIGHT_PURPLE,
    "Green": Colour.GREEN,
    "Sand Green": Colour.SAND_GREEN,
    "Dark Green": Colour.DARK_GREEN,
}

valid_colours_string = ", ".join(list(COLOUR_MAPPINGS.keys()))