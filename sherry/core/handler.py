# encoding=utf-8
"""
    create by pymu
    on 2021/5/12
    at 15:29
"""
import logging
import sys
import traceback

from sherry.view.activity.activity_dialog import NormalDialogActivity


class ExOperational:
    """异常操作类型"""

    title = "运行异常"  # Note: 标题， title
    description = "未知异常, "  # Note: 异常描述, Exception description
    callback = None  # Note: 回调，callback
    log_level = logging.ERROR  # Note: 日志等级, logging level
    log_it = True  # Note: 是否记录日志，默认记录, Whether to record the log, the default record

    exc_type = None  # Note: 触发的异常类型，Type of exception triggered
    exc_value = None  # Note: 异常类， Exception class
    tb = None  # Note: 栈回溯，Stack traceback

    def __init__(self, description="未知异常", title="错误", callback=None,
                 log_level=logging.ERROR, log_it=True):
        """
        初始化有一个异常操作类型,在异常触发时调用
        Initialization has an exception operation type,
        which is called when the exception is triggered

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

    def __repr__(self):
        return """ExOperational( title: {}, description: {}, log_level: {}, log_it: {} )""".format(self.title,
                                                                                                   self.description,
                                                                                                   self.log_level,
                                                                                                   self.log_it)


class ExceptHookHandler:
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
        # noinspection SpellCheckingInspection
        sys.excepthook = self.__exception

    def update_map(self, d):
        """
        更新异常映射
        update exception mapping
        """
        self.ex_map.update(d)

    @staticmethod
    def log(exc_type, exc_value, tb):
        msg = ' Traceback (most recent call last):\n'
        while tb:
            filename = tb.tb_frame.f_code.co_filename
            name = tb.tb_frame.f_code.co_name
            lineno = tb.tb_lineno
            msg += '   File "%.500s", line %d, in %.500s\n' % (filename, lineno, name)
            tb = tb.tb_next
        msg += ' %s: %s\n' % (exc_type.__name__, exc_value)
        return msg

    def __exception(self, exc_type, exc_value, tb):
        """
        分为两个部分：part of this：
            - 日志记录：写到日志文件中， log record
            - 弹窗提示，除了日志无感记录之外，出现未记录的异常应该提示给用户
        :param exc_type: 异常对象
        :param exc_value: 异常信息
        :param tb: 栈回溯
        """
        op = self.ex_map.get(exc_type.__name__, ExOperational(description="%s: \n%s" % (exc_type.__name__, exc_value)))
        if op.log_it:
            msg = self.log(exc_type, exc_value, tb)
            logging.getLogger().log(op.log_level, "{msg}".format(msg=msg))
        try:
            if op.callback:
                op.exc_value = exc_value
                op.exc_type = exc_type
                op.tb = tb
                op.callback(op)
        except Exception as e:
            traceback_rollback = traceback.format_exc()
            traceback_rollback = f"{str(e)}" if str(
                traceback_rollback) == "NoneType: None\n" else traceback_rollback
            logging.getLogger().error(traceback_rollback)
        dialog = NormalDialogActivity(title=op.title, info=op.description)
        dialog.setWindowTitle(op.title)
        dialog.exec()
