def check_username(username: str) -> str:
    if not 4 <= len(username) <= 32:
        raise ValueError("must be at least 4 and no more than 32 characters long")
    return username


def check_password(password: str) -> str:
    if not 8 <= len(password) <= 32:
        raise ValueError("must be at least 8 and no more than 32 characters long")
    return password
