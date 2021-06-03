from PyQt5.QtGui import QFont, QIcon

from sherry.core.config import ApplicationConfig


class ResourceLoader:
    # default font
    font_10: QFont
    font_11: QFont
    font_14: QFont
    font_16: QFont
    font_17: QFont

    project_icon: QIcon
    project_png: QIcon

    config: ApplicationConfig

    @staticmethod
    def __render_icon_by_path(path: str) -> QIcon: ...

    @staticmethod
    def __render_icon_by_path_convert(path: str) -> QIcon: ...

    def icon(self, name: str, convert=False) -> QIcon: ...

    @staticmethod
    def font(size: int, weight: int = 2, family: str = "微软雅黑") -> QFont: ...

    @staticmethod
    def font_icon(font_str: str, color="white") -> QIcon: ...

    def qss(self, *css_name: str) -> str: ...
