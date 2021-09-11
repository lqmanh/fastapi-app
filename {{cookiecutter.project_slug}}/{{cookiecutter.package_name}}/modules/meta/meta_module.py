from fastapi_module import module

from .meta_controller import MetaController


@module("/meta", controllers=(MetaController,))
class MetaModule:
    ...
