from datetime import datetime

from tortoise.fields import DatetimeField, IntField
from tortoise.models import Model


class TortoiseBaseModel(Model):
    id: int = IntField(pk=True)
    created_at: datetime = DatetimeField(auto_now_add=True)
    updated_at: datetime = DatetimeField(auto_now=True)

    class Meta:
        abstract = True
