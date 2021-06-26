# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 2:09
"""
from PyQt5.QtWidgets import QPushButton

from sherry.inherit.component import Component


class BaseBar(Component):
    bar_normal: QPushButton
    bar_close: QPushButton
    bar_mini: QPushButton

    def set_default_btn_icon(self): ...

    def change_normal(self): ...

    def change_max(self): ...
