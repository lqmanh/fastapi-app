from types import ModuleType
from typing import Tuple

import aerich.models
from pydantic import BaseSettings

from {{cookiecutter.package_name}}.modules.users import users_models


class Settings(BaseSettings):
    python_env: str = "dev"
    root_path: str = ""
    database_uri: str
    jwt_secret: str
    jwt_exp_seconds: int = -1  # no EXP
    pagination_max_limit: int = 100

    class Config:
        env_file = ".env.example"

    @property
    def tortoise_orm_model_modules(self) -> Tuple[ModuleType]:
        return (users_models, aerich.models)

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


settings = Settings()
tortoise_orm_config = settings.tortoise_orm_config
