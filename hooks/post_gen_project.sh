#!/usr/bin/env bash

# Install FastAPI with Uvicorn dependencies
poetry add \
    uvicorn \
    fastapi \
    fastapi-utils \
    python-multipart \
    python-jose[cryptography] \
    passlib[bcrypt]

# Install Tortoise ORM dependencies
poetry add \
    tortoise-orm \
    asyncpg

# Install Typer dependencies
poetry add \
    typer

# Install other dependencies
poetry add \
    python-dotenv \
    tomlkit
    
# Install dev dependencies
poetry add --dev \
    pytest \
    pylint \
    pyflakes \
    black


git init && git add . && git commit -m 'Initial commit'
