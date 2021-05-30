# coding=utf-8
"""
    create by pymu
    on 2021/5/6
    at 17:35
    默认的启动类，其实就是常用的全局设定
"""
import ctypes
import json
from dataclasses import dataclass, field
from logging import Logger

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.core.config import ApplicationConfig
from sherry.core.handler import ExCoreHandler, ExOperational


@dataclass
class SherryApplication:
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
    config: ApplicationConfig = field(default=ApplicationConfig())  # Note: 配置器 configurator
    activity: QWidget = field(default=QWidget())  # Note: 默认主页 default home page
    handler: ExCoreHandler = field(default=ExCoreHandler())  # Note: 拦截器 default exception handler
    unique: bool = field(default=False)  # Note: 唯一启动， only run
    logger: Logger = None  # Note: 日志 logger

    def __post_init__(self):
        """默认初始化"""
        self.localServer = QLocalServer()
        self.socket = QLocalSocket()

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

    #
    def shutdown(self):
        """
        关闭实例

        shutdown application
        """
        self.localServer.close()
        self.config.app.quit()
