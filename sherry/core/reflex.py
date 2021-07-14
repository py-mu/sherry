# coding=utf-8
"""
    create by pymu
    on 2021/7/13
    at 22:16
"""
import logging


class ReflexCenter:
    """反射神经中枢，检测所有的反射对象及反射路径，同时记录被反射对象"""

    __hook_dict__ = {}
    hook_log = False

    @staticmethod
    def hook(target, path, obj):
        if hasattr(target, path):
            ReflexCenter.__hook_dict__.setdefault(str(target) + path, getattr(target, path))
        if ReflexCenter.hook_log:
            logging.debug('hook %s at %s <-- %s' % (target, path, obj))
        setattr(target, path, obj)
