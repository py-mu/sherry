# coding=utf-8
"""
    create by pymu on 2020/5/7
    package: .logger.py
    project:
"""

import datetime
import logging
import os
import re

description = "日志信息"
__root_path__ = os.getcwd()
LOG_PATH = os.path.join(__root_path__, "log")

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)


class Logger(logging.Logger):
    """
    初始化一个日志器，并设置默认的文件名为 system， 记录等级为 info
    """

    def __init__(self, name='system_default_log', level=logging.INFO):
        super().__init__(name, level)
        self.level = level
        self.name = name
        self.__set_log_handler()

    def __set_log_handler(self):
        """
        日志输出格式及输出等级,默认为INFO, 回滚
        :return:
        """
        main_handler = MyLoggerHandler(filename=self.name, when='D', backup_count=5,
                                       encoding="utf-8")
        error_handler = MyLoggerHandler(filename='error_log', when='D',
                                        backup_count=5, encoding="utf-8")
        # 设置日志格式
        # 默认输出
        date_format = '%Y-%m-%d %H:%M:%S %a'
        formatter = logging.Formatter(fmt="%(asctime)s - %(module)s - %(funcName)s：%(lineno)d  - "
                                          "%(levelname)s: %(message)s", datefmt=date_format)

        bug_filter = logging.Filter()
        bug_filter.filter = lambda record: record.levelno == logging.ERROR  # 设置过滤等级
        error_handler.addFilter(bug_filter)
        error_handler.setFormatter(formatter)
        self.addHandler(error_handler)

        bug_filter = logging.Filter()
        bug_filter.filter = lambda record: record.levelno < logging.ERROR  # 设置过滤等级
        main_handler.addFilter(bug_filter)
        main_handler.addFilter(bug_filter)
        main_handler.setFormatter(formatter)
        self.main_handler = main_handler
        self.addHandler(main_handler)

    # def error(self, msg="", *args, **kwargs):
    #     """
    #     捕获异常栈
    #     :param msg:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     if self.isEnabledFor(logging.ERROR):
    #         traceback_rollback = traceback.format_exc()
    #         traceback_rollback = "" if str(traceback_rollback) == "NoneType: None\n" else traceback_rollback
    #         msg = str(msg) + traceback_rollback
    #         self._log(logging.ERROR, msg, args, **kwargs)

    def reset_name(self, name):
        """
        重新设置日志文件名
        :param name:
        :return:
        """
        self.name = name
        self.removeHandler(self.main_handler)
        self.__set_log_handler()


try:
    import codecs
except ImportError:
    codecs = None


class MyLoggerHandler(logging.FileHandler):
    def __init__(self, filename, when='M', backup_count=15, encoding=None, delay=False):
        self.prefix = os.path.join(LOG_PATH, '{name}'.format(name=filename))
        self.filename = filename
        self.when = when.upper()
        # S - Every second a new file
        # M - Every minute a new file
        # H - Every hour a new file
        # D - Every day a new file
        if self.when == 'S':
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}\.log$"
        elif self.when == 'M':
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}\.log$"
        elif self.when == 'H':
            self.suffix = "%Y-%m-%d_%H"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}\.log$"
        elif self.when == 'D':
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        else:
            raise ValueError("Invalid rollover interval specified: %s" % self.when)
        self.filePath = "%s%s.log" % (self.prefix, datetime.datetime.now().strftime(self.suffix))
        try:
            if os.path.exists(LOG_PATH) is False:
                os.makedirs(LOG_PATH)
        except Exception as e:
            print("can not make dirs")
            print("filepath is " + self.filePath)
            print(e)

        self.backupCount = backup_count
        if codecs is None:
            encoding = None
        logging.FileHandler.__init__(self, self.filePath, 'a', encoding, delay)

    def write_log(self):
        _filePath = "%s%s.log" % (self.prefix, datetime.datetime.now().strftime(self.suffix))
        if _filePath != self.filePath:
            self.filePath = _filePath
            return 1
        return 0

    def change_file(self):
        self.baseFilename = os.path.abspath(self.filePath)
        if self.stream is not None:
            self.stream.flush()
            self.stream.close()
        if not self.delay:
            self.stream = self._open()
        if self.backupCount > 0:
            for s in self.delete_old_log():
                os.remove(s)

    def delete_old_log(self):
        dir_name, base_name = os.path.split(self.baseFilename)
        file_names = os.listdir(dir_name)
        result = []
        p_len = len(self.filename)
        for fileName in file_names:
            if fileName[:p_len] == self.filename:
                suffix = fileName[p_len:]
                if re.compile(self.extMatch).match(suffix):
                    result.append(os.path.join(dir_name, fileName))
        result.sort()
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def emit(self, record):
        """
        Emit a record.
        """
        # noinspection PyBroadException
        try:
            if self.write_log():
                self.change_file()
            logging.FileHandler.emit(self, record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
