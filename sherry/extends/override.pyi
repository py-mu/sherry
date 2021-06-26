# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
from typing import List, Callable

from sherry.extends.events import EventCell

__all__ = ('Overrider', 'register')
__instance_func__: List[Callable] = []


def register(func: Callable): ...


class Overrider:
    custom_events: List[EventCell]

    @staticmethod
    @register
    def install_events(): ...

    @staticmethod
    @register
    def install_enter_event(): ...

    @staticmethod
    @register
    def install_leave_event(): ...

    #  设置动态修改属性会重载样式
    @staticmethod
    @register
    def install_set_property(): ...

    @staticmethod
    def install(): ...
