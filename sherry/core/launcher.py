# coding=utf-8
"""
    create by pymu
    on 2021/5/6
    at 17:35
    默认的启动类，其实就是常用的全局设定
"""
import ctypes
import json
import sys
from collections import namedtuple

from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from PyQt5.QtWidgets import QApplication, QWidget

from sherry.core.config import ApplicationConfig
from sherry.core.handler import ExCoreHandler, ExOperational

# 放在py文件中，需要在窗口显示之前实例化
# Need to be instantiated before the window is displayed
app: QApplication = QApplication.instance() or QApplication(sys.argv)


class Launcher:
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

    class Base(type):

        def __new__(mcs, name, bases, attrs, **kwargs):
            return super().__new__(mcs, name, bases, attrs)


    class Setting(dict, metaclass=Base):
        __slots__ = ('activity', 'unique', 'config', 'except_handler')

        def __init__(self, **kwargs):
            super().__init__()
            self.config = kwargs.get('config', ApplicationConfig())

        config: ApplicationConfig  # Note: 配置类  Configuration
        except_handler: ExCoreHandler  # Note: 异常拦截类  Exception Handler

    setting: Setting

    def __init__(self, **kwargs):
        """
        :type kwargs Launcher.Setting[str, object]

        :param kwargs:
        """
        self.Setting()

        self.setting = self.Setting(**kwargs)
        self.load()
        self.Setting()
        a = namedtuple('te', ['name', 'sex', 'age'])

        self.refresh_ex_data()
        self.localServer = QLocalServer()
        self.socket = QLocalSocket()

    def load(self):
        """
        装载跟设置默认参数
        初始化时会查询对应的包目录下，通过反射装载对应的配置类或者拦截类

        set and load default value
        """
        self.setting.setdefault('activity', None)
        self.setting.setdefault('unique', True)
        self.setting.setdefault('config', ApplicationConfig())
        self.setting.setdefault('except_handler', ExCoreHandler())

        self.config = self.setting.get('config')
        self.except_handler = self.setting.get('except_handler')

    def refresh_ex_data(self, file_path: str = ''):
        """
        从文件中读取异常拦截数据

        read default config
        """
        with open(file_path or self.config.file_path('sherry/exception_handler.json'), encoding='utf-8') as f:
            self.except_handler.update_map({k: ExOperational(**v) for k, v in json.load(f).items()})

    def run(self):
        """
        运行

        show your activity
        """
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.config.app_name)
        activity: QWidget = self.setting.get('activity')
        if not activity:
            raise ValueError('Activity is not load, did you install it ?')
        if not isinstance(activity, QWidget):
            raise TypeError('The Activity is not valid Activity.')
        if self.setting.get('unique'):
            self.socket.connectToServer(self.config.app_name)
            if self.socket.waitForConnected(200):
                # todo 添加提示
                self.shutdown()
            self.localServer.listen(self.config.app_name)
        activity.show()
        app.exec_()
        self.shutdown()

    def shutdown(self):
        """关闭实例"""
        self.localServer.close()
        app.quit()
