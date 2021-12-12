import importlib
import os


class Settings:
    def __init__(self):
        self._setup()

    def _setup(self):
        settings_module = self._get_settings_module()
        mod = importlib.import_module(settings_module)
        for config_key in mod.__dir__():
            if config_key.isupper():
                config_value = getattr(mod, config_key)
                setattr(self, config_key, config_value)

    @staticmethod
    def _get_settings_module():
        try:
            return os.environ['SETTINGS_MODULE']
        except KeyError:
            return 'config.settings.local'


settings = Settings()
