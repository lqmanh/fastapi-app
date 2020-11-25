from functools import lru_cache
import os
from types import ModuleType
from typing import Tuple

import aerich.models
from pydantic import BaseSettings

from {{cookiecutter.package_name}}.modules.access_control import access_control_models
from {{cookiecutter.package_name}}.modules.users import users_models


class Settings(BaseSettings):
    python_env: str = "dev"
    root_path: str = ""
    database_uri: str
    jwt_secret: str
    jwt_exp_seconds: int = -1  # no EXP

    class Config:
        env_file = ".env.example"

    @property
    def tortoise_orm_model_modules(self) -> Tuple[ModuleType]:
        return (access_control_models, users_models, aerich.models)

    @property
    def tortoise_orm_config(self) -> dict:
        return {
            "connections": {
                "default": self.database_uri,
            },
            "apps": {
                "default": {
                    "models": self.tortoise_orm_model_modules,
                }
            },
        }


@lru_cache()
def get_settings() -> Settings:
    return Settings()
