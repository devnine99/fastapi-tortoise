from tortoise import fields

from app.models.base import BaseModel


class User(BaseModel):
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=256)

    class PydanticMeta:
        exclude = ['password']
