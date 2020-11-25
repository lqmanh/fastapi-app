from tortoise.fields import CASCADE, CharField, ForeignKeyField, ReverseRelation

from {{cookiecutter.package_name}}.common.types import TortoiseBaseModel


class Permission(TortoiseBaseModel):
    role = ForeignKeyField(
        "default.Role", related_name="permissions", on_delete=CASCADE
    )
    resource = ForeignKeyField(
        "default.Resource", related_name="permissions", on_delete=CASCADE
    )
    action = ForeignKeyField(
        "default.Action", related_name="permissions", on_delete=CASCADE
    )

    class Meta:
        table = "permissions"


class Role(TortoiseBaseModel):
    name = CharField(64, unique=True)
    description = CharField(255, default="")

    permissions: ReverseRelation[Permission]

    class Meta:
        table = "roles"


class Resource(TortoiseBaseModel):
    name = CharField(64, unique=True)
    description = CharField(255, default="")

    permissions: ReverseRelation[Permission]

    class Meta:
        table = "resources"


class Action(TortoiseBaseModel):
    name = CharField(64, unique=True)
    description = CharField(255, default="")

    permissions: ReverseRelation[Permission]

    class Meta:
        table = "actions"
