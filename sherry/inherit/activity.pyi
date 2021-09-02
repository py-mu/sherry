# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 0:11
"""
from typing import Optional, Callable, Dict

from qtpy.QtCore import QEvent, QAbstractAnimation, QPropertyAnimation
from qtpy.QtWidgets import QDialog, QWidget, QLayout

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
    fade_out_animation: QPropertyAnimation
    fade_in_animation: QPropertyAnimation
    signals: Dict[int, Callable]

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

    def center(self): ...

    def set_default_window_shadow(self): ...

    def event_flag(self, event: QEvent): ...

    def set_switch_animation(self, callback: Callable = None, duration: int = 100, start=1, end=0,
                             animation: QAbstractAnimation = None): ...
