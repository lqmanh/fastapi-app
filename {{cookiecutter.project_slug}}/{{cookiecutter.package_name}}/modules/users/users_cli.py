from typer import Abort, Typer, prompt, secho
from typer.colors import GREEN, RED

from {{cookiecutter.package_name}}.common.utils import cli_wrapper

from .users_dtos import UserCreate
from .users_service import UsersService


app = Typer()


@app.command()
@cli_wrapper
async def init():
    """Add an user."""

    users_service = UsersService()

    try:
        username = prompt("Username")
        password = prompt("Password", hide_input=True, confirmation_prompt=True)
        user = await users_service.create_user(
            UserCreate(username=username, password=password)
        )
        secho(f"Add user {user.username}", fg=GREEN)
    except:
        secho("Something went wrong", fg=RED)
        raise Abort()
