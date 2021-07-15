# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
from typing import List, Callable

__all__ = ('WidgetInjector', 'register')
instance_func: List[Callable[[], None]] = []


def register(func: Callable[[], None]): ...


class WidgetInjector:

    @staticmethod
    def __install(): ...
