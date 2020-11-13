import os

from dotenv import load_dotenv

load_dotenv()
load_dotenv(f'.env.{os.getenv("PYTHON_ENV")}')

PYTHON_ENV = os.getenv("PYTHON_ENV") or "dev"
ROOT_PATH = os.getenv("ROOT_PATH") or "/"

DATABASE_URI = os.getenv("DATABASE_URI")
TORTOISE_ORM_CONFIG = {
    "connections": {
        "default": DATABASE_URI,
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

