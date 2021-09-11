from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from {{cookiecutter.package_name}}.config import settings

from .users_models import User
from .users_service import UsersService


async def get_current_user(
    users_service: UsersService = Depends(),
    token: str = Depends(OAuth2PasswordBearer(settings.token_url)),
) -> User:
    me = await users_service.read_user_by_access_token(token)
    return me
