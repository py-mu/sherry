# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
import functools

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from sherry.extends.events import TooltipEvent

__all__ = ('Overrider', 'register')
__instance_func__ = []


def register(func):
    """注册方法"""

    __instance_func__.append(func)

    @functools.wraps(func)
    def warps():
        return func()

    return warps


class Overrider:
    custom_events = [TooltipEvent]

    @staticmethod
    @register
    def install_events():
        """装载 event 颗粒"""
        # inherit old QWidget event function
        primeval_events = getattr(QWidget, "event")

        def custom_event(widget, event):
            for classic in Overrider.custom_events:
                result = classic(widget=widget, event=event)()
                if not result:
                    continue
                return result

            return primeval_events(widget, event)

        setattr(QWidget, 'event', custom_event)

    @staticmethod
    @register
    def install_enter_event():
        primeval_func = getattr(QWidget, "enterEvent")

        def enterEvent(widget, event):
            if not hasattr(widget, 'raw_cursor'):
                setattr(widget, 'raw_cursor', Qt.ArrowCursor)
            if widget.parent():
                setattr(widget, 'raw_cursor', widget.parent().cursor())
                if not widget.isEnabled():
                    widget.parent().setCursor(Qt.ForbiddenCursor)
            return primeval_func(widget, event)

        setattr(QWidget, 'enterEvent', enterEvent)

    @staticmethod
    @register
    def install_leave_event():
        primeval_func = getattr(QWidget, "leaveEvent")

        def leaveEvent(self, event) -> None:
            if not hasattr(self, 'raw_cursor'):
                setattr(self, 'raw_cursor', Qt.ArrowCursor)
            if self.parent():
                self.parent().setCursor(self.raw_cursor)
            return primeval_func(self, event)

        setattr(QWidget, 'leaveEvent', leaveEvent)

    #  设置动态修改属性会重载样式
    @staticmethod
    @register
    def install_set_property():
        primeval_func = getattr(QWidget, "setProperty")

        def setProperty(self, name, value):
            """在属性发生变化时刷新样式(不允许下划线开头)"""
            result = primeval_func(self, name, value)
            self.style().polish(self)
            return result

        setattr(QWidget, 'setProperty', setProperty)

    @staticmethod
    def install():
        for func in __instance_func__:
            func()
