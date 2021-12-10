from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)

    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=256)

    class PydanticMeta:
        exclude = ['password']
