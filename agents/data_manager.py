import json
import os
from datetime import datetime

class DataManager:
    def __init__(self, base_dir="data"):
        self.base_dir = base_dir
        # Ensure directories exist
        for subdir in ["raw", "processed", "logs"]:
            os.makedirs(os.path.join(self.base_dir, subdir), exist_ok=True)

    def save_json(self, filename, data, folder="processed"):
        path = os.path.join(self.base_dir, folder, filename)
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[*] Data saved to {path}")

    def load_json(self, filename, folder="processed"):
        path = os.path.join(self.base_dir, folder, filename)
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return json.load(f)
