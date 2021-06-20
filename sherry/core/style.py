# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 17:08
"""
from typing import Optional

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QWidget, QStyle, QStyleOption, QStyleHintReturn, QProxyStyle, QStyleOptionComplex,
                             QStyleOptionProgressBar)


class ElementStyle(QProxyStyle):
    """https://doc.qt.io/archives/qt-4.8/qstyle.html"""

    def polish(self, widget: QWidget) -> None:
        """
        安装 GUI 的某控件的某一功能，启用该行为

        用于初始化部件的外观，会在部件创建完成之后，在第一次显示之前被调用，默认实现什么也不做。
        子类化 QStyle 时，可利用以上函数的调用时机，对部件的一些属性 进行初始化。
        """
        a = super(ElementStyle, self).polish(widget)
        # if isinstance(widget, QPushButton):
        #     widget.setAttribute(Qt.WA_Hover, False)

        return a

    def unpolish(self, widget: QWidget) -> None:
        """
        卸载 GUI 的某控件的某一功能，禁用该行为
        作用和　polish()　相似，但只有在部件被销毁时才会被调用。
        """
        return super(ElementStyle, self).unpolish(widget)

    def styleHint(self, hint: QStyle.StyleHint, option: Optional[QStyleOption] = ..., widget: Optional[QWidget] = ...,
                  return_data: Optional[QStyleHintReturn] = ...) -> int:
        """开启或关闭某一 GUI 的控件的行为，或开启选择指定的某种特性"""
        return super(ElementStyle, self).styleHint(hint, option, widget, return_data)

    def drawPrimitive(self, element: QStyle.PrimitiveElement, option: QStyleOption, painter: QtGui.QPainter,
                      widget: Optional[QWidget] = ...) -> None:
        return super(ElementStyle, self).drawPrimitive(element, option, painter, widget)

    def drawControl(self, element: QStyle.ControlElement, option: QStyleOption, painter: QtGui.QPainter,
                    widget: Optional[QWidget] = ...) -> None:
        """绘画 GUI 某一控件的某一部分(控制元素)"""
        if isinstance(option, QStyleOptionProgressBar):
            option: QStyleOptionProgressBar
            # self.proxy().drawControl(QStyle.CE_ProgressBarGroove, option, painter, widget)
            option.rect = self.proxy().subElementRect(QStyle.SE_ProgressBarContents, option, widget)
            super(ElementStyle, self).drawControl(QStyle.CE_ProgressBarGroove, option, painter, widget)

        result = super(ElementStyle, self).drawControl(element, option, painter, widget)
        return result

    def subElementRect(self, element: QStyle.SubElement, option: QStyleOption, widget: QWidget) -> QtCore.QRect:
        """返回某一个元素的矩形大小；由样式选项 option 所描述的控件的子元素 subElement 的矩形；"""
        return super(ElementStyle, self).subElementRect(element, option, widget)

    def drawComplexControl(self, control: QStyle.ComplexControl, option: QStyleOptionComplex, painter: QtGui.QPainter,
                           widget: Optional[QWidget] = ...) -> None:
        """绘画 GUI 某一浮渣控件的元素，将该控件的每一个部分都绘画分派出去，调用 drawControl() 里面对应的枚举。"""
        return super(ElementStyle, self).drawComplexControl(control, option, painter, widget)

    def subControlRect(self, cc: QStyle.ComplexControl, opt: QStyleOptionComplex, sc: QStyle.SubControl,
                       widget: QWidget) -> QtCore.QRect:
        """返回一个 GUI 的复杂控件 cc 的子控件 subControl 的矩形"""
        return super(ElementStyle, self).subControlRect(cc, opt, sc, widget)

    def pixelMetric(self, metric: QStyle.PixelMetric, option: Optional[QStyleOption] = ...,
                    widget: Optional[QWidget] = ...) -> int:
        """返回某一个元素的长度"""
        return super(ElementStyle, self).pixelMetric(metric, option, widget)

    def sizeFromContents(self, _type: QStyle.ContentsType, option: QStyleOption, size: QtCore.QSize,
                         widget: QWidget) -> QtCore.QSize:
        """ 返回某一 GUI 控件的中心矩形的大小"""
        return super(ElementStyle, self).sizeFromContents(_type, option, size, widget)
