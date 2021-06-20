# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:30
"""
from PyQt5.QtCore import QEvent, QRect
from PyQt5.QtWidgets import QToolTip

from sherry.inherit.bean import EventCell


class TooltipEvent(EventCell):
    """重载 QT tooltip 逻辑"""

    def __call__(self, *args, **kwargs):
        if self.event.type() == QEvent.ToolTip and self.widget.toolTip():
            QToolTip.showText(self.event.globalPos(), "这是重载后的 tooltip", self.widget, QRect(), self.widget.toolTipDuration())
            return True
        else:
            self.event.ignore()

