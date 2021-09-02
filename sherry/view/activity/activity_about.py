# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 2:18
    页面描述
"""
from qtpy.QtWidgets import QWidget

from sherry.inherit.activity import FrameLessWindowHintActivity
from sherry.view.prototype.prototype_activity_about import Ui_Form


class AboutActivity(FrameLessWindowHintActivity, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置组件"""
        super(AboutActivity, self).place()
        content = QWidget()
        self.setupUi(content)
        self.body_layout.addWidget(content)
        self.body_layout.addStretch()
        self.center()
