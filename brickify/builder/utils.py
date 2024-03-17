import os
from collections import defaultdict
import json

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