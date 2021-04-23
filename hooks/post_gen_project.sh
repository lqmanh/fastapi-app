#!/usr/bin/env bash

# Install FastAPI with Uvicorn dependencies
poetry add \
    uvicorn[standard] \
    fastapi \
    pydantic[dotenv] \
    python-multipart \
    python-jose[cryptography] \
    passlib[bcrypt]

# As currently the official fastapi-utils is not very active, we use a custom fork
poetry add git+https://github.com/lqmanh/fastapi-utils.git#detached

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
    apscheduler

# Install dev dependencies
poetry add --dev \
    pytest \
    pylint \
    pyflakes \
    black


git init && git add . && git commit -m 'Initial commit. Bootstrap project'
