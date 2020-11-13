import asyncio
import functools
from typing import Callable

import typer
from typer import Typer


def _coro(f: Callable):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


app = Typer()


@app.command()
@_coro
async def ping():
    await asyncio.sleep(1)
    typer.echo("PONG")

