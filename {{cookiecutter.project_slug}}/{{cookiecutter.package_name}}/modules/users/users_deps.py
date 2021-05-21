from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer

from {{cookiecutter.package_name}}.config import settings

from .users_models import User
from .users_service import UsersService


async def get_current_user(
    users_service: UsersService = Depends(),
    token: str = Depends(OAuth2PasswordBearer(settings.default_token_url)),
) -> User:
    me = await users_service.read_user_by_access_token(token)
    return me


async def get_current_active_user(me: User = Depends(get_current_user)) -> User:
    if not me.is_active:
        raise HTTPException(status_code=403, detail="Inactive user")
    return me
