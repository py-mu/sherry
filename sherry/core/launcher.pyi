# coding=utf-8
"""
    create by pymu
    on 2021/5/6
    at 17:35
    默认的启动类，其实就是常用的全局设定
"""
from typing import Optional, Type

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.core.handler import AbnormalMap


class Application:
    socket: QLocalSocket
    localServer = QLocalServer
    activity: Optional[Type[QWidget]]
    args = ()
    kwargs = {}
    unique: bool

    def __init_before__(self): ...

    def __init__(self, *args, activity_: Optional[Type] = None, unique_: bool = False, **kwargs): ...

    def __init_app(self): ...

    @staticmethod
    def abnormal_dialog(op: AbnormalMap): ...

    def run(self): ...

    def shutdown(self): ...
