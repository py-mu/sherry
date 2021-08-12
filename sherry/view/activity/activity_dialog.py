# coding=utf-8
"""
    create by pymu
    on 2021/8/7
    at 19:39
"""
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from sherry.inherit.activity import FrameLessWindowHintActivity
from sherry.view.prototype.prototype_activity_dialog import Ui_Form


class NormalDialogActivity(FrameLessWindowHintActivity, Ui_Form):

    def __init__(self, info="消息提示", title="提示"):
        """一般弹窗, 继承自无边框窗体"""
        super(NormalDialogActivity, self).__init__()
        self.info = self.resource.translate("Alert", info)
        self.title = self.resource.translate("Alert", title)
        self.procedure()

    def place(self):
        """需要在父类界面渲染之前重构窗体"""
        main_layout = QHBoxLayout(self)
        self.body_widget = QWidget()
        self.setupUi(self.body_widget)
        main_layout.addWidget(self.body_widget)
        self.body_layout = self.body_widget.layout()
        super(NormalDialogActivity, self).place()
