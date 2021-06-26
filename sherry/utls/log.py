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

import colorlog


class ApplicationLogger(logging.Logger):
    root_path = 'log'

    def __init__(self, name: str):
        super().__init__(name)
        self.level = logging.INFO
        self.set_handler(name)

    def set_handler(self, name):
        if not os.path.exists(self.root_path):
            os.mkdir(self.root_path)
        file_path = os.path.join(self.root_path, name)
        handler = RotatingFileHandler(filename=file_path,
                                      maxBytes=20 * 1024 * 1024,
                                      backupCount=5, encoding='utf-8')
        _format = logging.Formatter(
            fmt="%(asctime)s - %(module)s - %(funcName)s：%(lineno)d  -  %(levelname)s: %(message)s",
            datefmt='%Y-%m-%d %H:%M:%S %a')
        handler.setLevel(logging.INFO)
        handler.setFormatter(_format)

        self.addHandler(handler)

    def error(self, msg, *args, exc_info=None, stack_info=None, level=None, extra=None, **kwargs):
        if self.isEnabledFor(logging.ERROR):
            traceback_rollback = traceback.format_exc()
            traceback_rollback = (" 无可视异常栈：" + str(exc_info)) if str(
                traceback_rollback) == f"NoneType: None\n" else traceback_rollback
            msg = str(msg) + traceback_rollback
            self._log(logging.ERROR, msg, args, **kwargs)


class LoggerSetter:
    """日志设置"""
    log_name = 'sherry'
    log_class = ApplicationLogger
    handlers = []

    def __init__(self):
        self.set_root_log()
        self.init_handler()
        self.add_handler()

    def set_root_log(self):
        """设置默认的日志来源"""
        logging.setLoggerClass(self.log_class)
        logging.root = self.log_class("{}.log".format(self.log_name))

    def init_handler(self):
        """"""
        self.handlers.append(self.TerminalHandler())
        # self.handlers.append(self.InterceptHandler())

    def add_handler(self):
        """添加handler"""
        for handler in self.handlers:
            logging.root.addHandler(handler)

    class TerminalHandler(logging.StreamHandler):
        """终端输出"""

        def __init__(self):
            super().__init__()
            self.formatter = colorlog.ColoredFormatter(
                fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
                datefmt='%Y-%m-%d  %H:%M:%S',
            )
            self.level = logging.DEBUG

    # class InterceptHandler(logging.Handler):
    #     """
    #     more read: https://github.com/Delgan/loguru
    #     """
    #     def emit(self, record):
    #         # Get corresponding Loguru level if it exists
    #         try:
    #             level = logger.level(record.levelname).name
    #         except ValueError:
    #             level = record.levelno
    #
    #         # Find caller from where originated the logged message, 查找来自记录消息的来源的呼叫者
    #         frame, depth = logging.currentframe(), 2
    #         while frame.f_code.co_filename == logging.__file__:
    #             frame = frame.f_back
    #             depth += 1
    #
    #         logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
