# coding=utf-8
"""
    create by pymu
    on 2021/4/30
    at 17:11
"""
import logging
from inspect import isfunction, isclass

from sherry.core.badge import Badge
from sherry.variable.precondition import *

try:
    from precondition import *
except ImportError:
    pass

logging.basicConfig(
    filename="{}.log".format(app_name),
    level=logging.DEBUG if DEBUG else logging.INFO
)

for lib in import_lib_before:
    try:
        __import__(lib)
    except ImportError as e:
        logging.exception("can't import module '{}'. ".format(lib))

# 回调
for call_object, args, kwargs in TaskDispatcher.values():
    if not call_object:
        continue
    if isclass(call_object):
        Badge(*args, source=call_object, **kwargs)
    elif isfunction(call_object):
        call_object(*args, **kwargs)
    else:
        logging.warning("未知数据类型 {} ".format(call_object))
