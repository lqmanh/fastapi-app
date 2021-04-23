from .users_dtos import UserRead
from .users_models import User


def user_to_user_read(user: User) -> UserRead:
    user_read = UserRead(
        id=user.id,
        username=user.username,
        is_active=user.is_active,
        role=user.role,
    )
    return user_read
