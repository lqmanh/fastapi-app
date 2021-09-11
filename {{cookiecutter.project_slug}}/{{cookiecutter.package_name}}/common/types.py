from datetime import datetime

from pydantic import BaseModel
from tortoise.fields import DatetimeField, IntField
from tortoise.models import Model


class TortoiseModel(Model):
    class Meta:
        abstract = True

    id: int = IntField(pk=True)
    created_at: datetime = DatetimeField(auto_now_add=True)
    updated_at: datetime = DatetimeField(auto_now=True)


class PydanticModel(BaseModel):
    ...
