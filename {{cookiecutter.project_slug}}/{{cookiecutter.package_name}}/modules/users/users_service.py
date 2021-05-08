from datetime import datetime, timedelta
from typing import Any, Union

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from passlib.context import CryptContext
from tortoise.queryset import QuerySet

from {{cookiecutter.package_name}}.config import settings

from .users_dtos import PasswordUpdate, SignUpInput, UserCreate, UserUpdate
from .users_models import User
from .users_types import Role


class UsersService:
    def __init__(self):
        self.crypt_ctx = CryptContext(schemes=["bcrypt"])

    def _get_password_hash(self, password: str) -> str:
        return self.crypt_ctx.hash(password)

    def _verify_password(self, password: str, password_hash: str) -> bool:
        return self.crypt_ctx.verify(password, password_hash)

    def _encode_access_token(self, sub: str) -> str:
        payload: dict[str, Any] = {"sub": sub}
        exp = settings.jwt_exp_seconds
        if exp > 0:
            payload["exp"] = datetime.utcnow() + timedelta(seconds=exp)
        access_token = jwt.encode(
            payload, settings.jwt_secret, algorithm=ALGORITHMS.HS256
        )
        return access_token

    def _decode_access_token(self, token: str) -> str:
        try:
            payload = jwt.decode(
                token, settings.jwt_secret, algorithms=[ALGORITHMS.HS256]
            )
            sub = payload["sub"]
            return sub
        except (JWTError, KeyError):
            raise HTTPException(status_code=401, detail="Cannot validate credentials")

    async def sign_up(self, input_: SignUpInput) -> User:
        user_create = UserCreate(
            username=input_.username, password=input_.password, role=Role.NORMAL
        )
        user = await self.create_user(user_create)
        return user

    async def sign_in(self, form_data: OAuth2PasswordRequestForm) -> str:
        user = await User.get_or_none(username=form_data.username)

        if not user or not self._verify_password(
            form_data.password, user.password_hash
        ):
            raise HTTPException(
                status_code=401, detail="Incorrect username or password"
            )
        if not user.is_active:
            raise HTTPException(status_code=403, detail="Inactive user")

        return self._encode_access_token(user.username)

    async def create_user(self, user_create: UserCreate) -> User:
        user_create_dict = user_create.dict()
        username = user_create_dict.pop("username")
        password_hash = self._get_password_hash(user_create_dict.pop("password"))
        user, _ = await User.get_or_create(
            {**user_create_dict, "password_hash": password_hash}, username=username
        )
        return user

    def read_users_queryset(self, *, filters: dict = {}) -> QuerySet[User]:
        return User.filter(**filters)

    async def read_user_by_access_token(self, token: str) -> User:
        sub = self._decode_access_token(token)
        user = await User.get(username=sub)
        return user

    async def read_user_by_id(self, id: int) -> User:
        user = await User.get(id=id)
        return user

    async def update_user(
        self, user: Union[User, int], user_update: UserUpdate
    ) -> User:
        if isinstance(user, int):
            user = await self.read_user_by_id(user)

        user.update_from_dict(user_update.dict(exclude_defaults=True))
        await user.save()
        return user

    async def update_user_password(
        self, user: Union[User, int], password_update: PasswordUpdate
    ) -> User:
        if isinstance(user, int):
            user = await self.read_user_by_id(user)

        current_password = password_update.current_password
        if not self._verify_password(current_password, user.password_hash):
            raise HTTPException(status_code=401, detail="Incorrect password")

        new_password = password_update.new_password
        user.password_hash = self._hash_password(new_password)
        await user.save()
        return user
