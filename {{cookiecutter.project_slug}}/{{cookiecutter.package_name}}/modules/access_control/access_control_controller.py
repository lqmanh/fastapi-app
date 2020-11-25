from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from {{cookiecutter.package_name}}.modules.access_control.access_control_service import AccessControlService


router = InferringRouter()


@cbv(router)
class AccessControlController:
    ac_service: AccessControlService = Depends()
