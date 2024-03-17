import json
from enum import Enum

def get_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
class AutoStringEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name
    
class LowerAutoStringEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name