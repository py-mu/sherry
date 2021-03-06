# encoding=utf-8
"""
    create by pymu
    on 2021/5/8
    at 14:35
"""
import logging
import os
import sys

import qtawesome
from qtpy.QtCore import Qt
from qtpy.QtGui import qGray, qRgba, qAlpha, QIcon, QPixmap, QFont, QFontDatabase
from qtpy.QtWidgets import QApplication

from sherry.core.badge import Badge
from sherry.core.paths import SherryPath
from sherry.core.qss import Qss
from sherry.inherit.style import ElementStyle
from sherry.utils.string import format_style_file

app = QApplication.instance() or QApplication(sys.argv)  # QT app


class ResourceLoader:
    """
    资源管理

    Simple resource loader.
    """

    def __init__(self):
        self.path = Badge(source=SherryPath, singleton=True)
        self.font_10 = self.font(10)
        self.font_11 = self.font(11)
        self.font_14 = self.font(14)
        self.font_16 = self.font(16)
        self.font_17 = self.font(17)

        self.project_icon = self.icon('icon.ico')
        self.project_png = self.icon('icon.png')

    def add_font(self, font_name):
        """添加字体"""
        path = self.path.get_path_in(
            self.path.project_font_path,
            self.path.package_font_path,
            name=font_name
        )
        if not path:
            path = self.path.link(self.path.project_font_path, font_name)
            self.__raise_file_not_found(path)
        QFontDatabase().addApplicationFont(path)

    def __raise_file_not_found(self, path):
        """抛出文件查找不到"""
        raise FileNotFoundError(
            "Are you sure that this resource file exists in your project directory? path: {path}".format(path=path), )

    @staticmethod
    def set_style(style=None or ElementStyle()):
        app.setStyle(style)

    @staticmethod
    def set_theme(theme):
        """设置样式表， set stylesheet"""
        app.setStyleSheet(theme)

    @staticmethod
    def set_translate(tran):
        app.installTranslator(tran)

    @staticmethod
    def setAttribute(key, value):
        """设置q app 属性"""
        app.setAttribute(key, value)

    @staticmethod
    def translate(base, text):
        """国际化"""
        return app.translate(base, text)

    @staticmethod
    def exec():
        """qt 事件循环"""
        app.exec_()

    @staticmethod
    def quit():
        """退出程序"""
        app.quit()

    @staticmethod
    def __render_icon_by_path(path):
        """
        通过路径渲染出一个icon图像

        Render an ico image through the path.

        :param path: 图像地址 image path
        :return: QtGui.QIcon对象 icon object
        """
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.On)
        return icon

    @staticmethod
    def __render_icon_by_path_convert(path):
        """
        返回灰度icon

        Back to gray icon.

        :param path: 图像地址 image path
        """
        icon = QIcon()
        image = QPixmap(path).toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                color = image.pixel(x, y)
                gray = qGray(color)
                image.setPixel(x, y, qRgba(gray, gray, gray, qAlpha(color)))
        icon.addPixmap(QPixmap().fromImage(image, Qt.ImageConversionFlags), QIcon.Normal, QIcon.On)
        return icon

    def icon(self, name, convert=False):
        """
        通过文件渲染 icon 对象(如果项目文件中不存则会查找pip包内部，不会报错)
        :param convert: 是否需要灰度转换
        :param name: 文件名
        """
        project_path, package_path = self.path.project_img_path, self.path.package_img_path
        path = self.path.get_path_in(project_path, package_path, name=name)
        if not path:
            logging.warning(
                "cant't find the image file in path '%s' or '%s' name called %s" % (project_path, package_path, name))
        if convert:
            return self.__render_icon_by_path_convert(path)
        return self.__render_icon_by_path(path)

    @staticmethod
    def font(size, weight=2):
        """
        创建一个字体，如此不必重复的
        实例化-设置-调用

        :param size: 大小
        :param weight: 权重
        """
        font = QFont()
        font.setWeight(weight)
        font.setPointSize(size)
        return font

    @staticmethod
    def font_icon(font_str, color="white", *args, **kwargs):
        """
        字体图标,临时使用，
        重复调用建议使用方法生成
        see: https://github.com/spyder-ide/qtawesome

        :param color: 显示的颜色，是一个颜色描述单词，或者十六进制色，如 '#666' default ’white‘
        :param font_str 图标标识 如：'fa5.file-excel'
        """
        return qtawesome.icon(font_str, *args, color=color, **kwargs)

    def qss(self, *css_name):
        """
        获取qss文件夹下的样式加载到容器中,
        样式优先级是由调用先后决定，
        即 先使用表[程序声明] < 后使用

        :param css_name: css 文件名, 可以是多个的
        :return: str 样式字符串
        """
        css_name = css_name or ('element.css',)
        style_str = ""
        for file_name in css_name:
            path = self.path.get_path_in(self.path.project_qss_path, self.path.package_qss_path, name=file_name)
            if not path:
                path = self.path.link(self.path.project_qss_path, file_name)
                self.__raise_file_not_found(path)
            root = os.path.commonpath([self.path.project_path, path, self.path.package_path])
            with open(path, encoding="utf-8") as f:
                style_str += format_style_file(f.read(), root)
        return style_str

    @staticmethod
    def qss_value(*qss, **kwargs):
        if not qss:
            qss = Qss,

        class CQss(type('_QSS', qss, kwargs)):
            def __getattribute__(self, item):
                """读取样式，如果是其他类的属性那应该直接返回"""
                _property_ = super(CQss, self).__getattribute__(item)
                if isinstance(_property_, str) and item in Qss.__dict__ and "_" in item:
                    return item, "True"
                return _property_

        return CQss()
