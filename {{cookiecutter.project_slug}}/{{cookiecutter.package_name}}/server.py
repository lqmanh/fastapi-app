from os import path

import tomlkit
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from {{cookiecutter.package_name}}.config import settings
from {{cookiecutter.package_name}}.modules.users import users_controller


with open(path.join(path.dirname(__file__), "../pyproject.toml")) as f:
    pyproject = tomlkit.parse(f.read())

app = FastAPI(
    debug=not settings.python_env.startswith("prod"),
    title=pyproject["tool"]["poetry"]["name"],
    description=pyproject["tool"]["poetry"]["description"],
    version=pyproject["tool"]["poetry"]["version"],
    root_path=settings.root_path,
)


#
# register all middlewares & other stuff here
#
register_tortoise(app, settings.tortoise_orm_config, add_exception_handlers=True)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?://(.+\.)*localhost(:\d+)?",
    allow_methods=("*",),
    allow_headers=("*",),
    allow_credentials=True,
    max_age=3600,
)


#
# register all routers here
#
app.include_router(users_controller.router, prefix="/v1/users", tags=["Users"])


#
# register all metadata routes here
#
@app.get("/ping")
def pong(req: Request) -> dict:
    return {
        "message": "PONG",
        "environment": settings.python_env,
        "root_path": req.scope.get("root_path"),
        "build_revision": pyproject["tool"]["poetry"]["version"],
        "project": pyproject,
    }


if __name__ == "__main__":
    uvicorn.run(
        "{{cookiecutter.package_name}}.server:app",
        host="0.0.0.0",
        reload=not settings.python_env.startswith("prod"),
    )
