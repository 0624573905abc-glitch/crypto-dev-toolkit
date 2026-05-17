import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.config = {}
        self.load_config()

    def load_config(self):
        try:
            if not os.path.exists(self.filename):
                raise ConfigError(f'Configuration file {self.filename} not found.')
            with open(self.filename, 'r') as file:
                self.config = json.load(file)
        except json.JSONDecodeError:
            raise ConfigError('Error decoding JSON from config file.')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {str(e)}')

    def get(self, key, default=None):
        if key in self.config:
            return self.config[key]
        if default is not None:
            return default
        raise ConfigError(f'Key {key} not found in config.')

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.config, file, indent=4)
        except Exception as e:
            raise ConfigError(f'Failed to save config: {str(e)}')