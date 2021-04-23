# fastapi-app

An opinionated modular FastAPI app boilerplate inspired by [NestJS](https://nestjs.com).

## Features

- Pre-built user management system with OAuth2 authentication
- Built-in pagination support
- Preconfigured logger
- Job scheduling with [APScheduler](https://github.com/agronholm/apscheduler)

## Tech Stack

- Python
- FastAPI + Uvicorn
- Tortoise ORM + Aerich
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
│   │   │   ├── ac_model.conf        # Casbin access model
│   │   │   └── ac_policies.csv      # Casbin permission policies
│   │   ├── logging                  # Logging module
│   │   │   └── logging_deps.py      #
│   │   ├── pagination               # Pagination module
│   │   │   ├── pagination_deps.py   #
│   │   │   ├── pagination_dtos.py   #
│   │   │   └── pagination_types.py  #
│   │   ├── scheduler                # Job scheduler module
│   │   │   └── scheduler_deps.py    #
│   │   └── users                    # User management module
│   │       ├── users_cli.py         # CLI sub-app
│   │       ├── users_controller.py  # Controller in NestJS, class-based view in Django
│   │       ├── users_deps.py        # Injectable dependencies
│   │       ├── users_dtos.py        # DTOs
│   │       ├── users_models.py      # Domain models
│   │       ├── users_service.py     # Business logic, also a special kind of dependencies
│   │       ├── users_types.py       # Types, enums,...
│   │       └── users_utils.py       # Helper functions, decorators,...
│   ├── cli.py                       # Root CLI app
│   ├── config.py                    # Global configurations
│   └── server.py                    # HTTP server
├── LICENSE                          # License
├── README.md                        # You know what it is ;)
├── aerich.ini                       # Aerich configurations
├── poetry.toml                      # Project-level Poetry configurations
└── pyproject.toml                   # Project meta
```
