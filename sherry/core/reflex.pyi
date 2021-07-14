# coding=utf-8
"""
    create by pymu
    on 2021/7/13
    at 22:16
"""
from typing import Union


class ReflexCenter:
    """反射神经中枢，检测所有的反射对象及反射路径，同时记录被反射对象"""

    __hook_dict__ = {}
    hook_log = True

    @staticmethod
    def hook(target: Union[type, object], path: str, obj): ...
