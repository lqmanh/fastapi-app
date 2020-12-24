import asyncio
import functools
from types import ModuleType
from typing import Callable, Iterable, Optional, Tuple, Type, Union

from tortoise import Tortoise
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator
from tortoise.models import Model

from {{cookiecutter.package_name}}.common.types import CrudMethod
from {{cookiecutter.package_name}}.config import settings


def init_tortoise_models(modules: Iterable[Union[ModuleType, str]]):
    Tortoise.init_models(modules, "default")


def create_pydantic_model(
    cls: Type[Model],
    *,
    crud_method: CrudMethod,
    name: Optional[str] = None,
    computed: Tuple[str, ...] = (),
    include: Tuple[str, ...] = (),
    exclude: Tuple[str, ...] = (),
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
) -> Tuple[Type[PydanticModel], ...]:
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
        await f(*args, **kwargs)
        await Tortoise.close_connections()

    return wrapper


def cli_wrapper(f: Callable):
    return _coro_wrapper(_tortoise_wrapper(f))
