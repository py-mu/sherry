import sys
from typing import Optional

from PyQt5.QtWidgets import QApplication, QStyle

import sherry
from sherry.inherit.bean import Bean


class BaseConfiguration(Bean):

    @classmethod
    def path_exists(cls, path: str) -> bool: ...

    @classmethod
    def path_create(cls, path: str) -> str: ...

    @classmethod
    def link(cls, source: str, target: str, create: bool = False) -> str: ...

    @property
    def package_path(self) -> str: ...

    @property
    def package_resource_path(self) -> str: ...

    @property
    def package_qss_path(self) -> str: ...

    @property
    def package_img_path(self) -> str: ...

    @property
    def project_path(self) -> str: ...

    @property
    def project_resource_path(self) -> str: ...

    @property
    def project_img_path(self) -> str: ...

    @property
    def project_qss_path(self) -> str: ...

    @property
    def log_path(self) -> str: ...

    @property
    def user_home(self) -> str: ...

    @property
    def user_desktop(self) -> str: ...

    def file_path(self, file_name: str) -> str: ...


class ApplicationConfig(BaseConfiguration):
    app: QApplication
    app_version: str
    app_name: str
    app_author: str

    def __init__(
            self,
            app: QApplication = QApplication.instance() or QApplication(sys.argv),
            app_version: str = sherry.__version__,
            app_name: str = sherry.__name__,
            *args,
            **kwargs): ...

    def set_style(self, style: Optional[QStyle] = None): ...

    def set_theme(self, theme: str): ...
