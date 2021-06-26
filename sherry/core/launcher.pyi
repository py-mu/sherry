# coding=utf-8
"""
    create by pymu
    on 2021/5/6
    at 17:35
    默认的启动类，其实就是常用的全局设定
"""
from typing import Optional

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.core.handler import ExceptHookHandler


class Application:
    socket: QLocalSocket
    localServer = QLocalServer
    activity: QWidget
    handler: ExceptHookHandler
    unique: bool

    def __init_before__(self): ...

    def __init__(self, activity: Optional[QWidget] = None, unique: bool = False): ...

    def refresh_ex_data(self, file_path: str): ...

    @staticmethod
    def __init_app(): ...

    def run(self): ...

    def shutdown(self): ...
