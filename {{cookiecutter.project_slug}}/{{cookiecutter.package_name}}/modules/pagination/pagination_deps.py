import asyncio
from typing import Callable, Generic, Iterable, Optional

from fastapi import Query
from tortoise.queryset import QuerySet

from {{cookiecutter.package_name}}.config import settings

from .pagination_dtos import PaginationOutput
from .pagination_types import MT, PT


class Pagination(Generic[MT, PT]):
    max_limit = settings.pagination_max_limit
    limit: int
    offset: int
    orderby: list[str]

    def __init__(
        self,
        limit: int = Query(10, ge=1, le=settings.pagination_max_limit),
        offset: int = Query(0, ge=0),
        orderby: Optional[str] = Query(None, description='Format: "id,-updated_at"'),
    ):
        self.limit = limit
        self.offset = offset
        if orderby:
            self.orderby = orderby.split(",")
        else:
            self.orderby = []


    def to_pagination_output(
        self, total: int, data: Iterable[PT]
    ) -> PaginationOutput[PT]:
        return PaginationOutput(
            total=total,
            limit=self.limit,
            offset=self.offset,
            orderby=self.orderby,
            data=list(data),
        )

    async def paginate(
        self, queryset: QuerySet[MT], mapper: Callable[[MT], PT]
    ) -> PaginationOutput[PT]:
        total, data = await asyncio.gather(
            queryset.count(),
            queryset.limit(self.limit).offset(self.offset).order_by(*self.orderby),
        )
        return self.to_pagination_output(total, map(mapper, data))
