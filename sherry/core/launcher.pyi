from logging import Logger
from typing import Type

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.common.logger import ApplicationLogger
from sherry.core.config import ApplicationConfig
from sherry.core.handler import ExceptHookHandler
from sherry.core.resource import ResourceLoader


class Application:
    config: ApplicationConfig
    activity: QWidget
    handler: ExceptHookHandler
    unique: bool
    log_class: Type[ApplicationLogger]
    localServer: QLocalServer
    socket: QLocalSocket
    logger: Logger
    resource: ResourceLoader

    def __init__(self,
                 config: ApplicationConfig = None,
                 activity: QWidget = None,
                 handler: ExceptHookHandler = None,
                 log_class: Type[ApplicationLogger] = None,
                 unique: bool = False
                 ): ...

    def __set_logger(self, logger_class: Type[ApplicationLogger]): ...

    def refresh_ex_data(self, file_path: str = ''): ...

    def run(self): ...

    def shutdown(self): ...