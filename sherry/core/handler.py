# encoding=utf-8
"""
    create by pymu
    on 2021/5/12
    at 15:29
"""
import logging
import sys
import traceback
from typing import Callable


class ExOperational:
    """异常操作类型"""

    title = "程序异常"  # Note: 标题， title
    description = "未知异常, "  # Note: 异常描述, Exception description
    callback: Callable = None  # Note: 回调，callback
    log_level: int = logging.ERROR  # Note: 日志等级, logging level
    log_it = True  # Note: 是否记录日志，默认记录, Whether to record the log, the default record

    exc_type: type  # Note: 触发的异常类型，Type of exception triggered
    exc_value: BaseException  # Note: 异常类， Exception class
    tb: traceback  # Note: 栈回溯，Stack traceback

    def __init__(self, description: str = "未知异常", title: str = "程序异常", callback: Callable = None,
                 log_level: int = logging.ERROR, log_it: bool = True):
        """
        初始化有一个异常操作类型,在异常触发时调用
        Initialization has an exception operation type, which is called when the exception is triggered

        :param description: 异常描述 Exception description
        :param title: 标题 dialog title
        :param callback: 回调，即触发该异常时进行回调 callback， default：None
        :param log_level: 异常等级，根据等级显示弹窗的等级 log level， default：logging.ERROR
        :param log_it: 是否做日志记录， 默认是 Whether to log，default：True
        """
        self.description = description
        self.callback = callback
        self.log_level = log_level
        self.log_it = log_it
        self.title = title


class ApplicationHandler:
    """
    异常拦截类

    Exception Interception Handler
    """
    ex_map = {}

    def __init__(self):
        """
        全局异常处理，包含属性： this include：
            - logger：日志 Log
            - exception：异常回溯 Exception traceback
        """
        self.logger = logging.Logger('system_error')
        # noinspection SpellCheckingInspection
        sys.excepthook = self.exception

    def update_map(self, d: dict):
        """
        更新异常映射
        update exception mapping
        """
        self.ex_map.update(d)

    @staticmethod
    def log(exc_type: type, exc_value: BaseException, tb: traceback):
        msg = ' Traceback (most recent call last):\n'
        while tb:
            filename = tb.tb_frame.f_code.co_filename
            name = tb.tb_frame.f_code.co_name
            lineno = tb.tb_lineno
            msg += '   File "%.500s", line %d, in %.500s\n' % (filename, lineno, name)
            tb = tb.tb_next
        msg += ' %s: %s\n' % (exc_type.__name__, exc_value)
        return msg

    def exception(self, exc_type: type, exc_value: BaseException, tb: traceback):
        """
        分为两个部分：part of this：
            - 日志记录：写到日志文件中， log record
            - 弹窗提示，除了日志无感记录之外，出现未记录的异常应该提示给用户
        :param exc_type: 异常对象
        :param exc_value: 异常信息
        :param tb: 栈回溯
        """
        op = self.ex_map.get(exc_type.__name__, ExOperational())
        if op.log_it:
            msg = self.log(exc_type, exc_value, tb)
            self.logger.log(op.log_level, f"{msg}")
        if not op.callback:
            return
        try:
            op.exc_value = exc_value
            op.exc_type = exc_type
            op.tb = tb
            op.callback(op)
        except Exception as e:
            traceback_rollback = traceback.format_exc()
            traceback_rollback = f"{str(e)}" if str(
                traceback_rollback) == "NoneType: None\n" else traceback_rollback
            self.logger.error(traceback_rollback)
