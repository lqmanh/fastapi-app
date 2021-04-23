from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer

from .users_models import User
from .users_service import UsersService


async def get_current_user(
    users_service: UsersService = Depends(),
    token: str = Depends(OAuth2PasswordBearer("/v1/users/sign-in")),
) -> User:
    user = await users_service.decode_access_token(token)
    return user


async def get_current_active_user(user: User = Depends(get_current_user)) -> User:
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user
