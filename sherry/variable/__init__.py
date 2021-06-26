# coding=utf-8
"""
    create by pymu
    on 2021/4/30
    at 17:11
"""
import logging

try:
    from precondition import *
except ImportError as e:
    from sherry.variable.precondition import *

from sherry.extends.override import Overrider
from sherry.core.badge import Badge

# import custom class
for lib in import_lib:
    try:
        __import__(lib)
    except ImportError as e:
        logging.exception("can't import module '{}'. ".format(lib))

# set logger
logger_setter()

# debug log

if DEBUG:
    logging.root.setLevel(logging.DEBUG)

# qt override
override_class = Badge(source=Overrider)
override_class.install()
