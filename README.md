# fastapi-app

An opinionated modular FastAPI app template inspired by [NestJS](https://nestjs.com).

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
{{cookiecutter.project_slug}}       # Project root
├── {{cookiecutter.package_name}}   # Root module, containing all source code
│   ├── common                      # Common components
│   │   ├── types.py                # General types
│   │   └── utils.py                # Helper functions, decorators,...
│   ├── modules                     # Modules, where magic happens
│   │   └── users                   # Account management module
│   │       ├── users_cli.py        # CLI sub-app
│   │       ├── users_controller.py # Controller/router
│   │       ├── users_deps.py       # Injectable providers
│   │       ├── users_dtos.py       # DTOs
│   │       ├── users_models.py     # Domain models
│   │       └── users_service.py    # A special kind of providers
│   ├── cli.py                      # Root CLI app
│   ├── config.py                   # Global configurations
│   └── server.py                   # HTTP server
├── LICENSE                         # License
├── README.md                       # You know what it is ;)
├── aerich.ini                      # Aerich configurations
├── poetry.toml                     # Project-level Poetry configurations
└── pyproject.toml                  # Project meta
```
