# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
from typing import List, Callable, Type

__all__ = ('WidgetInjector', 'register')
__instance_func__: List[Callable] = []

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QWidget


def register(func: Callable): ...


class WidgetInjector:

    @staticmethod
    def _register_tooltip(obj: Type[QWidget]) -> Callable[[QWidget, QEvent], bool]: ...

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
    def __install(): ...
