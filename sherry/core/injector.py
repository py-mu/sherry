# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
from __future__ import print_function

__all__ = ('CursorAgent', 'PropertyAgent', 'BaseAgent')

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from sherry.core.reflex import ReflexCenter


class BaseAgent:
    __agent__ = ()
    instance_func = []

    def __init__(self):
        for agent in self.__agent__:
            getattr(self, agent)()


class CursorAgent(BaseAgent):
    __agent__ = ('install_enter_event', 'install_leave_event')

    @staticmethod
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
    def install_leave_event():
        primeval_func = getattr(QWidget, "leaveEvent")

        def leaveEvent(widget, event) -> None:
            if not hasattr(widget, 'raw_cursor'):
                ReflexCenter.hook(widget, 'raw_cursor', Qt.ArrowCursor)
            if widget.parent():
                widget.parent().setCursor(widget.raw_cursor)
            return primeval_func(widget, event)

        ReflexCenter.hook(QWidget, 'leaveEvent', leaveEvent)


class PropertyAgent(BaseAgent):
    __agent__ = ('install_set_property',)

    @classmethod
    def install_set_property(cls):
        primeval_func = getattr(QWidget, "setProperty")

        def setProperty(self, name, value):
            """在属性发生变化时刷新样式(不允许下划线开头)"""
            result = primeval_func(self, name, value)
            self.style().polish(self)
            return result

        ReflexCenter.hook(QWidget, 'setProperty', setProperty)
