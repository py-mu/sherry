# coding=utf-8
"""
    create by pymu on 2020/5/7
    package: .logger.py
    project:
"""

import logging
import os
import traceback
from logging.handlers import RotatingFileHandler


class ApplicationLogger(logging.Logger):
    root_path = ''
    app_name = 'sherry'

    def __init__(self, name: str = None):
        name = name or ApplicationLogger.app_name
        super().__init__(name)
        self.level = logging.DEBUG
        self.set_handler(name)

    def set_handler(self, name):
        file_path = os.path.join(self.root_path, name)
        handler = RotatingFileHandler(filename=file_path,
                                      maxBytes=20 * 1024 * 1024,
                                      backupCount=5, encoding='utf-8')
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter(
            fmt="%(asctime)s - %(module)s - %(funcName)s：%(lineno)d  -  %(levelname)s: %(message)s",
            datefmt='%Y-%m-%d %H:%M:%S %a')
        )
        self.addHandler(handler)

    def error(self, msg, *args, exc_info=None, stack_info=None, level=None, extra=None, **kwargs):
        if self.isEnabledFor(logging.ERROR):
            traceback_rollback = traceback.format_exc()
            traceback_rollback = (" 无可视异常栈：" + str(exc_info)) if str(
                traceback_rollback) == f"NoneType: None\n" else traceback_rollback
            msg = str(msg) + traceback_rollback
            self._log(logging.ERROR, msg, args, **kwargs)
