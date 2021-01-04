from tortoise.fields import BooleanField, CharField

from {{cookiecutter.package_name}}.common.types import TortoiseBaseModel


class User(TortoiseBaseModel):
    username = CharField(64, unique=True)
    password_hash = CharField(255)
    is_active = BooleanField(default=True)

    class Meta:
        table = "users"

    class PydanticMeta:
        # always exclude password_hash
        exclude = ("password_hash",)
