# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation

### Requirements

- Python >= 3.7
- Poetry >= 1
- PostgreSQL >= 9.2
- [Environment variables](.env.example)

### Instructions

```sh
$ poetry install
```

## Usage

### Run web app

```sh
$ poetry run uvicorn {{cookiecutter.package_name}}.main:app --reload
```

### Run CLI app

```sh
$ poetry run {{cookiecutter.cli}}
```
