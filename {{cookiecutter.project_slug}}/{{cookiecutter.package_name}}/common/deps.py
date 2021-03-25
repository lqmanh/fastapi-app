from fastapi import Query

from {{cookiecutter.package_name}}.config import settings


class Pagination:
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
