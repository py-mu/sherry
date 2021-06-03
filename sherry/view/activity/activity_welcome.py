# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发示例：
"""
from PyQt5.QtWidgets import QWidget

from sherry.core.activity import FrameLessWindowHintActivity
from sherry.view.ui.example_welcome_activity import Ui_index_body


class WelcomeActivity(FrameLessWindowHintActivity, Ui_index_body):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_signal(self):
        super(WelcomeActivity, self).set_signal()
        self.index_close_btn.clicked.connect(self.accept)

    def place(self):
        """放置组件"""
        super(WelcomeActivity, self).place()
        content = QWidget()
        self.setupUi(content)
        self.body_layout.addWidget(content)
        self.body_layout.addStretch()

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        super(WelcomeActivity, self).configure()
        self.body_widget.setObjectName("example_index_activity")
        effect = self.get_effect_shadow()
        self.set_widget_shadow(effect, self.index_show_image)
        self.event_flags.event_switch_border_bottom_right = False
        self.event_flags.event_switch_border_bottom = False
        self.event_flags.event_switch_border_right = False
