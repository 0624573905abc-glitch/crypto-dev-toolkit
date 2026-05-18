import json
import os

DEFAULT_CONFIG = {
    "game_name": "MyGame",
    "resolution": "1920x1080",
    "fullscreen": True,
    "volume": 75,
    "controls": {
        "move_forward": "W",
        "move_backward": "S",
        "turn_left": "A",
        "turn_right": "D",
        "jump": "Space"
    }
}

class ConfigLoader:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as file:
                user_config = json.load(file)
            return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

    def save(self):
        with open(self.config_path, 'w') as file:
            json.dump(self.config, file, indent=4)

# Usage example:
# config_loader = ConfigLoader()
# print(config_loader.get('game_name'))
