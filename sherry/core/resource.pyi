# encoding=utf-8
"""
    create by pymu
    on 2021/5/8
    at 14:35
"""
from typing import Optional, Union

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QStyle, QApplication

from sherry.core.badge import T
from sherry.core.paths import SherryPath
from sherry.core.qss import Qss

app: Union[QApplication]


class ResourceLoader:
    path: SherryPath
    font_10: QFont
    font_11: QFont
    font_14: QFont
    font_16: QFont
    font_17: QFont
    project_icon: QIcon
    project_png: QIcon

    def __init__(self): ...

    @staticmethod
    def set_style(style: Optional[QStyle]): ...

    @staticmethod
    def set_theme(theme: str): ...

    @staticmethod
    def setAttribute(key, value): ...

    @staticmethod
    def exec(): ...

    @staticmethod
    def quit(): ...

    @staticmethod
    def __render_icon_by_path(path: str) -> QIcon: ...

    @staticmethod
    def __render_icon_by_path_convert(path: str) -> QIcon: ...

    def icon(self, name: str, convert: bool = False) -> QIcon: ...

    @staticmethod
    def font(size: int, weight: int = 2, family: str = "微软雅黑") -> QFont: ...

    @staticmethod
    def font_icon(font_str: str, color="white", *args, **kwargs) -> QIcon: ...

    def qss(self, *css_name: str) -> str: ...

    @staticmethod
    def qss_value(*qss: T, **kwargs) -> Union[Qss, T]: ...
