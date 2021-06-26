# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 17:08
"""

from PyQt5.QtWidgets import (QStyle, QProxyStyle, QStyleOptionProgressBar)


class ElementStyle(QProxyStyle):
    """https://doc.qt.io/archives/qt-4.8/qstyle.html"""

    def polish(self, widget):
        """
        安装 GUI 的某控件的某一功能，启用该行为

        用于初始化部件的外观，会在部件创建完成之后，在第一次显示之前被调用，默认实现什么也不做。
        子类化 QStyle 时，可利用以上函数的调用时机，对部件的一些属性 进行初始化。
        """
        a = super().polish(widget)
        # if isinstance(widget, QPushButton):
        #     widget.setAttribute(Qt.WA_Hover, False)

        return a

    def unpolish(self, widget):
        """
        卸载 GUI 的某控件的某一功能，禁用该行为
        作用和　polish()　相似，但只有在部件被销毁时才会被调用。
        """
        return super().unpolish(widget)

    def styleHint(self, hint, option=None, widget=None, return_data=None):
        """开启或关闭某一 GUI 的控件的行为，或开启选择指定的某种特性"""
        return super().styleHint(hint, option, widget, return_data)

    def drawPrimitive(self, element, option, painter, widget=None):
        return super().drawPrimitive(element, option, painter, widget)

    def drawControl(self, element, option, painter, widget=None):
        """绘画 GUI 某一控件的某一部分(控制元素)"""
        if isinstance(option, QStyleOptionProgressBar):
            option.rect = self.proxy().subElementRect(QStyle.SE_ProgressBarContents, option, widget)
            super().drawControl(QStyle.CE_ProgressBarGroove, option, painter, widget)

        result = super().drawControl(element, option, painter, widget)
        return result

    def subElementRect(self, element, option, widget):
        """返回某一个元素的矩形大小；由样式选项 option 所描述的控件的子元素 subElement 的矩形；"""
        return super().subElementRect(element, option, widget)

    def drawComplexControl(self, control, option, painter, widget=None):
        """绘画 GUI 某一浮渣控件的元素，将该控件的每一个部分都绘画分派出去，调用 drawControl() 里面对应的枚举。"""
        return super().drawComplexControl(control, option, painter, widget)

    def subControlRect(self, cc, opt, sc, widget):
        """返回一个 GUI 的复杂控件 cc 的子控件 subControl 的矩形"""
        return super().subControlRect(cc, opt, sc, widget)

    def pixelMetric(self, metric, option=None, widget=None):
        """返回某一个元素的长度"""
        return super().pixelMetric(metric, option, widget)

    def sizeFromContents(self, _type, option, size, widget):
        """ 返回某一 GUI 控件的中心矩形的大小"""
        return super().sizeFromContents(_type, option, size, widget)
