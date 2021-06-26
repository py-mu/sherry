# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:30
"""
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QWidget


class EventCell:
    """装载单元"""
    widget: QWidget
    event: QEvent

    def __init__(self, widget: QWidget, event: QEvent): ...

    def __hash__(self): ...

    def __call__(self, *args, **kwargs): ...


class TooltipEvent(EventCell):

    def __call__(self, *args, **kwargs): ...
