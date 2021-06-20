# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 0:11
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QHBoxLayout, QVBoxLayout

from sherry.core.config import ApplicationConfig
from sherry.inherit.view import BaseView


class BaseActivity(QDialog, BaseView):
    """
    默认的窗口级组件
    """
    parent = None

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # 此配置器是经过实例化后的子类，理论上在launcher装载后就会被全局共享
        # 所以此处获取到的即是你实例化后的子类
        # This configurator is a subclass after instantiation,
        # theoretically it will be shared globally after the launcher is loaded
        # So what you get here is the subclass you instantiated
        self.config = ApplicationConfig.instance()

    def configure(self):
        self.resize(1047, 680)
        self.setMouseTracking(True)
        self.setWindowIcon(self.resource.project_png)
        self.setWindowTitle(self.config.app_name)

    def keyPressEvent(self, event):
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

    body_widget = None  # Note: 页面上的主要容器，控件应该放在这个里面
    body_layout = None
    bar = None  # 顶部标题栏
    border_width = 5  # 窗口拉伸边界

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

        event_position_mouse = None

    def __init__(self, master=None, *args, **kwargs):
        super(FrameLessWindowHintActivity, self).__init__(master, *args, **kwargs)
        self.event_flags = self.EventFlags()
        self.procedure()

    def configure(self):
        super(FrameLessWindowHintActivity, self).configure()
        self.setObjectName("main_window")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        if self.body_widget:
            self.set_default_window_shadow()
            self.body_widget.setMouseTracking(True)

    def place(self):
        super(FrameLessWindowHintActivity, self).place()
        if not self.body_widget:
            main_layout = QHBoxLayout(self)
            self.body_widget = QWidget()
            self.body_layout = QVBoxLayout(self.body_widget)
            main_layout.addWidget(self.body_widget)

    def set_default_window_shadow(self):
        """设置默认阴影"""
        self.set_widget_shadow(self.get_effect_shadow(), self.body_widget)

    def event_flag(self, event):
        """判断鼠标是否移动到边界"""
        top = self.border_width < event.pos().y() < self.border_width + 10
        bottom = self.border_width + self.body_widget.height() < event.pos().y() < self.height()
        left = self.border_width < event.pos().x() < self.border_width + 10
        right = self.border_width + self.body_widget.width() < event.pos().x() < self.width()
        return top, bottom, left, right

    def mousePressEvent(self, event):
        """重构鼠标点击事件"""
        if not self.body_widget:
            return super(FrameLessWindowHintActivity, self).mousePressEvent(event)
        top, bottom, left, right = self.event_flag(event)
        # 左键事件
        if event.button() == Qt.LeftButton:
            self.event_flags.event_position_mouse = event.globalPos() - self.pos()
            if top and left and self.event_flags.event_switch_border_top_left:
                self.event_flags.event_flag_border_top_left = True
            elif top and right and self.event_flags.event_switch_border_top_right:
                self.event_flags.event_flag_border_top_right = True
            elif bottom and left and self.event_flags.event_switch_border_bottom_left:
                self.event_flags.event_flag_border_bottom_left = True
            elif bottom and right and self.event_flags.event_switch_border_bottom_right:
                self.event_flags.event_flag_border_bottom_right = True
            elif top and self.event_flags.event_switch_border_top:
                self.event_flags.event_flag_border_top = True
            elif bottom and self.event_flags.event_switch_border_bottom:
                self.event_flags.event_flag_border_bottom = True
            elif left and self.event_flags.event_switch_border_left:
                self.event_flags.event_flag_border_left = True
            elif right and self.event_flags.event_switch_border_right:
                self.event_flags.event_flag_border_right = True
            elif self.bar and self.body_widget and event.y() < self.bar.height() \
                    + self.body_widget.layout().getContentsMargins()[1] * 2 \
                    + self.border_width + self.body_layout.spacing():
                self.event_flags.event_flag_bar_move = True
                self.event_flags.event_position_mouse = event.globalPos() - self.pos()
        return super(FrameLessWindowHintActivity, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        super(FrameLessWindowHintActivity, self).mouseMoveEvent(event)
        if self.body_widget:
            top, bottom, left, right = self.event_flag(event)
            if top and left and self.event_flags.event_switch_border_top_left:
                self.setCursor(Qt.SizeFDiagCursor)
            elif bottom and right and self.event_flags.event_switch_border_bottom_right:
                self.setCursor(Qt.SizeFDiagCursor)
            elif top and right and self.event_flags.event_switch_border_top_right:
                self.setCursor(Qt.SizeBDiagCursor)
            elif bottom and left and self.event_flags.event_switch_border_bottom_left:
                self.setCursor(Qt.SizeBDiagCursor)
            elif top and self.event_flags.event_switch_border_top:
                self.setCursor(Qt.SizeVerCursor)
            elif bottom and self.event_flags.event_switch_border_bottom:
                self.setCursor(Qt.SizeVerCursor)
            elif left and self.event_flags.event_switch_border_left:
                self.setCursor(Qt.SizeHorCursor)
            elif right and self.event_flags.event_switch_border_right:
                self.setCursor(Qt.SizeHorCursor)
            elif Qt.LeftButton and self.event_flags.event_flag_bar_move:
                self.move(event.globalPos() - self.event_flags.event_position_mouse)
            else:
                self.setCursor(Qt.ArrowCursor)
            # 窗口拉伸
            if self.event_flags.event_flag_border_top_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y() + event.pos().y(),
                                 self.width() - event.pos().x(), self.height() - event.pos().y())
            elif self.event_flags.event_flag_border_bottom_right:
                self.resize(event.pos().x(), event.pos().y())

            elif self.event_flags.event_flag_border_bottom_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y(),
                                 self.width() - event.pos().x(), event.pos().y())

            elif self.event_flags.event_flag_border_top_right:
                self.setGeometry(self.geometry().x(), self.geometry().y() + event.pos().y(),
                                 event.pos().x(), self.height() - event.pos().y())
            elif self.event_flags.event_flag_border_right:
                self.resize(event.pos().x(), self.height())
            elif self.event_flags.event_flag_border_left:
                self.setGeometry(self.geometry().x() + event.pos().x(), self.geometry().y(),
                                 self.width() - event.pos().x(), self.height())
            elif self.event_flags.event_flag_border_bottom:
                self.resize(self.width(), event.pos().y())
            elif self.event_flags.event_flag_border_top:
                self.setGeometry(self.geometry().x(), self.geometry().y() + event.pos().y(),
                                 self.width(), self.height() - event.pos().y())

    def mouseReleaseEvent(self, event):
        """鼠标释放事件"""
        super(FrameLessWindowHintActivity, self).mouseReleaseEvent(event)
        self.event_flags.event_flag_bar_move = False
        self.event_flags.event_flag_border_left = False
        self.event_flags.event_flag_border_right = False
        self.event_flags.event_flag_border_top = False
        self.event_flags.event_flag_border_bottom = False
        self.event_flags.event_flag_border_top_left = False
        self.event_flags.event_flag_border_top_right = False
        self.event_flags.event_flag_border_bottom_left = False
        self.event_flags.event_flag_border_bottom_right = False
