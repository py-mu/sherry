# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 16:27
"""
from typing import Optional, Callable

from qtpy.QtCore import QThread, pyqtSignal


class Response:
    code: int
    task_id: str
    data: Optional[object]

    def __init__(self, code: int = 0, task_id: str = '', data: Optional[object] = None): ...


class Worker(QThread):
    __success: pyqtSignal
    __error: pyqtSignal
    __end: pyqtSignal
    __is_working: bool

    @property
    def success(self) -> pyqtSignal: ...

    @property
    def error(self) -> pyqtSignal: ...

    @property
    def end(self) -> pyqtSignal: ...

    @property
    def running(self) -> bool: ...

    def strike(self, response: Optional[Response] = None): ...

    def set_func(self, func: Callable, task_id: Optional[str] = None, *args, **kwargs): ...

    def kill(self): ...
