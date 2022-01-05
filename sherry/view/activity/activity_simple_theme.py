# coding=utf-8
"""
    create by pymu
    on 2021/8/8
    at 21:17
"""
from qtpy.QtWidgets import QWidget

from sherry.inherit.activity import FrameLessWindowHintActivity
from sherry.view.prototype.prototype_activity_simple_theme import Ui_Main


class SimpleThemeActivity(FrameLessWindowHintActivity, Ui_Main):

    def __init__(self, a=0):
        super().__init__()
        self.procedure()

    def place(self):
        super(SimpleThemeActivity, self).place()
        content = QWidget()
        self.setupUi(content)
        self.body_layout.addWidget(content)
