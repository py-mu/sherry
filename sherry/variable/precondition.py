# coding=utf-8
"""
    create by pymu
    on 2021/6/25
    at 23:18
"""

from sherry import __name__, __version__, __author__
from sherry.core.badge import Badge
from sherry.core.handler import AbnormalHookHandler
from sherry.core.injector import CursorAgent, PropertyAgent
from sherry.core.paths import SherryPath
from sherry.inherit.style import ElementStyle
from sherry.utils.log import LoggerSetter

app_name = __name__  # Note: 应用名称 app name.
author = __author__  # Note: 作者 app author.
app_version = __version__  # Note: 版本 app version.

log_file = "log/{}.log".format(app_name)  # Note: 日志文件路径 log file path.
base_qss = "element.css"  # Note: 默认使用的主题 base theme.
base_font = 'element.ttf'
base_style = ElementStyle()  # Note: 默认的style, base style.
# if debug
DEBUG = True

# run before
# 在部分使用badge注入的类，在程序没有扫描到的子类，是不会生效的
# 此时需要在程序运行伊始手动导入，这样装载子类时才会生效
# todo 希望能添加自动扫描(先存储一个路径列表，然后进行遍历导入，失败则跳过，直到只剩一条就抛出异常)
import_lib_before = [
    'sherry.view.digital.digital_activity_simple_theme',
    'sherry.view.decoration.decoration_base_bar',
    'sherry.view.decoration.decoration_activity_dialog',
    'sherry.view.decoration.decoration_activity_welcome',
    'sherry.view.decoration.decoration_activity_simple_theme',
    'sherry.view.decoration.decoration_activity_example_designer',
    'sherry.view.decoration.decoration_activity_about',

    'sherry.view.signal.signal_activity_dialog',
    'sherry.view.signal.signal_activity_simple_theme',
    'sherry.view.signal.signal_activity_welcome',
]

# 部分需要框架初始化结束后才能进行装载的衍生类
import_lib_after = []


def set_exception_mapping():
    json_path = Badge(source=SherryPath, singleton=True).file_path('sherry/exception-handler.json')
    Badge(source=AbnormalHookHandler, singleton=True).update_json(json_path)


# 执行任务列表
TaskDispatcher = {
    "project_path": SherryPath,
    "logger": (LoggerSetter, (log_file,), {"singleton": True}),
    "qt_cursor_agent": CursorAgent,
    "qt_property_agent": PropertyAgent,
    "abnormal_interceptor": AbnormalHookHandler,
    "set_exception_mapping": set_exception_mapping,
}
