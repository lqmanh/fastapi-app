from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from {{cookiecutter.package_name}}.modules.ac.ac_deps import get_authorized_user
from {{cookiecutter.package_name}}.modules.pagination.pagination_deps import Pagination
from {{cookiecutter.package_name}}.modules.pagination.pagination_dtos import PaginationOutput

from .users_dtos import (
    PasswordUpdate,
    SignInOutput,
    SignUpInput,
    UserCreate,
    UserRead,
    UserUpdate,
)

from .users_deps import get_current_active_user
from .users_mapper import UsersMapper
from .users_models import User
from .users_service import UsersService

router = InferringRouter(tags=["users"])


@cbv(router)
class UsersController:
    users_service: UsersService = Depends()
    users_mapper: UsersMapper = Depends()

    @router.post("/sign-up")
    async def sign_up(self, input_: SignUpInput) -> UserRead:
        user = await self.users_service.sign_up(input_)
        return self.users_mapper.to_user_read(user)

    @router.post("/sign-in")
    async def sign_in(
        self, form_data: OAuth2PasswordRequestForm = Depends()
    ) -> SignInOutput:
        access_token = await self.users_service.sign_in(form_data)
        return SignInOutput(access_token=access_token, token_type="bearer")

    @router.post("/", status_code=201)
    async def create_user(
        self, user_create: UserCreate, _: User = Depends(get_authorized_user)
    ) -> UserRead:
        user = await self.users_service.create_user(user_create)
        return self.users_mapper.to_user_read(user)

    @router.get("/")
    async def read_users(
        self,
        pagin: Pagination[User, UserRead] = Depends(Pagination),
        _: User = Depends(get_authorized_user),
    ) -> PaginationOutput[UserRead]:
        qs = self.users_service.read_users_queryset()
        return await pagin.paginate(qs, self.users_mapper.to_user_read)

    @router.get("/me")
    async def read_current_user(
        self, me: User = Depends(get_current_active_user)
    ) -> UserRead:
        return self.users_mapper.to_user_read(me)


    @router.get("/{user_id}")
    async def read_user(
        self,
        user_id: int,
        me: User = Depends(get_authorized_user),
    ) -> UserRead:
        user = await self.users_service.read_user_by_id(user_id)
        return self.users_mapper.to_user_read(user)

    @router.patch("/me")
    async def update_current_user(
        self,
        user_update: UserUpdate,
        me: User = Depends(get_current_active_user),
    ) -> UserRead:
        if user_update.role:
            raise HTTPException(
                status_code=403, detail="Users cannot update their role themselves"
            )

        user = await self.users_service.update_user(me, user_update)
        return self.users_mapper.to_user_read(user)

    @router.patch("/{user_id}")
    async def update_user(
        self,
        user_id: int,
        user_update: UserUpdate,
        me: User = Depends(get_authorized_user),
    ) -> UserRead:
        user = await self.users_service.update_user(user_id, user_update)
        return self.users_mapper.to_user_read(user)


    @router.patch("/me/password")
    async def update_current_user_password(
        self,
        password_update: PasswordUpdate,
        me: User = Depends(get_current_active_user),
    ) -> UserRead:
        user = await self.users_service.update_user_password(me, password_update)
        return self.users_mapper.to_user_read(user)
