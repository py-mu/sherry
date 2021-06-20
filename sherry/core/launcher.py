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
from typing import Type

from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.common.logger import ApplicationLogger
from sherry.core.config import ApplicationConfig
from sherry.core.handler import ExceptHookHandler, ExOperational
from sherry.core.resource import ResourceLoader
from sherry.extends.override import Overrider
from sherry.view.activity.activity_dialog import NormalDialogActivity
from sherry.view.activity.activity_welcome import WelcomeActivity


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

    __slots__ = (
    'activity', 'config', 'handler', 'log_class', 'unique', 'override_class', 'err_desc_file_path', 'localServer',
    'socket')

    def __before__(self):
        """运行之前"""
        self.unique = False
        self.override_class = Overrider
        self.socket = QLocalSocket()
        self.localServer = QLocalServer()
        self.config = ApplicationConfig().instance()
        self.log_class = ApplicationLogger
        self.activity = WelcomeActivity
        self.handler = ExceptHookHandler()
        self.err_desc_file_path = self.config.file_path('sherry/exception-handler.json')

    def set_properties(self, *args, **kwargs):
        """设置类属性"""
        for index, value in enumerate(args):
            if value:
                setattr(self, self.__slots__[index], value)
        for key, value in kwargs.items():
            if key not in self.__slots__:
                raise ValueError(
                    'can not install key {}  to init.'
                    'because of you are not append the key into value "self.init_keys".'.format(key)
                )
            if value:
                setattr(self, key, value)

    def __init__(self, *args, **kwargs):
        self.__before__()
        self.set_properties(*args, **kwargs)
        self.procedure()

    def procedure(self):
        """实施"""
        self.override_class().install()
        self.__set_logger(self.log_class)
        self.refresh_ex_data(self.err_desc_file_path)
        self.__init_app()

    def __set_logger(self, logger_class: Type[ApplicationLogger]):
        """
        定义一个可以装载的自定义logger属性

        Define a custom logger attribute that can be loaded.
        """
        logger_class.root_path = self.config.log_path
        logger_class.app_name = self.config.app_name + ".log"
        logging.root = logger_class(logger_class.app_name)
        logging.setLoggerClass(logger_class)

    def refresh_ex_data(self, file_path):
        """
        从文件中读取异常拦截数据

        read default config
        """
        with open(file_path, encoding='utf-8') as f:
            self.handler.update_map({k: ExOperational(**v) for k, v in json.load(f).items()})

    def __init_app(self):
        """初始化Qt Application"""
        self.config.set_theme(ResourceLoader().qss("element.css"))
        app = self.config.app
        app.setAttribute(Qt.AA_UseStyleSheetPropagationInWidgetStyles, True)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.config.app_name)

    def run(self):
        """
        运行

        show your activity
        """
        logging.info('start {}'.format(self.config.app_name))
        if not self.activity:
            raise ValueError('Activity is not load, did you install it ?')
        if not isinstance(self.activity, type(QWidget)):
            raise TypeError('The Activity is not valid Activity.')
        if self.unique:
            self.socket.connectToServer(self.config.app_name)
            if self.socket.waitForConnected(200):
                dialog = NormalDialogActivity(title="重复运行", info="已有实例 {} 在运行.".format(self.config.app_name))
                dialog.exec()
                self.shutdown()
            self.localServer.listen(self.config.app_name)
        self.activity().show()
        self.config.app.exec_()
        self.shutdown()

    def shutdown(self):
        """
        关闭实例

        shutdown application
        """
        logging.info('shutdown {}'.format(self.config.app_name))
        self.localServer.close()
        self.config.app.quit()
        logging.shutdown()
