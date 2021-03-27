from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from {{cookiecutter.package_name}}.modules.users.users_deps import get_current_active_user
from {{cookiecutter.package_name}}.modules.users.users_dtos import LoginOutput, UserCreate, UserRead
from {{cookiecutter.package_name}}.modules.users.users_models import User
from {{cookiecutter.package_name}}.modules.users.users_service import UsersService


router = InferringRouter(tags=["Users"])


@cbv(router)
class UsersController:
    users_service: UsersService = Depends()

    @router.post("/", status_code=201)
    async def create_user(self, user_create: UserCreate) -> UserRead:
        user = await self.users_service.create_user(user_create)
        return await UserRead.from_tortoise_orm(user)

    @router.post("/login")
    async def login(
        self, form_data: OAuth2PasswordRequestForm = Depends()
    ) -> LoginOutput:
        result = await self.users_service.login(form_data)
        return LoginOutput(**result)

    @router.get("/me")
    async def read_current_user(
        self, user: User = Depends(get_current_active_user)
    ) -> UserRead:
        return await UserRead.from_tortoise_orm(user)
