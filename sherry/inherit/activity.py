# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 0:11
"""

from qtpy.QtCore import Qt, QPropertyAnimation
from qtpy.QtWidgets import QDialog, QWidget, QHBoxLayout, QVBoxLayout

from sherry.core.resource import app
from sherry.inherit.view import BaseView
from sherry.variable import app_name


class BaseActivity(QDialog, BaseView):
    """
    默认的窗口级组件
    """

    def __init__(self, master=None, *args, **kwargs):
        super(BaseActivity, self).__init__(master, *args, **kwargs)
        # 此配置器是经过实例化后的子类，理论上在launcher装载后就会被全局共享
        # 所以此处获取到的即是你实例化后的子类
        # This configurator is a subclass after instantiation,
        # theoretically it will be shared globally after the launcher is loaded
        # So what you get here is the subclass you instantiated

    def configure(self):
        self.resize(1047, 680)
        self.setMouseTracking(True)
        self.setWindowIcon(self.resource.project_png)
        self.setWindowTitle(app_name)

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
    fade_out_animation = None  # 淡出
    fade_in_animation = None  # 淡入
    signals = {}

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

    def center(self):
        screen = app.desktop().availableGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2 - 100)

    def configure(self):
        super(FrameLessWindowHintActivity, self).configure()
        self.setObjectName("main_window")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        if self.body_widget:
            self.set_default_window_shadow()
            self.body_widget.setMouseTracking(True)

    def accept(self):
        self.set_switch_animation(self.accept_)

    def set_switch_animation(self, callback=None, duration=200, start=1, end=0, animation=None):
        """设置切换效果"""
        self.fade_out_animation = animation or self.fade_out_animation or QPropertyAnimation(self, b'windowOpacity')
        while self.signals:
            key, slot = self.signals.popitem()
            try:
                self.fade_out_animation.finished.disconnect(slot)
            except TypeError:
                pass
        self.fade_out_animation.stop()
        self.fade_out_animation.setDuration(duration)
        self.fade_out_animation.setStartValue(start)
        self.fade_out_animation.setEndValue(end)
        if callback:
            self.signals.update({id(callback): callback})
            self.fade_out_animation.finished.connect(callback)
        self.fade_out_animation.start()

    def accept_(self):
        """添加淡出"""
        return super(FrameLessWindowHintActivity, self).accept()

    # noinspection PyArgumentList
    def place(self):
        super(FrameLessWindowHintActivity, self).place()
        if not self.body_widget:
            main_layout = QHBoxLayout(self)
            self.body_widget = QWidget(self, flags=Qt.Widget)
            self.body_layout = QVBoxLayout(self.body_widget)
            self.body_layout.setContentsMargins(*[0] * 4)
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
