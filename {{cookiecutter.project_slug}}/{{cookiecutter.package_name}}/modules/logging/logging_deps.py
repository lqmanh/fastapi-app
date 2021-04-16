from functools import lru_cache
from logging import DEBUG, INFO, Formatter, Logger, StreamHandler, getLogger

from {{cookiecutter.package_name}}.config import settings


@lru_cache
def get_logger() -> Logger:
    logger = getLogger("{{cookiecutter.project_slug}}")

    logger.setLevel(DEBUG if not settings.python_env.startswith("prod") else INFO)

    std_handler = StreamHandler()
    std_handler.setLevel(INFO)
    std_handler.setFormatter(
        Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    )
    debug_handler = StreamHandler()
    debug_handler.addFilter(lambda record: record.levelno == DEBUG)
    debug_handler.setFormatter(
        Formatter(
            "%(asctime)s %(name)s %(levelname)s %(pathname)s:%(lineno)d %(message)s"
        )
    )
    logger.handlers = [std_handler, debug_handler]

    return logger
