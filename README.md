# fastapi-app

An opinionated modular FastAPI app boilerplate inspired by [NestJS](https://nestjs.com).

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
│   │   ├── pagination               #
│   │   │   ├── pagination_deps.py   #
│   │   │   ├── pagination_dtos.py   #
│   │   │   └── pagination_types.py  #
│   │   └── users                    # Account management module
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
