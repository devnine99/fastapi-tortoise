import os

os.environ.setdefault('SETTINGS_MODULE', 'config.settings.local')

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.v1 import router as v1_router
from config.settings import settings


app = FastAPI(title='FastAPI')
app.include_router(v1_router)
register_tortoise(app, config=settings.DATABASE)
