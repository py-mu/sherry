from typing import Tuple, Optional

from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QDialog, QWidget, QHBoxLayout

from sherry.core.view import BaseView


class BaseActivity(QDialog, BaseView):
    parent: QWidget

    def __init__(self, master: Optional[QWidget] = None, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...


class FrameLessWindowHintActivity(BaseActivity):

    body_widget: QWidget
    body_layout: QHBoxLayout
    bar: BaseView
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

        event_position_mouse: QPoint

    def event_flag(self, event: QtGui.QMouseEvent) -> Tuple[bool, bool, bool, bool]: ...

