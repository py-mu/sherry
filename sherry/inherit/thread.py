# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 16:27
"""
import logging
import uuid

from PyQt5.QtCore import QThread, pyqtSignal


class Response:
    code = 0
    task_id = None
    data = None

    def __init__(self, code=0, task_id='', data=None):
        self.code = code
        self.task_id = task_id or uuid.uuid4().hex
        self.data = data


class Worker(QThread):
    """
    使用示例：
        # 在activity 类中声明一个func thread

        self.delete_file_func = Worker()

        # 为线程信号绑定槽

        self.delete_file_func.thread_signal.connect(....)    # 正常通信频道
        self.delete_file_func.thread_error_signal.connect(....)    # 异常通信频道

    """
    # 正常通信信号
    __success = pyqtSignal(Response)
    # 异常通信信号
    __error = pyqtSignal(Response)
    # 终止信号
    __end = pyqtSignal(Response)
    # 是否在运行
    __is_working = False

    @property
    def success(self):
        return self.__success

    @property
    def error(self):
        return self.__error

    @property
    def end(self):
        return self.__end

    @property
    def running(self):
        return self.__is_working

    def strike(self, response=None):
        """
        手动激发
        :param response:
        :return:
        """
        # noinspection PyUnresolvedReferences
        self.end.emit(response or Response())

    def __init__(self):
        super().__init__()
        self.func = None
        self._id = uuid.uuid4().hex
        self.func_args = []
        self.func_kwargs = {}
        # noinspection PyUnresolvedReferences
        self.success.connect(lambda: None)
        # noinspection PyUnresolvedReferences
        self.error.connect(lambda: None)

    def set_func(self, func, task_id=None, *args, **kwargs):
        self.func_args = list(args)
        self.func_kwargs = kwargs
        self.func = func
        self._id = task_id
        logging.info("设置线程 func={}  arg={}  kwargs={}".format(func.__name__, args, kwargs))

    def kill(self):
        self.__is_working = False
        self.terminate()

    def run(self):
        self.__is_working = True
        response = Response()
        response.task_id = self._id
        if not self.func:
            return
        try:
            result = self.func(*self.func_args, **self.func_kwargs)
            response.data = result
            self.thread_signal.emit(response)
        except Exception as e:
            response.code = 1
            response.data = e
            # noinspection PyUnresolvedReferences
            self.error.emit(response)
            logging.exception("执行失败 func={}  arg={}  kwargs={}, error={}".format(self.func.__name__,
                                                                                 self.func_args,
                                                                                 self.func_kwargs,
                                                                                 e))
        finally:
            # noinspection PyUnresolvedReferences
            self.end.emit(response)
        self.__is_working = False
