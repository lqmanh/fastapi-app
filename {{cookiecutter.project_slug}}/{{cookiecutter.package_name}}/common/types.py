from enum import Enum

from tortoise.fields import DatetimeField
from tortoise.models import Model


class _TimestampMixin:
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)


class TortoiseBaseModel(_TimestampMixin, Model):
    class Meta:
        abstract = True


class CrudMethod(str, Enum):
    Create = "create"
    Read = "read"
    Update = "update"
    Delete = "delete"
