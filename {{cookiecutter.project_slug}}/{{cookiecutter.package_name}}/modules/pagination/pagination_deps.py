import asyncio
from typing import Callable, Generic, Iterable

from fastapi import Query
from tortoise.queryset import QuerySet

from {{cookiecutter.package_name}}.config import settings
from {{cookiecutter.package_name}}.modules.pagination.pagination_dtos import PaginationOutput
from {{cookiecutter.package_name}}.modules.pagination.pagination_types import MT, PT


class Pagination(Generic[MT, PT]):
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

    def to_pagination_output(
        self, total: int, data: Iterable[PT]
    ) -> PaginationOutput[PT]:
        return PaginationOutput(
            total=total,
            limit=self.limit,
            offset=self.offset,
            data=list(data),
        )

    async def paginate(
        self, queryset: QuerySet[MT], mapper: Callable[[MT], PT]
    ) -> PaginationOutput[PT]:
        total, data = await asyncio.gather(
            queryset.count(),
            queryset.limit(self.limit).offset(self.offset),
        )
        return self.to_pagination_output(total, map(mapper, data))
