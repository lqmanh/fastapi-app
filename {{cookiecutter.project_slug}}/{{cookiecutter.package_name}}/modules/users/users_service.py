from datetime import datetime, timedelta
from typing import Any, Dict, List

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist

from {{cookiecutter.package_name}}.modules.settings.settings_deps import (
    Settings,
    get_settings,
)
from {{cookiecutter.package_name}}.modules.users.users_dtos import UserCreate
from {{cookiecutter.package_name}}.modules.users.users_models import User


class UsersService:
    def __init__(self, settings: Settings = Depends(get_settings)):
        self.settings = settings
        self.crypt_ctx = CryptContext(schemes=["bcrypt"])

    def _get_password_hash(self, password: str) -> str:
        return self.crypt_ctx.hash(password)

    def _verify_password(self, password: str, password_hash: str) -> bool:
        return self.crypt_ctx.verify(password, password_hash)

    def _encode_access_token(self, username: str) -> str:
        payload: Dict[str, Any] = {"sub": username}
        exp = self.settings.jwt_exp_seconds
        if exp > 0:
            payload["exp"] = datetime.utcnow() + timedelta(seconds=exp)
        access_token = jwt.encode(
            payload, self.settings.jwt_secret, algorithm=ALGORITHMS.HS256
        )
        return access_token

    async def decode_access_token(self, token: str) -> User:
        try:
            payload = jwt.decode(
                token, self.settings.jwt_secret, algorithms=[ALGORITHMS.HS256]
            )
            username = payload["sub"]
            user = await User.get(username=username)
            return user
        except (JWTError, KeyError, DoesNotExist):
            raise HTTPException(
                status_code=401, detail="Could not validate credentials"
            )

    async def create_user(self, user_create: UserCreate) -> User:
        user_create_dict = user_create.dict()
        username = user_create_dict.pop("username")
        password_hash = self._get_password_hash(user_create_dict.pop("password"))
        user, _ = await User.get_or_create(
            {**user_create_dict, "password_hash": password_hash}, username=username
        )
        return user

    async def read_users(self) -> List[User]:
        return await User.all()

    async def login(self, form_data: OAuth2PasswordRequestForm) -> Dict[str, str]:
        user = await User.get_or_none(username=form_data.username)

        if not user or not self._verify_password(
            form_data.password, user.password_hash
        ):
            raise HTTPException(
                status_code=401, detail="Incorrect username or password"
            )
        access_token = self._encode_access_token(user.username)

        return {"access_token": access_token, "token_type": "bearer"}
