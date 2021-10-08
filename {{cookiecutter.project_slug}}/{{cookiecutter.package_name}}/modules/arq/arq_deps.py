from functools import cache

from arq import ArqRedis, create_pool
from arq.connections import RedisSettings

from {{cookiecutter.package_name}}.config import settings


@cache
async def get_redis() -> ArqRedis:
    redis_settings = RedisSettings.from_dsn(settings.redis_dsn)
    redis = await create_pool(redis_settings)
    return redis
