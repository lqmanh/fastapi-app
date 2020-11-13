import asyncio
from typing import List

from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from {{cookiecutter.package_name}}.modules.users.users_dtos import UserCreate, UserRead
from {{cookiecutter.package_name}}.modules.users.users_service import UsersService


router = InferringRouter()


@cbv(router)
class UsersController:
    users_service: UsersService = Depends()

    @router.post("/")
    async def create_user(self, user_create: UserCreate) -> UserRead:
        user = await self.users_service.create_user(user_create)
        return await UserRead.from_tortoise_orm(user)

    @router.get("/")
    async def read_users(self) -> List[UserRead]:
        users = await self.users_service.read_users()
        return await asyncio.gather(
            *(UserRead.from_tortoise_orm(user) for user in users)
        ) 

