# coding=utf-8
"""
    create by pymu
    on 2021/6/25
    at 23:18
"""
import sys

from PyQt5.QtWidgets import QApplication

from sherry import __name__, __version__, __author__
from sherry.utls.log import LoggerSetter

# 应用名称 app name.
app_name = __name__
# 作者 app author.
author = __author__
# 版本 app version.
app_version = __version__
# QT app
app = QApplication.instance() or QApplication(sys.argv)

# if debug
DEBUG = True

# logger
logger_setter = LoggerSetter
logger_setter.log_name = app_name

# run before
import_lib = []
