from functools import lru_cache
from os import path

from casbin import Enforcer
from fastapi import Depends, HTTPException, Request

from {{cookiecutter.package_name}}.modules.users.users_deps import get_current_active_user
from {{cookiecutter.package_name}}.modules.users.users_models import User


@lru_cache
def get_enforcer() -> Enforcer:
    dirname = path.dirname(__file__)
    return Enforcer(
        path.join(dirname, "ac_model.conf"),
        path.join(dirname, "ac_policies.csv"),
    )


def get_authorized_user(
    req: Request,
    enforcer: Enforcer = Depends(get_enforcer),
    user: User = Depends(get_current_active_user),
) -> User:
    actor = user.id
    action = req.method
    resource = req.url.path
    if enforcer.enforce(actor, action, resource):
        return user
    raise HTTPException(status_code=403, detail="Forbidden")
