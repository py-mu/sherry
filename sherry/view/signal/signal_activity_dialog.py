# coding=utf-8
"""
    create by pymu
    on 2021/8/7
    at 19:37
"""
from sherry.view.decoration.decoration_activity_dialog import NormalDialogDecoration


class NormalDialogSignal(NormalDialogDecoration):

    def set_signal(self):
        super(NormalDialogSignal, self).set_signal()
        self.btn_dialog_yes.clicked.connect(self.on_click_sure)
        self.btn_bar_close.clicked.connect(self.accept)

    def on_click_sure(self):
        """点击确认"""
        self.accept()
