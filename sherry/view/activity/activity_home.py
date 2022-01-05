# coding=utf-8
"""
    create by pymu
    on 2021/9/6
    at 17:12
"""

from sherry.inherit.component import Component
from sherry.view.prototype.prototype_activity_home import Ui_Form


class HomeActivity(Component, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """放置组件"""
        super(HomeActivity, self).place()
        self.setupUi(self)
