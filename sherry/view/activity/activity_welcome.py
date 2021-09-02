# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发示例：
"""

from PyQt5.QtWidgets import QWidget

from sherry.core.badge import Badge
from sherry.core.paths import SherryPath
from sherry.inherit.activity import FrameLessWindowHintActivity
from sherry.view.prototype.prototype_activity_welcome import Ui_index_body


class WelcomeActivity(FrameLessWindowHintActivity, Ui_index_body):
    """图像来源：https://tieba.baidu.com/p/5273658104?pid=110599529244"""

    def __init__(self, *args, **kwargs):
        self.app_path = Badge(source=SherryPath, singleton=True)
        super(WelcomeActivity, self).__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置组件"""
        super(WelcomeActivity, self).place()
        content = QWidget()
        self.setupUi(content)
        self.body_layout.addWidget(content)
        self.body_layout.addStretch()
