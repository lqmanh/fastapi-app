from tortoise.fields import CharEnumField, CharField

from {{cookiecutter.package_name}}.common.types import TortoiseModel

from .users_types import Role


class User(TortoiseModel):
    password_hash: str = CharField(255)
    role: Role = CharEnumField(Role, max_length=255)
    username: str = CharField(255, unique=True)
