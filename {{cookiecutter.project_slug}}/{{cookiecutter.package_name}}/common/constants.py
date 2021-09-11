from datetime import date, datetime
from functools import partial

from tortoise.fields.data import JSON_DUMPS, JSON_LOADS


def serialize_dt(v) -> str:
    if isinstance(v, (datetime, date)):
        return v.isoformat()
    return v


#
# Because the default JSON encoder/decoder does not support `date`s and `datetime`s,
# you may want to use these ones with `JSONField`s
#
TORTOISE_JSON_DUMPS = partial(JSON_DUMPS, default=serialize_dt)
TORTOISE_JSON_LOADS = JSON_LOADS
