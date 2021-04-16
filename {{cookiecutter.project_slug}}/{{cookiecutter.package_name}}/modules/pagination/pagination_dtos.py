from typing import Generic

from pydantic.generics import GenericModel

from {{cookiecutter.package_name}}.modules.pagination.pagination_types import PT


class PaginationOutput(GenericModel, Generic[PT]):
    total: int
    limit: int
    offset: int
    data: list[PT]
