from fastapi_module import module

from .users_controller import UsersController


@module(controllers=(UsersController,))
class UsersModule:
    ...
