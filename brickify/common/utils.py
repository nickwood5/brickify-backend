import json
from enum import Enum

def get_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
class AutoStringEnum(Enum):
    def __str__(self):
        return self.name
    
class LowerAutoStringEnum(Enum):
    
    def __str__(self):
        return self.name.lower()###