import importlib
import os

os.environ.setdefault('SETTINGS_MODULE', 'config.settings.local')


class Settings:
    def __init__(self):
        settings_module = os.getenv('SETTINGS_MODULE')
        mod = importlib.import_module(settings_module)
        for config_key in dir(mod):
            if config_key.isupper():
                config_value = getattr(mod, config_key)
                setattr(self, config_key, config_value)


settings = Settings()
