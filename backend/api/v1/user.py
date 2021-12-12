from typing import List

from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.models.user import User
from app.schemas.user import UserPydantic, UserInPydantic

router = APIRouter(prefix='/user', tags=['user'])


@router.get('', response_model=List[UserPydantic])
async def get_user_list():
    return await UserPydantic.from_queryset(User.all())


@router.post('', response_model=UserPydantic)
async def create_user(user: UserInPydantic):
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await UserPydantic.from_tortoise_orm(user_obj)


@router.get('/{pk}', response_model=UserPydantic, responses={404: {'model': HTTPNotFoundError}})
async def get_user_detail(pk: int):
    return await UserPydantic.from_queryset_single(User.get(pk=pk))


@router.put('/{pk}', response_model=UserPydantic, responses={404: {'model': HTTPNotFoundError}})
async def update_user(pk: int, user: UserInPydantic):
    await User.filter(pk=pk).update(**user.dict(exclude_unset=True))
    return await UserPydantic.from_queryset_single(User.get(pk=pk))
