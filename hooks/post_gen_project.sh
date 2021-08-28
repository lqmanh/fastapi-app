#!/usr/bin/env bash

# Install FastAPI with Uvicorn dependencies
poetry add \
    uvicorn[standard] \
    fastapi \
    pydantic[dotenv] \
    git+https://github.com/lqmanh/fastapi-module.git#v0.2.0 \
    python-multipart \
    python-jose[cryptography] \
    passlib[bcrypt]

# Install Typer dependencies
poetry add \
    typer

# Install Tortoise ORM dependencies
poetry add \
    {% if cookiecutter.database_driver %} tortoise-orm[{{cookiecutter.database_driver}}] {% else %} tortoise-orm {% endif %} \
    aerich

# Install other dependencies
poetry add \
    rtoml \
    casbin \
    {% if cookiecutter.job_scheduler %} {{cookiecutter.job_scheduler}} {% endif %}

# Install dev dependencies
poetry add --dev \
    pytest \
    pytest-asyncio \
    mypy \
    black

# Remove unused modules
{% if cookiecutter.job_scheduler != "apscheduler" %} rm -r {{cookiecutter.package_name}}/modules/apscheduler {% endif %}
{% if cookiecutter.job_scheduler != "spinach" %} rm -r {{cookiecutter.package_name}}/modules/spinach {% endif %}

git init && git add . && git commit -m 'Initial commit. Bootstrap project'
