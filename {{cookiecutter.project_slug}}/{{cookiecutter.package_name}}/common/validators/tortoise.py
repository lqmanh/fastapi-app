import re
from typing import Union

from tortoise.exceptions import ValidationError


def unsigned(value: Union[int, float]):
    if value < 0:
        raise ValidationError(f"{value} is not an unsigned number")


def positive(value: Union[int, float]):
    if value <= 0:
        raise ValidationError(f"{value} is not a positive number")
