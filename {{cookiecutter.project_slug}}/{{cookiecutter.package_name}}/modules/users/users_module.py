from fastapi_module import module

from .users_controller import UsersController


@module("/users", controllers=(UsersController,))
class UsersModule:
    ...
