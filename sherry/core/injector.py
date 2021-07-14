# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
from __future__ import print_function

import functools

from PyQt5.QtCore import Qt, QEvent, QRect
from PyQt5.QtWidgets import QToolTip, QWidget, QAbstractScrollArea

__all__ = ('WidgetInjector', 'register')
__instance_func__ = []

from sherry.core.reflex import ReflexCenter


def register(func):
    """注册方法"""

    __instance_func__.append(func)

    @functools.wraps(func)
    def warps():
        return func()

    return warps


class WidgetInjector:

    def __init__(self):
        self.__install()

    @staticmethod
    def _register_tooltip(obj):
        """替换内置的tooltip样式"""
        primeval_event_function = getattr(obj, 'event')

        def graft(widget, event):
            if event.type() == QEvent.ToolTip and widget.toolTip():
                QToolTip.showText(event.globalPos(), "这是重载后的 tooltip", widget, QRect(),
                                  widget.toolTipDuration())
                return True
            return primeval_event_function(widget, event)

        return graft

    @staticmethod
    @register
    def install_events():
        """装载 event 颗粒"""
        ReflexCenter.hook(QWidget, 'event', WidgetInjector._register_tooltip(QWidget))
        ReflexCenter.hook(QAbstractScrollArea, 'event', WidgetInjector._register_tooltip(QAbstractScrollArea))

    @staticmethod
    @register
    def install_enter_event():
        primeval_func = getattr(QWidget, "enterEvent")

        def enterEvent(widget, event):
            if not hasattr(widget, 'raw_cursor'):
                ReflexCenter.hook(widget, 'raw_cursor', Qt.ArrowCursor)
            if widget.parent():
                ReflexCenter.hook(widget, 'raw_cursor', widget.parent().cursor())
                if not widget.isEnabled():
                    widget.parent().setCursor(Qt.ForbiddenCursor)
            return primeval_func(widget, event)

        ReflexCenter.hook(QWidget, 'enterEvent', enterEvent)

    @staticmethod
    @register
    def install_leave_event():
        primeval_func = getattr(QWidget, "leaveEvent")

        def leaveEvent(widget, event) -> None:
            if not hasattr(widget, 'raw_cursor'):
                ReflexCenter.hook(widget, 'raw_cursor', Qt.ArrowCursor)
            if widget.parent():
                widget.parent().setCursor(widget.raw_cursor)
            return primeval_func(widget, event)

        ReflexCenter.hook(QWidget, 'leaveEvent', leaveEvent)

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

        ReflexCenter.hook(QWidget, 'setProperty', setProperty)

    @staticmethod
    def __install():
        for func in __instance_func__:
            func()
