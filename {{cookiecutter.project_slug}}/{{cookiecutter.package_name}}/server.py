from pathlib import Path

import rtoml
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from {{cookiecutter.package_name}}.config import settings
{% if cookiecutter.job_scheduler == "apscheduler" -%}
from {{cookiecutter.package_name}}.modules.apscheduler.apscheduler_deps import get_scheduler
{% elif cookiecutter.job_scheduler == "spinach" -%}
from {{cookiecutter.package_name}}.modules.spinach.spinach_deps import get_spinach
{%- endif %}
from {{cookiecutter.package_name}}.modules.meta.meta_module import MetaModule
from {{cookiecutter.package_name}}.modules.users.users_module import UsersModule


pyproject = rtoml.load(Path(__file__).parent.joinpath("../pyproject.toml"))
app = FastAPI(
    debug=not settings.python_env.startswith("prod"),
    title=pyproject["tool"]["poetry"]["name"],
    description=pyproject["tool"]["poetry"]["description"],
    version=pyproject["tool"]["poetry"]["version"],
    root_path=settings.root_path,
)


#
# register all event handlers here
#
@app.on_event("startup")
def on_startup():
    {% if cookiecutter.job_scheduler == "apscheduler" -%}
    scheduler = get_scheduler()
    scheduler.start()
    {% elif cookiecutter.job_scheduler == "spinach" -%}
    spin = get_spinach()
    spin.start_workers(block=False)
    {% else -%}
    pass
    {%- endif %}


@app.on_event("shutdown")
def on_shutdown():
    {% if cookiecutter.job_scheduler == "apscheduler" -%}
    scheduler = get_scheduler()
    scheduler.shutdown()
    {% elif cookiecutter.job_scheduler == "spinach" -%}
    spin = get_spinach()
    spin.stop_workers()
    {% else -%}
    pass
    {%- endif %}


#
# register all middlewares & other stuff here
#
register_tortoise(app, settings.tortoise_orm_config)

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
app.include_router(MetaModule.router)
app.include_router(UsersModule.router)


if __name__ == "__main__":
    uvicorn.run(
        "{{cookiecutter.package_name}}.server:app",
        host="0.0.0.0",
        reload=not settings.python_env.startswith("prod"),
        reload_dirs=["{{cookiecutter.package_name}}"],
    )
