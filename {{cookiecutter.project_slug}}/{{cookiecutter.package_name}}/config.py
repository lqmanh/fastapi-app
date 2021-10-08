from types import ModuleType

from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = "{{cookiecutter.env_file}}"

    python_env: str = "dev"
    root_path: str = ""

    database_uri: str
    redis_dsn: str

    jwt_secret: str
    jwt_exp_seconds: int = -1  # no EXP

    pagination_max_limit: int = 100

    @property
    def tortoise_orm_model_modules(self) -> tuple[ModuleType, ...]:
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
            "use_tz": True,
        }

    @property
    def token_url(self) -> str:
        return f"{self.root_path}/v1/users/sign-in"


settings = Settings()
tortoise_orm_config = settings.tortoise_orm_config
