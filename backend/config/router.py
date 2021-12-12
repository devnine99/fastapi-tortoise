from typing import Type

from tortoise import Model

from config.settings import settings


class Router:
    databases: list = list(settings.DATABASE.keys())

    def db_for_read(self, model: Type[Model]):
        if 'reader' in self.databases:
            return 'reader'
        return 'default'

    def db_for_write(self, model: Type[Model]):
        return 'default'
