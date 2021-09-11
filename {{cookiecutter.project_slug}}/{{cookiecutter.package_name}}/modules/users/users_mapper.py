from .users_dtos import UserRead
from .users_models import User


class UsersMapper:
    def to_user_read(self, user: User) -> UserRead:
        return UserRead(
            id=user.id,
            role=user.role,
            username=user.username,
        )
