# encoding=utf-8
"""
    create by pymu
    on 2021/5/12
    at 15:29
"""
import json
import logging
import sys


class AbnormalMap:
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
        self.log_level = log_level
        self.log_it = log_it
        self.title = title
        self.callback = callback

    def __repr__(self):
        return """ExOperational( title: {}, description: {}, log_level: {}, log_it: {} )""".format(self.title,
                                                                                                   self.description,
                                                                                                   self.log_level,
                                                                                                   self.log_it)


class AbnormalHookHandler:
    """
    异常拦截类

    Exception Interception Handler
    """
    ex_map = {}
    __default_call_func = None

    def __init__(self):
        """
        全局异常处理，包含属性： this include：
            - logger：日志 Log
            - exception：异常回溯 Exception traceback
        """
        # noinspection SpellCheckingInspection
        setattr(sys, 'excepthook', self.__exception)

    def update_map(self, d):
        """
        更新异常映射
        update exception mapping
        """
        self.ex_map.update(d)

    def update_json(self, json_path, encoding='utf-8'):
        with open(json_path, encoding=encoding) as f:
            self.update_map({k: AbnormalMap(**v) for k, v in json.load(f).items()})

    def set_default_callback(self, func):
        self.__default_call_func = func

    def __exception(self, exc_info, exc_value, tb):
        """
        分为两个部分：part of this：
            - 日志记录：写到日志文件中， log record
            - 弹窗提示，除了日志无感记录之外，出现未记录的异常应该提示给用户
        :param exc_info: 异常对象
        :param exc_value: 异常信息
        :param tb: 栈回溯
        """
        op = self.ex_map.get(exc_info.__name__, AbnormalMap(description="%s: \n%s" % (exc_info.__name__, exc_value)))
        if op.log_it:
            logging.exception('未拦截异常', exc_info=(exc_info, exc_value, tb))
        call_func = op.callback or self.__default_call_func
        if call_func:
            op.exc_value = exc_value
            op.exc_type = exc_info
            op.tb = tb
            call_func(op)
