from typing import Generic

from pydantic.generics import GenericModel

from .pagination_types import PT


class PaginationOutput(GenericModel, Generic[PT]):
    total: int
    limit: int
    offset: int
    order: list[str]
    data: list[PT]
