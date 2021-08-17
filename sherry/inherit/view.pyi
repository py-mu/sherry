from typing import Optional, Union, Tuple

from qtpy import QtGui
from qtpy.QtCore import Qt, QEvent
from qtpy.QtGui import QColor, QGradient, QMouseEvent
from qtpy.QtWidgets import QWidget, QGraphicsDropShadowEffect

from sherry.core.resource import ResourceLoader


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
