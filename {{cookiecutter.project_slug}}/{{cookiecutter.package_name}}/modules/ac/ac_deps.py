from functools import lru_cache
from os import path

from casbin import Enforcer
from fastapi import Depends, HTTPException, Request

from {{cookiecutter.package_name}}.config import settings
from {{cookiecutter.package_name}}.modules.users.users_deps import get_current_user
from {{cookiecutter.package_name}}.modules.users.users_models import User


@lru_cache
def get_enforcer() -> Enforcer:
    dir_ = path.dirname(__file__)
    return Enforcer(
        path.join(dir_, "ac_model.conf"),
        path.join(dir_, "ac_policies.csv"),
    )


def get_authorized_user(
    req: Request,
    enforcer: Enforcer = Depends(get_enforcer),
    me: User = Depends(get_current_user),
) -> User:
    sub = me.role
    obj = req.url.path.removeprefix(settings.root_path)
    act = req.method
    if enforcer.enforce(sub, obj, act):
        return me
    raise HTTPException(status_code=403, detail="Forbidden")
