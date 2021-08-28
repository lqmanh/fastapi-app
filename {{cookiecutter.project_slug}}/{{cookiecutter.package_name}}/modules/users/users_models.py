from tortoise.fields import BooleanField, CharEnumField, CharField

from {{cookiecutter.package_name}}.common.types import TortoiseBaseModel

from .users_types import Role


class User(TortoiseBaseModel):
    is_active = BooleanField(default=True)
    password_hash: str = CharField(255)
    role: Role = CharEnumField(Role, max_length=255)
    username: str = CharField(255, unique=True)

    class Meta:
        table = "users"
