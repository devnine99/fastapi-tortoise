import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.v1 import router as v1_router

os.environ.setdefault('SETTINGS_MODULE', 'config.settings.local')


def create_app():
    from config.settings import settings
    app = FastAPI(title="FastAPI and TortoiseORM")
    app.include_router(v1_router)
    register_tortoise(app, config=settings.DATABASE)
    return app


app = create_app()
