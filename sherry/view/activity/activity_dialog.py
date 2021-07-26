# coding=utf-8
"""
    create by pymu
    on 2020/12/16
    at 11:19
     一般弹窗
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from sherry.inherit.activity import FrameLessWindowHintActivity
from sherry.view.ui.activity_dialog import Ui_Form


class NormalDialogActivity(FrameLessWindowHintActivity, Ui_Form):

    def __init__(self, info="消息提示", title="提示"):
        """一般弹窗, 继承自无边框窗体"""
        self.info = info
        self.title = title
        super(NormalDialogActivity, self).__init__()

    def place(self):
        """需要在父类界面渲染之前重构窗体"""
        main_layout = QHBoxLayout(self)
        self.body_widget = QWidget()
        self.setupUi(self.body_widget)
        main_layout.addWidget(self.body_widget)
        self.body_layout = self.body_widget.layout()
        super(NormalDialogActivity, self).place()

    def configure(self):
        super(NormalDialogActivity, self).configure()
        self.resize(300, 200)
        self.btn_bar_app_logo.setIcon(self.resource.project_png)
        self.btn_bar_app_logo.setIconSize(QSize(30, 30))
        self.btn_bar_title.setText(self.title)
        self.dialog_show_info.setText(self.info)
        self.btn_dialog_yes.setText("确认")
        self.btn_dialog_yes.setProperty(*self.resource.qss_value().btn_primary)
        self.btn_dialog_no.setText("取消")
        self.btn_bar_close.setIcon(self.resource.font_icon("fa.close", color="black"))
        self.btn_dialog_no.setHidden(True)
        self.event_flags.event_switch_border_bottom = False
        self.event_flags.event_switch_border_right = False
        self.event_flags.event_switch_border_bottom_right = False

    def set_signal(self):
        super(NormalDialogActivity, self).set_signal()
        self.btn_dialog_yes.clicked.connect(self.on_click_sure)
        self.btn_bar_close.clicked.connect(self.accept)

    def on_click_sure(self):
        """点击确认"""
        self.accept()
