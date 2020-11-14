from os import path

import tomlkit
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from {{cookiecutter.package_name}}.config import PYTHON_ENV, ROOT_PATH, TORTOISE_ORM_CONFIG
from {{cookiecutter.package_name}}.modules.users import users_controller


with open(path.join(path.dirname(path.abspath(__file__)), "../pyproject.toml")) as f:
    pyproject = tomlkit.parse(f.read())


app = FastAPI(
    debug=not PYTHON_ENV.startswith("prod"),
    title=pyproject["tool"]["poetry"]["name"],
    description=pyproject["tool"]["poetry"]["description"],
    version=pyproject["tool"]["poetry"]["version"],
    root_path=ROOT_PATH,
)


#
# register all middlewares & other stuff here
#
register_tortoise(app, TORTOISE_ORM_CONFIG, add_exception_handlers=True)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?://(.+\.)*localhost(:\d+)?",
    allow_methods=("*",),
    allow_headers=("*",),
    allow_credentials=True,
    max_age=3600,
)


#
# register all event handlers & scheduled tasks here
#


#
# register all routers here
#
app.include_router(users_controller.router, prefix="/v1/users")


#
# register all metadata routes here
#
@app.get("/ping")
def pong(req: Request) -> dict:
    return {
        "message": "PONG",
        "environment": PYTHON_ENV,
        "root_path": req.scope.get("root_path"),
        "build_revision": pyproject["tool"]["poetry"]["version"],
        "project": pyproject,
    }
