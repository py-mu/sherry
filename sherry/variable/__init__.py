# coding=utf-8
"""
    create by pymu
    on 2021/4/30
    at 17:11
"""
import logging
import os
from inspect import isfunction, isclass

from sherry.core.badge import Badge
from sherry.variable.precondition import *

try:
    from precondition import *
except ImportError:
    pass

if not os.path.exists(os.path.dirname(log_file)):
    os.mkdir(os.path.dirname(log_file))
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG if DEBUG else logging.INFO
)

for lib in import_lib_before:
    try:
        __import__(lib)
    except ImportError as e:
        logging.exception("can't import module '{}'. ".format(lib))

# 回调
for call_object in TaskDispatcher.values():
    if not call_object:
        continue
    args = ()
    kwargs = {}
    call_cls = None
    if isinstance(call_object, tuple):
        call_cls = call_object[0]
        if len(call_object) > 1:
            for i in call_object[1:]:
                if isinstance(i, tuple):
                    args = i
                elif isinstance(i, dict):
                    kwargs = i
    if not call_cls:
        continue

    if isclass(call_cls):
        Badge(*args, source=call_cls, **kwargs)
    elif isfunction(call_cls):
        call_cls(*args, **kwargs)
    else:
        logging.warning("未知数据类型 {} ".format(call_object))
