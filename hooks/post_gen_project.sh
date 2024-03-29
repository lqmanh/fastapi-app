#!/usr/bin/env bash

# Install FastAPI with Uvicorn dependencies
poetry add \
    uvicorn[standard] \
    fastapi \
    pydantic[dotenv] \
    git+https://github.com/lqmanh/fastapi-module.git#ceb8c3d \
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
    arq

# Install dev dependencies
poetry add --dev \
    pytest \
    pytest-asyncio \
    mypy \
    black

# Remove unused modules

git init && git add .
