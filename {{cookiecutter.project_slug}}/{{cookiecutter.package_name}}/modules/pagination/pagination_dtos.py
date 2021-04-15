from typing import Generic

from pydantic import BaseModel

from {{cookiecutter.package_name}}.modules.pagination.pagination_types import PT


class PaginationOutput(BaseModel, Generic[PT]):
    total: int
    limit: int
    offset: int
    data: list[PT]
