# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 2:01
"""
from qtpy.QtCore import QSize

from sherry.view.activity.componet_base_bar import BarComponent


class BaseBarDecoration(BarComponent):

    def configure(self):
        super(BaseBarDecoration, self).configure()
        self.btn_bar_app_name.setText(self.resource.translate("Bar", "默认标题栏一"))
        self.btn_bar_app_logo.setIcon(self.resource.project_png)
        self.btn_bar_app_logo.setIconSize(QSize(30, 30))
