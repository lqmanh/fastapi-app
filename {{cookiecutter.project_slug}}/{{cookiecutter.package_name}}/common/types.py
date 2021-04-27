from tortoise.fields import DatetimeField, IntField
from tortoise.models import Model


class _TimestampMixin:
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)


class TortoiseBaseModel(_TimestampMixin, Model):
    id = IntField(pk=True)

    class Meta:
        abstract = True
