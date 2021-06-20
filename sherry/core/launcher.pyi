from typing import Type

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.common.logger import ApplicationLogger
from sherry.core.config import ApplicationConfig
from sherry.core.handler import ExceptHookHandler
from sherry.extends.override import Overrider


class Application:
    config: ApplicationConfig
    activity: Type[QWidget]
    handler: ExceptHookHandler
    unique: bool
    log_class: Type[ApplicationLogger]
    localServer: QLocalServer
    socket: QLocalSocket
    override_class: Type[Overrider]
    err_desc_file_path: str

    def __before__(self): ...

    def set_properties(self, *args, **kwargs): ...

    def __init__(self,
                 activity: Type[QWidget] = None,
                 config: ApplicationConfig = None,
                 handler: ExceptHookHandler = None,
                 log_class: Type[ApplicationLogger] = None,
                 unique: bool = False,
                 override_class: Type[Overrider] = None,
                 err_desc_file_path: str = ''
                 ): ...

    def procedure(self): ...

    def __set_logger(self, logger_class: Type[ApplicationLogger]): ...

    def refresh_ex_data(self, file_path): ...

    def __init_app(self): ...

    def run(self): ...

    def shutdown(self): ...
