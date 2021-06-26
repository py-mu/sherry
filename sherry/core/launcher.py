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

from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.variable import app_name, app
from sherry.core.handler import ExceptHookHandler, ExOperational
from sherry.core.resource import ResourceLoader
from sherry.core.badge import Badge
from sherry.utls.paths import SherryPath
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

    def __init_before__(self):
        self.socket = QLocalSocket()
        self.localServer = QLocalServer()
        self.activity = Badge(source=WelcomeActivity)
        self.handler = Badge(source=ExceptHookHandler)
        self.err_desc_file_path = Badge(source=SherryPath).file_path('sherry/exception-handler.json')
        self.refresh_ex_data(self.err_desc_file_path)

    def __init__(self, activity=None, unique=False):
        self.__init_before__()
        self.unique = unique
        self.activity = activity or self.activity
        self.__init_app()

    def refresh_ex_data(self, file_path):
        """
        从文件中读取异常拦截数据

        read default config
        """
        with open(file_path, encoding='utf-8') as f:
            self.handler.update_map({k: ExOperational(**v) for k, v in json.load(f).items()})

    @staticmethod
    def __init_app():
        """初始化Qt Application"""
        resource = ResourceLoader()
        resource.set_theme(resource.qss("element.css"))
        app.setAttribute(Qt.AA_UseStyleSheetPropagationInWidgetStyles, True)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_name)

    def run(self):
        """
        运行

        show your activity
        """
        logging.info('start {}'.format(app_name))
        if not self.activity:
            raise ValueError('Activity is not load, did you install it ?')
        if not isinstance(self.activity, QWidget):
            raise TypeError('The Activity is not valid Activity.')
        if self.unique:
            self.socket.connectToServer(app_name)
            if self.socket.waitForConnected(200):
                raise RuntimeError('重复运行')
            self.localServer.listen(app_name)
        self.activity.show()
        app.exec_()
        self.shutdown()

    def shutdown(self):
        """
        关闭实例

        shutdown application
        """
        logging.info('shutdown {}'.format(app_name))
        self.localServer.close()
        app.quit()
        logging.shutdown()
