# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 2:01
"""

from sherry.inherit.bar import BaseBar
from sherry.view.ui.component_base_bar import Ui_bar


class BarComponent(BaseBar, Ui_bar):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.procedure()

    def place(self):
        """
        如果标题的按钮名称与基类预留名称一致则不用赋值引用，否则需要把按钮迁移到当前类上
        即：self.bar_close = self.btn_bar_close
        """
        super(BarComponent, self).place()
        self.setupUi(self)
        self.bar_close = self.btn_bar_close
        self.bar_mini = self.btn_bar_min
        self.bar_normal = self.btn_bar_normal

    def configure(self):
        super(BarComponent, self).configure()
        self.btn_bar_app_name.setText(self.resource.translate("Bar", "默认标题栏一"))
        self.btn_bar_app_logo.setIcon(self.resource.project_png)
