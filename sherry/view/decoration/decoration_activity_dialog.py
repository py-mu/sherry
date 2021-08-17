# coding=utf-8
"""
    create by pymu
    on 2020/12/16
    at 11:19
     一般弹窗
"""
from qtpy.QtCore import QSize

from sherry.view.activity.activity_dialog import NormalDialogActivity


class NormalDialogDecoration(NormalDialogActivity):

    def configure(self):
        super(NormalDialogDecoration, self).configure()
        self.resize(300, 200)
        self.btn_bar_app_logo.setIcon(self.resource.project_png)
        self.btn_bar_app_logo.setIconSize(QSize(30, 30))
        self.btn_bar_title.setText(self.title)
        self.dialog_show_info.setText(self.info)
        self.btn_dialog_yes.setText(self.resource.translate("Alert", "确认"))
        self.btn_dialog_yes.setProperty(*self.resource.qss_value().btn_primary)
        self.btn_dialog_no.setText(self.resource.translate("Alert", "取消"))
        self.btn_bar_close.setIcon(self.resource.font_icon("fa.close", color="black"))
        self.btn_dialog_no.setHidden(True)
        self.event_flags.event_switch_border_bottom = False
        self.event_flags.event_switch_border_right = False
        self.event_flags.event_switch_border_bottom_right = False
