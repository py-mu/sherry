# coding=utf-8
"""
    create by pymu
    on 2021/6/25
    at 23:18
"""
import sys

from PyQt5.QtWidgets import QApplication

from sherry import __name__, __version__, __author__

# 应用名称 app name.
from sherry.utls.log import ApplicationLogger

app_name = __name__
# 作者 app author.
author = __author__
# 版本 app version.
app_version = __version__

app = QApplication.instance() or QApplication(sys.argv)

# 全局logger
# 使用 loguru：
#
# from loguru import logger as log_record
# logger = log_record
# logger = logger.add('log/{}.log'.format(app_name), rotation="5 MB")
#
# more read: https://github.com/Delgan/loguru
logger = ApplicationLogger(app_name)
