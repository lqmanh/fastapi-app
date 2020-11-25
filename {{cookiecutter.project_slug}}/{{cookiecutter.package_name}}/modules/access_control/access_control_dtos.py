from {{cookiecutter.package_name}}.common.utils import create_pydantic_models
from {{cookiecutter.package_name}}.modules.access_control.access_control_models import (
    Action,
    Permission,
    Resource,
    Role,
)


PermissionCreate, PermissionRead, *_ = create_pydantic_models(Permission)

RoleCreate, RoleRead, *_ = create_pydantic_models(Role)

ResourceCreate, ResourceRead, *_ = create_pydantic_models(Resource)

ActionCreate, ActionRead, *_ = create_pydantic_models(Action)
