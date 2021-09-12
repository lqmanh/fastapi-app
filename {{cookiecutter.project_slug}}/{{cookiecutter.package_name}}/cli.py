from typer import Typer

from {{cookiecutter.package_name}}.modules.users import users_cli

app = Typer()


app.add_typer(users_cli.app, name="users")


if __name__ == "__main__":
    app()
