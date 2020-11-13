from tortoise.fields import BooleanField, CharField

from {{cookiecutter.package_name}}.common.base_model import BaseModel


class User(BaseModel):
    username = CharField(64, unique=True)
    password_hash = CharField(255)
    is_active = BooleanField(default=True)

    class Meta:
        table = "users"
