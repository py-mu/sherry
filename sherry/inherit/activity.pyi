# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 0:11
"""
from typing import Optional

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QDialog, QWidget, QLayout

from sherry.inherit.view import BaseView


class BaseActivity(QDialog, BaseView):
    """
    默认的窗口级组件
    """


class FrameLessWindowHintActivity(BaseActivity):
    body_widget: Optional[QWidget]
    body_layout: Optional[QLayout]
    bar: Optional[QWidget]
    border_width: int

    class EventFlags:
        event_flag_bar_move: bool
        event_flag_border_left: bool
        event_flag_border_right: bool
        event_flag_border_top: bool
        event_flag_border_bottom: bool
        event_flag_border_top_left: bool
        event_flag_border_top_right: bool
        event_flag_border_bottom_left: bool
        event_flag_border_bottom_right: bool

        event_switch_border_left: bool
        event_switch_border_right: bool
        event_switch_border_top: bool
        event_switch_border_bottom: bool
        event_switch_border_top_left: bool
        event_switch_border_top_right: bool
        event_switch_border_bottom_left: bool
        event_switch_border_bottom_right: bool

        event_position_mouse = None

    def set_default_window_shadow(self): ...

    def event_flag(self, event: QEvent): ...
