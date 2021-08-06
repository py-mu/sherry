# coding=utf-8
"""
    create by pymu on 2020/5/7
    package: .logger.py
    project:
"""
import logging
from logging.handlers import RotatingFileHandler


class LoggerSetter:
    """
    日志设置，设定应用使用的日志类

    set default logger, more uses see:
    """
    handlers = []
    record2file = True
    use_default_log_module = False
    formatter = '%(asctime)s - %(module)s - %(funcName)s：%(lineno)d  -  %(levelname)s: %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S %a'

    def __init__(self, filepath=None):
        self.__init_handler(filepath)
        self.__add_handler()

    def __init_handler(self, filepath):
        """"""
        try:
            # noinspection PyPackageRequirements,PyUnresolvedReferences
            from loguru import logger
            # use loguru.
            # More usage see: https://github.com/Delgan/loguru.
            self.LoguruHandler.logger = logger
            if not self.use_default_log_module:
                self.handlers.append(self.LoguruHandler(filepath))

        except ImportError:
            self.use_default_log_module = True
            # output to terminal by colorlog module.
            # more and see: https://github.com/borntyping/python-colorlog.
            # self.handlers.append(self.TerminalHandler())

        if self.use_default_log_module:
            # output log into file. use python default logging module.
            # 使用默认的logging模块作为日志输出模块
            if filepath:
                self.handlers.append(self.LogFileHandler(filepath))

            # output to terminal by python default logging module.
            # 使用logging输出到终端
            self.handlers.append(self.TerminalHandler())

    def __add_handler(self):
        # remover logging default handler and use new defined.
        [logging.root.removeHandler(handler) for handler in logging.root.handlers]
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

    class LogFileHandler(RotatingFileHandler):
        """
        输出到文件

        output log into file. use python default logging module.
        """

        def __init__(self, filename):
            super().__init__(filename, maxBytes=20 * 1024 * 1024,
                             backupCount=5, encoding='utf-8')
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

    class LoguruHandler(logging.Handler):
        """
        使用loguru

        More usage see: https://github.com/Delgan/loguru.
        """
        logger = None

        def __init__(self, filename=None):
            super().__init__()
            if filename and LoggerSetter.record2file:
                self.logger.add(filename, rotation="20 MB", enqueue=True)

        def emit(self, record):
            try:
                level = self.logger.level(record.levelname).name
            except ValueError:
                level = record.levelno
            frame, depth = logging.currentframe(), 1
            while frame and frame.f_code.co_name != '<module>':
                frame = frame.f_back
                depth += 1
            self.logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
