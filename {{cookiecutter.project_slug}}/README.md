# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation

### Requirements

- Python >= 3.7
- Poetry >= 1
- SQLite/PostgreSQL/MySQL/MariaDB
- [Environment variables](.env.example)

### Instructions

```sh
$ poetry install
```

### Init database migrations

```sh
$ poetry run aerich init-db
```

## Usage

### Run web app

```sh
$ poetry run uvicorn {{cookiecutter.package_name}}.server:app --reload
```

### Run CLI app

```sh
$ poetry run {{cookiecutter.cli}}
```
