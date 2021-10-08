# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Guidelines

See https://github.com/lqmanh/fastapi-app.

## Installation

### Requirements

- Python >= 3.9
- Poetry >= 1
- SQLite/PostgreSQL/MySQL/MariaDB
- [Environment variables]({{cookiecutter.env_file}})

### Instructions

```sh
$ poetry install
```

## Usage

### Run apps

#### Run web app

```sh
$ poetry run python {{cookiecutter.package_name}}/server.py
```

#### Run CLI app

```sh
$ poetry run {{cookiecutter.cli}}
```

or

```sh
$ poetry run python {{cookiecutter.package_name}}/cli.py
```

#### Run worker

```sh
$ poetry run python {{cookiecutter.package_name}}/worker.py
```

### API documentation

#### Web app

Go to `/docs` or `/redoc` for more details.

#### CLI app

```sh
$ poetry run {{cookiecutter.cli}} --help
```
