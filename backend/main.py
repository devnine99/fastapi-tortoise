from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import config
from api.v1 import router as v1_router


app = FastAPI(title="FastAPI and TortoiseORM")

app.include_router(v1_router)
register_tortoise(app, config=config.DATABASE, generate_schemas=True)
