import asyncio
import functools
from typing import Callable

from tortoise import Tortoise

from {{cookiecutter.package_name}}.config import settings


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
