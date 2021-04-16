import asyncio
import functools
from types import ModuleType
from typing import Callable, Iterable, Optional, Type, Union

from tortoise import Tortoise
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator
from tortoise.models import Model

from {{cookiecutter.package_name}}.config import settings

from .types import CrudMethod


def init_tortoise_models(modules: Iterable[Union[ModuleType, str]]):
    """
    See https://tortoise-orm.readthedocs.io/en/latest/contrib/pydantic.html#relations-early-init.
    """
    Tortoise.init_models(modules, "default")


def create_pydantic_model(
    cls: Type[Model],
    *,
    crud_method: CrudMethod,
    name: Optional[str] = None,
    computed: tuple[str, ...] = (),
    include: tuple[str, ...] = (),
    exclude: tuple[str, ...] = (),
    exclude_readonly: bool = False,
) -> Type[PydanticModel]:
    if crud_method == CrudMethod.Create or crud_method == CrudMethod.Update:
        exclude_readonly = True

    return pydantic_model_creator(
        cls,
        name=name or cls.__name__ + crud_method.value.title(),
        computed=computed,
        include=include,
        exclude=exclude,
        exclude_readonly=exclude_readonly,
    )


def create_pydantic_models(
    cls: Type[Model],
    *,
    crud_methods: Iterable[CrudMethod] = (
        CrudMethod.Create,
        CrudMethod.Read,
        CrudMethod.Update,
        CrudMethod.Delete,
    ),
) -> tuple[Type[PydanticModel], ...]:
    return tuple(
        create_pydantic_model(cls, crud_method=method) for method in crud_methods
    )


def _coro_wrapper(f: Callable):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


def _tortoise_wrapper(f: Callable):
    @functools.wraps(f)
    async def wrapper(*args, **kwargs):
        await Tortoise.init(settings.tortoise_orm_config)
        await Tortoise.generate_schemas()
        try:
            await f(*args, **kwargs)
        finally:
            await Tortoise.close_connections()

    return wrapper


def cli_wrapper(f: Callable):
    return _coro_wrapper(_tortoise_wrapper(f))
