# coding=utf-8
"""
    create by pymu on 2020/5/7
    package: .logger.py
    project:
"""
import logging
import os
from logging.handlers import RotatingFileHandler


class ApplicationLogger(logging.Logger):

    def __init__(self, name):
        super().__init__(name)
        self.level = logging.INFO


class LoggerSetter:
    """
    日志设置，设定应用使用的日志类

    set default logger, more uses see:
    """
    debug = True
    log_path = 'log'
    log_name = 'sherry'
    log_class = ApplicationLogger
    handlers = []
    record2file = True
    formatter = '%(asctime)s - %(module)s - %(funcName)s：%(lineno)d  -  %(levelname)s: %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S %a'

    def __init__(self, name=None, debug=True):
        self.debug = debug
        self.log_name = name or self.log_name
        self.set_root_log()
        self.__init_handler()
        self.__add_handler()

    def set_root_log(self):
        """设置默认的日志来源"""
        logging.setLoggerClass(self.log_class)
        logging.root = self.log_class("{}.log".format(self.log_name))
        if self.debug:
            logging.root.setLevel(logging.DEBUG)

    def __init_handler(self):
        """"""
        if self.record2file:
            if not os.path.exists(self.log_path):
                os.mkdir(self.log_path)
            file_path = os.path.join(self.log_path, "{}.log".format(self.log_name))

            # output log into file. use python default logging module.
            self.handlers.append(self.LogFileHandler(file_path))

        # output to terminal by python default logging module.
        self.handlers.append(self.TerminalHandler())

        # output to terminal by colorlog module.
        # more and see: https://github.com/borntyping/python-colorlog.
        # self.handlers.append(self.TerminalHandler())

        # use loguru.
        # More usage see: https://github.com/Delgan/loguru.
        # self.handlers.append(self.LoguruHandler(file_path))

    def __add_handler(self):
        for handler in self.handlers:
            logging.root.addHandler(handler)

    class TerminalHandler(logging.StreamHandler):
        """
        默认的日志输出

        output to terminal by python default logging module.
        """

        def __init__(self):
            super().__init__()
            self.formatter = logging.Formatter(fmt=LoggerSetter.formatter, datefmt=LoggerSetter.datefmt)
            self.level = logging.DEBUG

    class LogFileHandler(RotatingFileHandler):
        """
        输出到文件

        output log into file. use python default logging module.
        """

        def __init__(self, filename):
            super().__init__(filename, maxBytes=20 * 1024 * 1024,
                             backupCount=5, encoding='utf-8')
            self.level = logging.INFO
            self.formatter = logging.Formatter(fmt=LoggerSetter.formatter, datefmt=LoggerSetter.datefmt)

    # class ColorlogTerminalHandler(logging.StreamHandler):
    #     """使用 cololog 作为终端输出"""
    #
    #     def __init__(self):
    #         super().__init__()
    #         self.formatter = colorlog.ColoredFormatter(
    #             fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    #             datefmt='%Y-%m-%d  %H:%M:%S',
    #         )
    #         self.level = logging.DEBUG

    # class LoguruHandler(logging.Handler):
    #     """
    #     使用loguru
    #
    #     More usage see: https://github.com/Delgan/loguru.
    #     """
    #
    #     def __init__(self, filename=None):
    #         super().__init__()
    #         # 输出到文件
    #         if filename and LoggerSetter.record2file:
    #             logger.add(filename, rotation="20 MB", enqueue=True)
    #
    #     def emit(self, record):
    #         try:
    #             level = logger.level(record.levelname).name
    #         except ValueError:
    #             level = record.levelno
    #         frame, depth = logging.currentframe(), 2
    #         while frame.f_code.co_name != '<module>':
    #             frame = frame.f_back
    #             depth += 1
    #         logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
