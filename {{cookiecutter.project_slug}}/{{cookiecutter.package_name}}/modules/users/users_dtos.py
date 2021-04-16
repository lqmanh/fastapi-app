from pydantic import BaseModel, validator

from {{cookiecutter.package_name}}.common.types import CrudMethod
from {{cookiecutter.package_name}}.common.utils import create_pydantic_model

from .users_models import User
from .users_utils import check_password, check_username


class UserCreate(create_pydantic_model(User, crud_method=CrudMethod.Create)):
    password: str

    _check_username = validator("username", allow_reuse=True)(check_username)
    _check_password = validator("password", allow_reuse=True)(check_password)


UserRead = create_pydantic_model(User, crud_method=CrudMethod.Read)


class LoginOutput(BaseModel):
    access_token: str
    token_type: str
