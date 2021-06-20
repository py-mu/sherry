from typing import Optional

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QPushButton, QWidget

from sherry.inherit.component import Component


class BaseBar(Component):
    bar_normal: Optional[QPushButton]
    bar_close: Optional[QPushButton]
    bar_mini: Optional[QPushButton]

    def __init__(self, master: QWidget, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

    def set_default_btn_icon(self): ...

    def change_normal(self): ...

    def change_max(self): ...

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None: ...
