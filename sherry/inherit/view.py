# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 0:11
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle, QGraphicsDropShadowEffect

from sherry.core.resource import ResourceLoader


class BaseView(QWidget):
    """
    application base view.
    """

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.resource = ResourceLoader()

    def set_signal(self):
        """
        信号设置, 信号放在此处定义，方便管理哦，如此在后期调试就不用在各处翻找事件及信号

        Signal settings, the signals are defined here,
        which is convenient for management,
        so you don’t need to search for events and signals everywhere in post-debugging
        """
        ...

    def configure(self):
        """
        属性配置，同上统一配置方便管理

        Attribute configuration, same as above, unified configuration for easy management
        """
        ...

    def procedure(self):
        """
        初始化流程, 比如setUi、place、configure、set_signal等，
        注意先后顺序，place放置结束之后、进行页面配置（样式、属性等）、连接信号。

        Initialization process, such as setUi, place, configure, set_signal, etc.,
        Pay attention to the order, after placing the place,
        perform page configuration (style, attributes, etc.) and connect signals.
        """
        self.place()
        self.configure()
        self.set_signal()

    def place(self):
        """
        页面微布局,并不是所有的页面都是由Qt designer 设计而来的
        还有部分组件需要加载到页面，约定在这里编写，方便管理哦

        Page micro layout, not all pages are designed by Qt designer
        There are still some components that need to be loaded on the page.
         The agreement is written here for easy management.
        """
        ...

    def get_effect_shadow(self,
                          offset=(0, 0),
                          radius=10,
                          color=Qt.darkGray):
        """
        获取一个默认的阴影对象

        Get a default shadow object.

        :param offset: 偏移（x， y）
        :param radius: 半径；默认10
        :param color: 颜色
        """
        effect_shadow = QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(*offset)  # Note: 偏移
        effect_shadow.setBlurRadius(radius)  # Note: 阴影半径
        effect_shadow.setColor(color)  # Note: 阴影颜色
        return effect_shadow

    @staticmethod
    def set_widget_shadow(shadow, widget):
        """
        给控件设置阴影

        Set a shadow to the control.
        """
        widget.setGraphicsEffect(shadow)

    def paintEvent(self, event):
        """
        重写paintEvent,
        如此在继承widget等控件之后依然可以通过调用qss样式文件进行样式重载

        Rewrite paintEvent,
        In this way, after inheriting widgets and other controls,
         you can still reload styles by calling the qss style file
        """
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, QPainter(self), self)
        super().paintEvent(event)

    def showEvent(self, event):
        """解决最小化之后页面假死问题，此处参阅：https://blog.csdn.net/qq_40194498/article/details/109511055"""
        if not self.isMinimized():
            self.setAttribute(Qt.WA_Mapped)
        return super().showEvent(event)

    # def event(self, event: QEvent) -> bool:
    #     if event.type() == QEvent.ToolTip:
    #         event: QHelpEvent
    #         w, h = tooltip.width(), tooltip.height()
    #         x, y = event.globalX(), event.globalY() + h
    #         tooltip.setGeometry(x, y, w, h)
    #         tooltip.show()
    #         return True
    #     return super().event(event)
