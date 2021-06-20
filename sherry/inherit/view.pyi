from typing import Optional, Union, Tuple, Any

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QColor, QGradient, QMouseEvent
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect

from sherry.core.resource import ResourceLoader
from sherry.view.component.tooltip import Tooltip

tooltip: Tooltip
# inherit old QWidget event function
old_func: Any


class BaseView(QWidget):
    resource: ResourceLoader
    master: Optional[QWidget]

    def __init__(self, master: Optional[QWidget] = None, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

    def set_signal(self): ...

    def configure(self): ...

    def procedure(self): ...

    def place(self): ...

    def get_effect_shadow(self,
                          offset: Tuple[int, int] = (0, 0),
                          radius: int = 10,
                          color: Union[
                              QColor, Qt.GlobalColor, QGradient] = Qt.darkGray) -> QGraphicsDropShadowEffect: ...

    @staticmethod
    def set_widget_shadow(shadow: QGraphicsDropShadowEffect, widget: QWidget): ...

    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...

    def showEvent(self, event: QtGui.QShowEvent) -> None: ...

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...

    def mousePressEvent(self, event: QMouseEvent) -> None: ...

    def mouseMoveEvent(self, event: QMouseEvent) -> None: ...

    def mouseReleaseEvent(self, event: QMouseEvent) -> None: ...

    def event(self, event: QEvent) -> bool: ...
