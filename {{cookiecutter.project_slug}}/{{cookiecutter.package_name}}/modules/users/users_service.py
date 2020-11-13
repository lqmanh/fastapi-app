from typing import List

from passlib.context import CryptContext

from {{cookiecutter.package_name}}.modules.users.users_models import User
from {{cookiecutter.package_name}}.modules.users.users_dtos import UserCreate 


class UsersService:
    def __init__(self):
        self.crypt_ctx = CryptContext(schemes=["bcrypt"])

    def _get_password_hash(self, password: str) -> str:
        return self.crypt_ctx.hash(password)

    def _verify_password(self, password: str, password_hash: str) -> bool:
        return self.crypt_ctx.verify(password, password_hash)

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

