from functools import lru_cache

from {{cookiecutter.package_name}}.config import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()
