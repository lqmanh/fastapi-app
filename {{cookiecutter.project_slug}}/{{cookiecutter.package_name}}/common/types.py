from enum import Enum


class CrudMethod(str, Enum):
    Create = "create"
    Read = "read"
    Update = "update"
    Delete = "delete"

