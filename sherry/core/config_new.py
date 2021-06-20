# coding=utf-8
"""
    create by pymu
    on 2021/6/20
    at 17:11
"""
import sys

from PyQt5.QtWidgets import QApplication

import sherry
from sherry.common.paths import SherryPath
from sherry.core.style import ElementStyle
from sherry.inherit.badge import Badge


class ApplicationConfig:
    """
    属性项

    Project configuration class.
    """
    app = QApplication.instance() or QApplication(sys.argv)
    app_name = sherry.__name__
    app_version = sherry.__version__
    app_path = None

    def __init__(
            self,
            app=None,
            app_version=sherry.__version__,
            app_name=sherry.__name__,
            *args,
            **kwargs):
        app = app or self.app
        super().__init__(*args, **kwargs)
        self.app = app
        self.app_name = app_name
        self.app_version = app_version
        self.set_style()
        self.app_path = Badge(badge=SherryPath)

    def set_style(self, style=None or ElementStyle()):
        self.app.setStyle(style)

    def set_theme(self, theme):
        self.app.setStyleSheet(theme)
