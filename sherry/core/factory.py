# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 0:31
"""
import sys
from dataclasses import dataclass, field

from PyQt5.QtWidgets import QApplication

from sherry.core.config import ApplicationConfig


@dataclass
class ConfigurationFactory:
    """"""
    app: QApplication = field(default=QApplication.instance() or QApplication(sys.argv))  # Note: 全局QT实例
    config: ApplicationConfig = field(default=ApplicationConfig())  # Note: 全局配置项


config = ConfigurationFactory()
