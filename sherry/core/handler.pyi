import logging
from types import TracebackType
from typing import Callable, Optional, Dict


class ExOperational:
    title: str
    description: str
    callback: Optional[Callable]
    log_level: int
    log_it: bool

    exc_type: type
    exc_value: BaseException
    tb: TracebackType

    def __init__(
            self,
            description: str = "未知异常",
            title: str = "程序异常",
            callback: Optional[Callable] = None,
            log_level: int = logging.ERROR,
            log_it: bool = True
    ): ...


class ExceptHookHandler:
    ex_map: Dict[str, ExOperational]

    def update_map(self, d: Dict[str, ExOperational]): ...

    @staticmethod
    def log(exc_type: type, exc_value: BaseException, tb: TracebackType): ...
    def __exception(self, exc_type: type, exc_value: BaseException, tb: TracebackType):...
