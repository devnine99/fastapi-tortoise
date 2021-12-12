from tortoise import models, fields


class BaseModel(models.Model):
    id = fields.BigIntField(pk=True)

    created_date = fields.DatetimeField(auto_now_add=True)
    updated_date = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True
