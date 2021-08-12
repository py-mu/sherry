# coding=utf-8
"""
    create by pymu
    on 2021/8/7
    at 19:44
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from sherry.inherit.activity import FrameLessWindowHintActivity
from sherry.view.activity.componet_base_bar import BarComponent
from sherry.view.prototype.prototype_example_designer_activity import Ui_Form


class DesignerActivity(FrameLessWindowHintActivity, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(DesignerActivity, self).__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置组件"""
        super(DesignerActivity, self).place()
        self.bar = self.get_bar()
        # noinspection PyArgumentList
        self.body_layout.addWidget(self.bar, alignment=Qt.AlignTop)
        content = QWidget()
        self.setupUi(content)
        self.body_layout.addWidget(content)

    def get_bar(self):
        return BarComponent(self)
