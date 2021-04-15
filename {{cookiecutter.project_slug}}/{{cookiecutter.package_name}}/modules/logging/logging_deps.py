from functools import lru_cache
from logging import DEBUG, INFO, Formatter, Logger, StreamHandler, getLogger

from {{cookiecutter.package_name}}.config import settings


@lru_cache
def get_logger() -> Logger:
    logger = getLogger("{{cookiecutter.project_slug}}")

    logger.setLevel(DEBUG if not settings.python_env.startswith("prod") else INFO)

    handler = StreamHandler()
    handler.setFormatter(
        Formatter(
            "%(asctime)s %(name)s %(levelname)s %(pathname)s:%(lineno)d %(message)s"
        )
    )
    logger.handlers = [handler]

    return logger
