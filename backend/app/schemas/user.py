from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.user import User

UserPydantic = pydantic_model_creator(User, name='User')
UserInPydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)
