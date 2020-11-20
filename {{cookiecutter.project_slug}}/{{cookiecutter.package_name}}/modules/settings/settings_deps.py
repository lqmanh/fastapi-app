from functools import lru_cache
import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    python_env: str = "dev"
    root_path: str = ""
    database_uri: str
    jwt_secret: str
    jwt_exp_seconds: int = -1  # no EXP

    class Config:
        env_file = ".env.example"

    @property
    def tortoise_orm_config(self) -> dict:
        return {
            "connections": {
                "default": self.database_uri,
            },
            "apps": {
                "default": {
                    "models": (
                        "{{cookiecutter.package_name}}.modules.users.users_models",
                        "aerich.models",
                    )
                }
            },
        }


@lru_cache()
def get_settings() -> Settings:
    return Settings()
