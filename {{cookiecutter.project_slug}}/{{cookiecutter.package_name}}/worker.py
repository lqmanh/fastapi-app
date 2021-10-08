from typing import cast

from arq import run_worker
from arq.connections import RedisSettings
from arq.typing import WorkerSettingsType
from tortoise import Tortoise

from {{cookiecutter.package_name}}.config import settings


async def startup(ctx):
    await Tortoise.init(settings.tortoise_orm_config)


async def shutdown(ctx):
    await Tortoise.close_connections()


class WorkerSettings:
    cron_jobs = []
    functions = []
    job_timeout = 10  # seconds
    max_jobs = 10
    max_tries = 2
    on_shutdown = shutdown
    on_startup = startup
    poll_delay = 1  # second
    redis_settings = RedisSettings.from_dsn(settings.redis_dsn)


if __name__ == "__main__":
    settings_cls = cast(WorkerSettingsType, WorkerSettings)
    run_worker(settings_cls)
