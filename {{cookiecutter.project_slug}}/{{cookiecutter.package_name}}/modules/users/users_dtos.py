from typing import Optional

from pydantic import validator

from {{cookiecutter.package_name}}.common.types import PydanticModel

from .users_types import Role


def check_username(username: str) -> str:
    if not 4 <= len(username) <= 32:
        raise ValueError("must be at least 4 and no more than 32 characters long")
    return username


def check_password(password: str) -> str:
    if not 8 <= len(password) <= 32:
        raise ValueError("must be at least 8 and no more than 32 characters long")
    return password


class SignUpInput(PydanticModel):
    username: str
    password: str

    _check_username = validator("username", allow_reuse=True)(check_username)
    _check_password = validator("password", allow_reuse=True)(check_password)


class SignInOutput(PydanticModel):
    access_token: str
    token_type: str


class UserCreate(SignUpInput):
    role: Role


class UserRead(PydanticModel):
    id: int
    username: str
    role: Role


class UserUpdate(PydanticModel):
    role: Optional[Role] = None


class PasswordUpdate(PydanticModel):
    current_password: str
    new_password: str

    _check_password = validator("*", allow_reuse=True)(check_password)
