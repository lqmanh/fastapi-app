from tortoise.fields import BooleanField, CharEnumField, CharField

from {{cookiecutter.package_name}}.common.types import TortoiseBaseModel

from .users_types import Role


class User(TortoiseBaseModel):
    username = CharField(64, unique=True)
    password_hash = CharField(255)
    is_active = BooleanField(default=True)
    role = CharEnumField(Role, max_length=255)

    class Meta:
        table = "users"
