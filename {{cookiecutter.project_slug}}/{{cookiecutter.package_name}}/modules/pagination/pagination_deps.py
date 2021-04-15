from typing import Generic

from fastapi import Query

from {{cookiecutter.package_name}}.config import settings
from {{cookiecutter.package_name}}.modules.pagination.pagination_dtos import PaginationOutput
from {{cookiecutter.package_name}}.modules.pagination.pagination_types import PT


class Pagination(Generic[PT]):
    max_limit = settings.pagination_max_limit
    limit: int
    offset: int

    def __init__(
        self,
        limit: int = Query(10, ge=1, le=settings.pagination_max_limit),
        offset: int = Query(0, ge=0),
    ):
        self.limit = limit
        self.offset = offset

    def to_pagination_output(self, total: int, data: PT) -> PaginationOutput[PT]:
        return PaginationOutput(
            total=total,
            limit=self.limit,
            offset=self.offset,
            data=list(data),
        )
