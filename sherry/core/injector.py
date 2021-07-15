# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
from __future__ import print_function

import functools

__all__ = ('WidgetInjector', 'register')
instance_func = []


def register(func):
    """注册方法"""

    instance_func.append(func)

    @functools.wraps(func)
    def warps():
        return func()

    return warps


class WidgetInjector:

    def __init__(self):
        self.__install()

    @staticmethod
    def __install():
        for func in instance_func:
            func()
