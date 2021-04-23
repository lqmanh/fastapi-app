from typer import Abort, Option, Typer, secho
from typer.colors import GREEN, RED

from {{cookiecutter.package_name}}.common.utils import cli_wrapper

from .users_dtos import UserCreate
from .users_service import UsersService
from .users_types import Role

app = Typer()


@app.command()
@cli_wrapper
async def create(
    username: str,
    role: Role = Role.NORMAL,
    password: str = Option(..., prompt=True, confirmation_prompt=True),
):
    """Create an user."""
    users_service = UsersService()

    try:
        user_create = UserCreate(username=username, password=password, role=role)
        user = await users_service.create_user(user_create)
        secho(f"Create user {user.username}", fg=GREEN)
    except:
        secho("Something went wrong", fg=RED)
        raise Abort()
