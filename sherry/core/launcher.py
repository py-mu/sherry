# coding=utf-8
"""
    create by pymu
    on 2021/5/6
    at 17:35
    默认的启动类，其实就是常用的全局设定
"""
import ctypes
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QWidget

from sherry.core.badge import Badge
from sherry.core.handler import AbnormalHookHandler
from sherry.core.resource import ResourceLoader
from sherry.variable import app_name, app
from sherry.variable.rear import retouch
from sherry.view.activity.activity_dialog import NormalDialogActivity
from sherry.view.activity.activity_welcome import WelcomeActivity

# 加载修饰类
retouch()


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

    def __init__(self, activity=None, unique=False):
        self.__init_before__()
        self.unique = unique
        self.activity = activity or self.activity
        self.__init_app()

    @staticmethod
    def abnormal_dialog(op):
        """异常弹窗"""
        dialog = Badge(source=NormalDialogActivity, title=op.title, info=op.description)
        dialog.setWindowTitle(op.title)
        dialog.exec()

    def __init_app(self):
        """初始化Qt Application"""
        resource = ResourceLoader()
        resource.set_theme(resource.qss("element.css"))
        app.setAttribute(Qt.AA_UseStyleSheetPropagationInWidgetStyles, True)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_name)
        handler = Badge(source=AbnormalHookHandler)

        handler.set_default_callback(self.abnormal_dialog)

    def run(self):
        """
        运行

        show your activity
        """
        logging.info('start {}'.format(app_name))
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
