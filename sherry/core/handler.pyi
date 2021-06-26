# encoding=utf-8
"""
    create by pymu
    on 2021/5/12
    at 15:29
"""
import logging
import traceback
from typing import Callable, Optional, Type


class ExOperational:
    title: str
    description: str
    callback: Optional[Callable]
    log_level: int
    log_it: bool
    exc_type: Optional[Type[BaseException]]
    exc_value: Optional[BaseException]
    tb: Optional[traceback]

    def __init__(self,
                 description: str = "未知异常",
                 title: str = "错误",
                 callback: Optional[Callable] = None,
                 log_level: int = logging.ERROR,
                 log_it: bool = True): ...

    @staticmethod
    def callback_fun(op: ExOperational): ...

    def __repr__(self): ...


class ExceptHookHandler:
    ex_map = {}

    def __init__(self): ...

    def update_map(self, d: dict): ...

    def __exception(self, exc_info: Optional[Type[BaseException]], exc_value: Optional[BaseException], tb: traceback):
        ...
