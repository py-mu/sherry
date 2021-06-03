from typing import Any, Callable

from PyQt5.QtCore import QThread, pyqtSignal


class Response:
    code: int
    task_id: str
    data: Any

    def __init__(self, code=0, task_id='', data=None): ...


class Worker(QThread):
    __success = pyqtSignal(Response)
    __error = pyqtSignal(Response)
    __end = pyqtSignal(Response)
    __is_working: bool = False

    @property
    def success(self) -> pyqtSignal(Response): ...

    @property
    def error(self) -> pyqtSignal(Response): ...

    @property
    def end(self) -> pyqtSignal(Response): ...

    @property
    def running(self) -> pyqtSignal(Response): ...

    def strike(self, response: Response = None): ...

    def set_func(self, func: Callable, task_id=None, *args, **kwargs): ...

    def kill(self) -> None: ...

    def run(self) -> None: ...
