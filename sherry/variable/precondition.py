# coding=utf-8
"""
    create by pymu
    on 2021/6/25
    at 23:18
"""
import sys

from PyQt5.QtWidgets import QApplication

from sherry import __name__, __version__, __author__
from sherry.core.badge import Badge
from sherry.core.handler import AbnormalHookHandler
from sherry.core.paths import SherryPath
from sherry.core.injector import WidgetInjector
from sherry.utils.log import LoggerSetter

app_name = __name__  # Note: 应用名称 app name.
author = __author__  # Note: 作者 app author.
app_version = __version__  # Note: 版本 app version.
app = QApplication.instance() or QApplication(sys.argv)  # QT app

# if debug
DEBUG = True

# run before
# 在部分使用badge注入的类，在程序没有扫描到的子类，是不会生效的
# 此时需要在程序运行伊始手动导入，这样装载子类时才会生效
import_lib = []


def set_exception_mapping():
    json_path = Badge(source=SherryPath).file_path('sherry/exception-handler.json')
    Badge(source=AbnormalHookHandler).update_json(json_path)


# 执行任务列表
TaskDispatcher = {
    "project_path": (SherryPath, (), {}),
    "logger": (LoggerSetter, (app_name, ), {}),
    "qt_injector": (WidgetInjector, (), {}),
    "abnormal_interceptor": (AbnormalHookHandler, (), {}),
    "set_exception_mapping": (set_exception_mapping, (), {}),
}
