from tortoise.fields import DatetimeField
from tortoise.models import Model


class _TimestampMixin:
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)


class BaseModel(_TimestampMixin, Model):
    class Meta:
        abstract = True

