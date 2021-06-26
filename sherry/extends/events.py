# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:30
"""
from PyQt5.QtCore import QEvent, QRect
from PyQt5.QtWidgets import QToolTip


class EventCell:
    """装载单元"""

    def __init__(self, widget, event):
        self.widget = widget
        self.event = event

    def __hash__(self):
        return id(self.__class__.__name__)

    def __call__(self, *args, **kwargs):
        raise NotImplementedError('未实现回调')


class TooltipEvent(EventCell):
    """重载 QT tooltip 逻辑"""

    def __call__(self, *args, **kwargs):
        if self.event.type() == QEvent.ToolTip and self.widget.toolTip():
            QToolTip.showText(self.event.globalPos(), "这是重载后的 tooltip", self.widget, QRect(),
                              self.widget.toolTipDuration())
            return True
        else:
            self.event.ignore()
