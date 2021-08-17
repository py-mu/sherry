# encoding=utf-8
"""
    create by pymu
    on 2021/5/8
    at 14:35
"""
from typing import Optional, Union

from qtpy.QtCore import QTranslator
from qtpy.QtGui import QIcon, QFont
from qtpy.QtWidgets import QStyle, QApplication

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

    def add_font(self, font_name: str) -> int: ...

    def __raise_file_not_found(self, path: str): ...

    @staticmethod
    def set_style(style: Optional[QStyle]): ...

    @staticmethod
    def set_theme(theme: str): ...

    @staticmethod
    def set_translate(tran: QTranslator): ...

    @staticmethod
    def setAttribute(key, value): ...

    @staticmethod
    def translate(base: str, text: str): ...

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
    def font(size: int, weight: int = 2) -> QFont: ...

    @staticmethod
    def font_icon(font_str: str, color="white", *args, **kwargs) -> QIcon: ...

    def qss(self, *css_name: str) -> str: ...

    @staticmethod
    def qss_value(*qss: T, **kwargs) -> Union[Qss, T]: ...
