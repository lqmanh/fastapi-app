#!/usr/bin/env bash

# Install FastAPI with Uvicorn dependencies
poetry add \
    uvicorn[standard] \
    fastapi \
    fastapi-utils \
    pydantic[dotenv] \
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
    tomlkit

# Install dev dependencies
poetry add --dev \
    pytest \
    pylint \
    pyflakes \
    black


git init && git add . && git commit -m 'Initial commit. Bootstrap project'
