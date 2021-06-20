# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
import functools

from PyQt5.QtCore import Qt, QEvent, QObject
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

        def custom_event(widget: QWidget, event) -> bool:
            for classic in Overrider.custom_events:
                result = classic(widget=widget, event=event)()
                if not result:
                    continue
                return result

            return primeval_events(widget, event)

        setattr(QWidget, 'event', custom_event)

    # @staticmethod
    # @register
    # def install_set_disabled():
    #     """设置控件不可用时，设定鼠标为禁用样式"""
    #     primeval_func = getattr(QWidget, "setDisabled")
    # 
    #     def setDisabled(widget: QWidget, disabled: bool):
    #         key_name = '__sherry_custom_cursor__'
    #         cursor = Qt.ArrowCursor
    #         if disabled:
    #             if not hasattr(widget, key_name):
    #                 setattr(widget, key_name, widget.cursor())
    #             cursor = Qt.ForbiddenCursor
    #         else:
    #             if hasattr(widget, key_name):
    #                 cursor = getattr(widget, key_name) or Qt.ArrowCursor
    #         widget.setCursor(cursor)
    #         return primeval_func(widget, disabled)
    # 
    #     setattr(QWidget, 'setDisabled', setDisabled)

    @staticmethod
    @register
    def install_set_enabled():
        primeval_func = getattr(QWidget, "setEnabled")

        def setEnabled(widget: QWidget, enabled: bool):
            key_name = '__sherry_custom_cursor__'
            cursor = Qt.ArrowCursor
            if not enabled:
                if not hasattr(widget, key_name):
                    setattr(widget, key_name, widget.cursor())
                cursor = Qt.ForbiddenCursor
            else:
                if hasattr(widget, key_name):
                    cursor = getattr(widget, key_name) or Qt.ArrowCursor
            widget.setCursor(cursor)
            return primeval_func(widget, enabled)

        setattr(QWidget, 'setEnabled', setEnabled)

    @staticmethod
    @register
    def install_event_filter():
        primeval_func = getattr(QWidget, "eventFilter")

        def eventFilter(self, obj: QObject, event: QEvent) -> bool:
            if event.type() == QEvent.MouseButtonRelease:
                print(event)
                return True
            return primeval_func(self, obj, event)

        setattr(QWidget, 'eventFilter', eventFilter)

    @staticmethod
    def install():
        for func in __instance_func__:
            func()
