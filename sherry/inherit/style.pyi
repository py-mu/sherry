# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 17:08
"""
from typing import Optional

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QWidget, QStyle, QStyleOption, QStyleHintReturn, QProxyStyle, QStyleOptionComplex)


class ElementStyle(QProxyStyle):
    """https://doc.qt.io/archives/qt-4.8/qstyle.html"""

    def polish(self: QProxyStyle, widget: QWidget) -> None: ...

    def unpolish(self: QProxyStyle, widget: QWidget) -> None: ...

    def styleHint(self: QProxyStyle, hint: QStyle.StyleHint, option: Optional[QStyleOption] = ..., widget: Optional[QWidget] = ...,
                  return_data: Optional[QStyleHintReturn] = ...) -> int: ...

    def drawPrimitive(self: QProxyStyle, element: QStyle.PrimitiveElement, option: QStyleOption, painter: QtGui.QPainter,
                      widget: Optional[QWidget] = ...) -> None: ...

    def drawControl(self: QProxyStyle, element: QStyle.ControlElement, option: QStyleOption, painter: QtGui.QPainter,
                    widget: Optional[QWidget] = ...) -> None: ...

    def subElementRect(self: QProxyStyle, element: QStyle.SubElement, option: QStyleOption, widget: QWidget) -> QtCore.QRect: ...

    def drawComplexControl(self: QProxyStyle, control: QStyle.ComplexControl, option: QStyleOptionComplex, painter: QtGui.QPainter,
                           widget: Optional[QWidget] = ...) -> None: ...

    def subControlRect(self: QProxyStyle, cc: QStyle.ComplexControl, opt: QStyleOptionComplex, sc: QStyle.SubControl,
                       widget: QWidget) -> QtCore.QRect: ...

    def pixelMetric(self: QProxyStyle, metric: QStyle.PixelMetric, option: Optional[QStyleOption] = ...,
                    widget: Optional[QWidget] = ...) -> int: ...

    def sizeFromContents(self: QProxyStyle, _type: QStyle.ContentsType, option: QStyleOption, size: QtCore.QSize,
                         widget: QWidget) -> QtCore.QSize: ...
