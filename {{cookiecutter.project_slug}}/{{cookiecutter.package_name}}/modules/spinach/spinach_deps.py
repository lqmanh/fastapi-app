from functools import lru_cache

from spinach import Engine, MemoryBroker

from {{cookiecutter.package_name}}.config import settings


@lru_cache
def get_spinach() -> Engine:
    spin = Engine(MemoryBroker(), f"{{cookiecutter.project_slug}}-{settings.python_env}")
    return spin
