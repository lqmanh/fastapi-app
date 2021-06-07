# Fastapi-app

Fastapi-app is an opinionated modular FastAPI app boilerplate inspired by [NestJS](https://nestjs.com) and Flask's [Blueprint](https://flask.palletsprojects.com/blueprints). It is suitable for small to medium sized API oriented microservices.

## Features

- Authentication with OAuth2
- Access control with [Casbin](https://github.com/casbin/pycasbin)
- Job scheduling with [APScheduler](https://github.com/agronholm/apscheduler) or [Spinach](https://github.com/NicolasLM/spinach)
- CLI with [Typer](https://github.com/tiangolo/typer)
- Built-in pagination support
- Preconfigured logger

## Tech Stack

- Python
- FastAPI + Uvicorn
- Tortoise ORM + Aerich
- Casbin
- APScheduler/Spinach
- Typer

## Usage

```sh
cookiecutter https://github.com/lqmanh/fastapi-app
```

## Project Structure

```sh
{{cookiecutter.project_slug}}        # Project root
├── {{cookiecutter.package_name}}    # Root module, containing all source code
│   ├── common                       # Common components
│   │   ├── types.py                 # Common types, enums,...
│   │   └── utils.py                 # Common helper functions, decorators,...
│   ├── modules                      # Where magic happens
│   │   ├── ac                       # Access control module
│   │   │   ├── ac_deps.py           #
│   │   │   ├── ac_model.conf        # Access control model
│   │   │   └── ac_policies.csv      # Policies
│   │   ├── apscheduler              # APScheduler module
│   │   │   └── apscheduler_deps.py  #
│   │   ├── logging                  # Logging module
│   │   │   └── logging_deps.py      #
│   │   ├── pagination               # Pagination module
│   │   │   ├── pagination_deps.py   #
│   │   │   ├── pagination_dtos.py   #
│   │   │   └── pagination_types.py  #
│   │   ├── spinach                  # Spinach module
│   │   │   └── spinach_deps.py      #
│   │   └── users                    # User management module
│   │       ├── users_cli.py         # CLI sub-app
│   │       ├── users_controller.py  # Controller in NestJS, class-based view in Django
│   │       ├── users_deps.py        # Injectable dependencies
│   │       ├── users_dtos.py        # DTOs, view models
│   │       ├── users_mapper.py      # Mapper that maps domain models to DTOs
│   │       ├── users_models.py      # Domain models
│   │       ├── users_service.py     # Business logic, also a special kind of dependencies
│   │       └── users_types.py       # Types, enums,...
│   ├── cli.py                       # Root CLI app
│   ├── config.py                    # Global configurations
│   └── server.py                    # HTTP server
├── LICENSE                          # License
├── README.md                        # You know what it is ;)
├── aerich.ini                       # Aerich configurations
├── poetry.toml                      # Project-level Poetry configurations
└── pyproject.toml                   # Project meta
```
