import asyncio
from inspect import iscoroutinefunction
from typing import Any, Callable, Coroutine, Generic, Iterable, Optional, Union

from fastapi import Query
from fastapi_module import enhanced_cbd
from tortoise.queryset import QuerySet

from {{cookiecutter.package_name}}.config import settings

from .pagination_dtos import PaginationOutput
from .pagination_types import MT, PT


@enhanced_cbd
class Pagination(Generic[MT, PT]):
    limit: int = Query(10, ge=1, le=settings.pagination_max_limit)
    offset: int = Query(0, ge=0)

    def __init__(
        self,
        orderby: Optional[str] = Query(None, description='Format: "id,-updated_at"'),
    ):
        self.orderby = orderby.split(",") if orderby else []

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
        self,
        queryset: QuerySet[MT],
        mapper: Callable[[MT], Union[PT, Coroutine[Any, Any, PT]]],
    ) -> PaginationOutput[PT]:
        total, data = await asyncio.gather(
            queryset.count(),
            queryset.limit(self.limit).offset(self.offset).order_by(*self.orderby),
        )

        if iscoroutinefunction(mapper):
            output_data = await asyncio.gather(*map(mapper, data))
        else:
            output_data = map(mapper, data)

        return self.to_pagination_output(total, output_data)
