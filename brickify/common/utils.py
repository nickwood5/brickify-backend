import json
from enum import Enum

def get_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
class AutoStringEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name
    
    @classmethod
    def from_string(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"{value} is not a valid {cls.__name__}")

class LowerAutoStringEnum(Enum):
    
    def __str__(self):
        return self.name.lower()###
    
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()
    
    @classmethod
    def from_string(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"{value} is not a valid {cls.__name__}")