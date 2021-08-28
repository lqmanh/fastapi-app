from enum import Enum


class Role(str, Enum):
    ROOT = "root"
    ADMIN = "admin"
    END_USER = "end-user"
