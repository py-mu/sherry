# encoding=utf-8
"""
    create by pymu
    on 2021/5/12
    at 15:29
"""
import logging
import traceback
from typing import Callable, Optional, Type, Dict


class AbnormalMap:
    title: str
    description: str
    callback: Optional[Callable[[AbnormalMap], None]]
    log_level: int
    log_it: bool
    exc_type: Optional[Type[BaseException]]
    exc_value: Optional[BaseException]
    tb: Optional[traceback]

    def __init__(self,
                 description: str = "未知异常",
                 title: str = "错误",
                 callback: Optional[Callable[[AbnormalMap], None]] = None,
                 log_level: int = logging.ERROR,
                 log_it: bool = True): ...

    def __repr__(self): ...


class AbnormalHookHandler:
    ex_map = {}
    __default_call_func: Callable[[AbnormalMap], None]

    def __init__(self): ...

    def update_map(self, d: Dict[str, AbnormalMap]): ...
    def update_json(self, json_path: str): ...

    def set_default_callback(self, func: Callable[[AbnormalMap], None]): ...

    def __exception(self, exc_info: Optional[Type[BaseException]], exc_value: Optional[BaseException], tb: traceback):
        ...
