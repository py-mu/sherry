# coding=utf-8
"""
    create by pymu
    on 2021/5/6
    at 17:35
    默认的启动类，其实就是常用的全局设定
"""
import ctypes
import json
import logging
from dataclasses import dataclass
from typing import Type

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.common.logger import ApplicationLogger
from sherry.core.config import ApplicationConfig
from sherry.core.handler import ExceptHookHandler, ExOperational
from sherry.core.resource import ResourceLoader


@dataclass
class Application:
    """
    启动配置类
    设置了一部分对于 QApplication 的初始化或者是流程设定，方便启动及检测，
    这是整个框架的默认入口，你也可以继承这个类，重构其中部分方法以实现您所需要的功能。
    其主要的方法是对窗口的生命周期管理，同时也会添加一些自动化相关的逻辑，
    可能会比较抽象，但是胜在其能够实现。

    Launcher configuration class
    Some initialization or process settings for QApplication are set to facilitate startup and detection,
    This is the default entry of the whole framework.
    You can also inherit this class and refactor some of its methods to achieve the functions you need.
    The main method is to manage the life cycle of windows, and at the same time add some automation related logic,
    It may be more abstract, but the advantage is that it can be realized.
    """

    def __init__(self,
                 config=None,
                 activity=None,
                 handler=None,
                 log_class=None,
                 unique=False
                 ):
        self.config = config or ApplicationConfig()
        self.activity = activity or QWidget()
        self.handler = handler or ExceptHookHandler()
        self.log_class = log_class or ApplicationLogger
        self.unique = unique
        self.localServer = QLocalServer()
        self.socket = QLocalSocket()
        self.resource = ResourceLoader()
        self.__set_logger(self.log_class)
        self.refresh_ex_data()
        self.logger = logging.getLogger()

    def __set_logger(self, logger_class: Type[ApplicationLogger]):
        """
        定义一个可以装载的自定义logger属性

        Define a custom logger attribute that can be loaded.
        """
        logger_class.root_path = self.config.log_path
        logger_class.app_name = self.config.app_name + ".log"
        logging.root = logger_class(logger_class.app_name)
        logging.setLoggerClass(logger_class)

    def refresh_ex_data(self, file_path: str = ''):
        """
        从文件中读取异常拦截数据

        read default config
        """
        with open(file_path or self.config.file_path('sherry/exception_handler.json'), encoding='utf-8') as f:
            self.handler.update_map({k: ExOperational(**v) for k, v in json.load(f).items()})

    def run(self):
        """
        运行

        show your activity
        """
        self.logger.info('启动应用{}'.format(self.config.app_name))
        self.config.app.setStyleSheet(self.resource.qss("common.css"))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.config.app_name)
        if not self.activity:
            raise ValueError('Activity is not load, did you install it ?')
        if not isinstance(self.activity, QWidget):
            raise TypeError('The Activity is not valid Activity.')
        if self.unique:
            self.socket.connectToServer(self.config.app_name)
            if self.socket.waitForConnected(200):
                # todo 添加提示
                self.shutdown()
            self.localServer.listen(self.config.app_name)
        self.activity.show()
        self.config.app.exec_()
        self.shutdown()

    def shutdown(self):
        """
        关闭实例

        shutdown application
        """
        self.logger.info('关闭应用{}'.format(self.config.app_name))
        self.localServer.close()
        self.config.app.quit()
        logging.shutdown()
