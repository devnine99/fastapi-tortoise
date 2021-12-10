from typing import List

from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.models import User
from app.schemas import User_Pydantic, UserIn_Pydantic

router = APIRouter(prefix='/user', tags=['user'])


@router.get('', response_model=List[User_Pydantic])
async def get_user_list():
    return await User_Pydantic.from_queryset(User.all())


@router.post('', response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@router.get('/{pk}', response_model=User_Pydantic, responses={404: {'model': HTTPNotFoundError}})
async def get_user_detail(pk: int):
    return await User_Pydantic.from_queryset_single(User.get(pk=pk))


@router.put('/{pk}', response_model=User_Pydantic, responses={404: {'model': HTTPNotFoundError}})
async def update_user(pk: int, user: UserIn_Pydantic):
    await User.filter(pk=pk).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(User.get(pk=pk))
