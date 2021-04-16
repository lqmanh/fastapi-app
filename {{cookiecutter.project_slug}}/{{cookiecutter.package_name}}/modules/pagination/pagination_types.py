from typing import TypeVar

from pydantic import BaseModel

from {{cookiecutter.package_name}}.common.types import TortoiseBaseModel

MT = TypeVar("MT", bound=TortoiseBaseModel)

PT = TypeVar("PT", bound=BaseModel)
