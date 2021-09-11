from typing import TypeVar

from {{cookiecutter.package_name}}.common.types import PydanticModel, TortoiseModel

TT = TypeVar("TT", bound=TortoiseModel)

PT = TypeVar("PT", bound=PydanticModel)
