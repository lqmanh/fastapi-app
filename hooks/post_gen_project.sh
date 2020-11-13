#!/usr/bin/env bash

poetry add \
# Install FastAPI with Uvicorn dependencies
    uvicorn \
    fastapi \
    fastapi-utils \
    python-multipart \
    python-jose[cryptography] \
    passlib[bcrypt] \
# Install Tortoise ORM dependencies
    tortoise-orm \
    asyncpg \
# Install Typer dependencies
    typer \
# Install other dependencies
    python-dotenv \
    tomlkit \
    
poetry add --dev \
    pytest \
    pylint \
    pyflakes \
    black


mkdir migrations && poetry run aerich init-db


git init && git add . && git commit -m 'Initial commit'
