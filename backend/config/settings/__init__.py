import importlib
import os


class Settings:
    def __init__(self):
        self._setup()

    def _setup(self):
        config_module = os.getenv('SETTINGS_MODULE')
        mod = importlib.import_module(config_module)
        for config_key in mod.__dir__():
            if config_key.isupper():
                config_value = getattr(mod, config_key)
                setattr(self, config_key, config_value)


settings = Settings()