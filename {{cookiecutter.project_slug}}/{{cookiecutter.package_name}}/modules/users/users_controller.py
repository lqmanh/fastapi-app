from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from {{cookiecutter.package_name}}.modules.ac.ac_deps import get_authorized_user
from {{cookiecutter.package_name}}.modules.pagination.pagination_deps import Pagination
from {{cookiecutter.package_name}}.modules.pagination.pagination_dtos import PaginationOutput

from .users_dtos import SignInOutput, SignUpInput, UserCreate, UserRead
from .users_models import User
from .users_service import UsersService
from .users_utils import user_to_user_read

router = InferringRouter(tags=["Users"])


@cbv(router)
class UsersController:
    users_service: UsersService = Depends()

    @router.post("/sign-up")
    async def sign_up(self, input_: SignUpInput) -> UserRead:
        user = await self.users_service.sign_up(input_)
        return user_to_user_read(user)

    @router.post("/sign-in")
    async def sign_in(
        self, form_data: OAuth2PasswordRequestForm = Depends()
    ) -> SignInOutput:
        result = await self.users_service.sign_in(form_data)
        return SignInOutput(**result)

    @router.post("/", status_code=201)
    async def create_user(
        self, user_create: UserCreate, _: User = Depends(get_authorized_user)
    ) -> UserRead:
        user = await self.users_service.create_user(user_create)
        return user_to_user_read(user)

    @router.get("/")
    async def read_users(
        self,
        pagin: Pagination[User, UserRead] = Depends(Pagination),
        _: User = Depends(get_authorized_user),
    ) -> PaginationOutput[UserRead]:
        qs = self.users_service.read_users_queryset()
        result = await pagin.paginate(qs, user_to_user_read)
        return result

    @router.get("/me")
    async def read_current_user(
        self, me: User = Depends(get_authorized_user)
    ) -> UserRead:
        return user_to_user_read(me)
