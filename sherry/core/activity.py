# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 0:11
"""

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QDialog, QWidget, QHBoxLayout
from PyQt5.uic.properties import QtGui

from sherry.core.config import ApplicationConfig
from sherry.core.resource import ResourceLoader
from sherry.core.view import BaseView


class BaseActivity(QDialog, BaseView):
    """
    默认的窗口级组件
    """
    parent: QWidget = None

    def __init__(self, parent: QWidget, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        # 此配置器是经过实例化后的子类，理论上在launcher装载后就会被全局共享
        # 所以此处获取到的即是你实例化后的子类
        # This configurator is a subclass after instantiation,
        # theoretically it will be shared globally after the launcher is loaded
        # So what you get here is the subclass you instantiated
        self.config = ApplicationConfig.instance()
        self.resource = ResourceLoader()

    def configure(self) -> None:
        self.resize(1047, 680)
        self.setMouseTracking(True)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        """
        键盘监听事件, 取消按 ESC 退出

        Keyboard monitor event, cancel and press ESC to exit.

        :param event: event事件
        """
        if event.key() == Qt.Key_Escape:
            event.ignore()
        else:
            event.accept()


class FrameLessWindowHintActivity(BaseActivity):
    """
    无边框窗口

    FrameLessWindowHintActivity.
    """

    body_widget: QWidget = None  # Note: 页面上的主要容器，控件应该放在这个里面
    body_layout: QHBoxLayout = None
    bar: BaseView = None  # 顶部标题栏
    border_width: int = 5  # 窗口拉伸边界

    class EventFlags:
        """
        扳机状态，用于判定鼠标事件是否触发

        flag event.
        """
        event_flag_bar_move = False
        event_flag_border_left = False
        event_flag_border_right = False
        event_flag_border_top = False
        event_flag_border_bottom = False
        event_flag_border_top_left = False
        event_flag_border_top_right = False
        event_flag_border_bottom_left = False
        event_flag_border_bottom_right = False

        # 不得已以为拉伸闪烁问题
        # 只能设定固定方向的拉伸能够使用
        # 当然全部打开也是可以的，只是存在闪烁问题
        # PC端的应用大部分存在这个问题，所以用也可以
        # I have to think that the stretching flicker problem
        # Can only be used for stretching in a fixed direction
        # Of course, it’s okay to open it all, but there is a flickering problem
        # Most of the PC-side applications have this problem, so it can be used
        event_switch_border_left = False
        event_switch_border_right = True
        event_switch_border_top = False
        event_switch_border_bottom = True
        event_switch_border_top_left = False
        event_switch_border_top_right = False
        event_switch_border_bottom_left = False
        event_switch_border_bottom_right = True

        event_position_mouse: QPoint = None

    def __init__(self, parent: QWidget, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    def configure(self) -> None:
        super(FrameLessWindowHintActivity, self).configure()
        self.setObjectName("main_window")
        self.setWindowIcon(self.resource.project_png)
