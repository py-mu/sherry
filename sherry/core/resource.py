# encoding=utf-8
"""
    create by pymu
    on 2021/5/8
    at 14:35
"""

import qtawesome
from PyQt5.QtGui import qGray, qRgba, qAlpha, QIcon, QPixmap, QFont

from sherry.common.utils.string import format_style_file
from sherry.core.config import ApplicationConfig


class ResourceLoader:
    """
    资源管理

    Simple resource loader.
    """

    def __init__(self):
        self.config = ApplicationConfig.instance()

        self.font_10 = self.font(10)
        self.font_11 = self.font(11)
        self.font_14 = self.font(14)
        self.font_16 = self.font(16)
        self.font_17 = self.font(17)

        self.project_icon = self.icon('icon.ico')
        self.project_png = self.icon('icon.png')

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
        icon.addPixmap(QPixmap.fromImage(image), QIcon.Normal, QIcon.On)
        return icon

    def icon(self, name, convert=False):
        """
        通过文件渲染 icon 对象(如果项目文件中不存则会查找pip包内部，不会报错)
        :param convert: 是否需要灰度转换
        :param name: 文件名
        """
        path = self.config.link(self.config.project_img_path, name)
        if not self.config.path_exists(path):
            path = self.config.link(self.config.package_img_path, name)
        if convert:
            return self.__render_icon_by_path_convert(path)
        return self.__render_icon_by_path(path)

    @staticmethod
    def font(size, weight=2, family="微软雅黑"):
        """
        创建一个字体，如此不必重复的
        实例化-设置-调用

        :param size: 大小
        :param weight: 权重
        :param family: 字体族
        """
        font = QFont()
        font.setWeight(weight)
        font.setFamily(family)
        font.setPointSize(size)
        return font

    @staticmethod
    def font_icon(font_str, color="white"):
        """
        字体图标,临时使用，
        重复调用建议使用方法生成

        :param color: 显示的颜色，是一个颜色描述单词，或者十六进制色，如 '#666' default ’white‘
        :param font_str 图标标识 如：'fa5.file-excel'
        """
        return qtawesome.icon(font_str, color=color)

    def qss(self, *css_name):
        """
        获取qss文件夹下的样式加载到容器中,
        样式优先级是由调用先后决定，
        即 先使用表[程序声明] < 后使用

        :param css_name: css 文件名, 可以是多个的
        :return: str 样式字符串
        """
        style_str = ""
        for file_name in css_name:
            path = self.config.link(self.config.project_qss_path, file_name)
            if not self.config.path_exists(path):
                path = self.config.link(self.config.package_qss_path, file_name)
            try:
                with open(path, encoding="utf-8") as f:
                    style_str += format_style_file(f.read(), self.config.package_resource_path)
            except FileNotFoundError:
                path = self.config.link(self.config.project_qss_path, file_name)
                raise FileNotFoundError(f"您确定您的项目目录下存在这个资源文件吗？{path}", )
        return style_str
