from pydantic import BaseModel, validator

from {{cookiecutter.package_name}}.common.types import CrudMethod
from {{cookiecutter.package_name}}.common.utils import create_pydantic_model
from {{cookiecutter.package_name}}.modules.users.users_models import User


class UserCreate(create_pydantic_model(User, crud_method=CrudMethod.Create)):
    password: str

    @validator("username")
    def _check_username_length(cls, username: str) -> str:
        if not 4 <= len(username) <= 32:
            raise ValueError("must be at least 4 and no more than 32 characters long")
        return username

    @validator("password")
    def _check_password_length(cls, password: str) -> str:
        if not 8 <= len(password) <= 32:
            raise ValueError("must be at least 8 and no more than 32 characters long")
        return password


UserRead = create_pydantic_model(User, crud_method=CrudMethod.Read)


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
