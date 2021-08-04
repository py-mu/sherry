# coding=utf-8
"""
    create by pymu
    on 2021/5/6
    at 17:35
    默认的启动类，其实就是常用的全局设定
"""
from typing import Type, Union

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.core.handler import AbnormalMap
from sherry.core.resource import ResourceLoader


class Application:
    resource: ResourceLoader
    socket: QLocalSocket
    localServer = QLocalServer
    activity: Union[Type[QWidget], None, QWidget]
    args = ()
    kwargs = {}
    unique: bool

    def __init_before__(self): ...

    def __init__(self, *args, activity: Union[Type[QWidget], None, QWidget] = None, unique: bool = False, **kwargs): ...

    def __init_app(self): ...

    @staticmethod
    def abnormal_dialog(op: AbnormalMap): ...

    def run(self): ...

    def shutdown(self): ...
