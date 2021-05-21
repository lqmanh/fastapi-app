from types import ModuleType
from typing import Tuple

from pydantic import BaseSettings


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
        import aerich.models
        from {{cookiecutter.package_name}}.modules.users import users_models

        return (aerich.models, users_models)

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

    @property
    def default_token_url(self) -> str:
        return f"{self.root_path}/v1/users/sign-in"


settings = Settings()
tortoise_orm_config = settings.tortoise_orm_config
