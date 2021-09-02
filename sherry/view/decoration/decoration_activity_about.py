# coding=utf-8
"""
    create by pymu
    on 2021/8/18
    at 20:29
"""
from qtpy.QtCore import QSize

from sherry.view.activity.activity_about import AboutActivity


class AboutDecoration(AboutActivity):

    def configure(self):
        super(AboutDecoration, self).configure()
        self.resize(500, 300)
        self.event_flags.event_switch_border_bottom_right = False
        self.event_flags.event_switch_border_bottom = False
        self.event_flags.event_switch_border_right = False
        self.pushButton.setProperty('icon_button', 'True')
        self.pushButton_2.setObjectName('btn_bar_close')
        self.pushButton_2.setIcon(self.resource.font_icon("fa.close", color="black"))
        self.pushButton.resize(70, 70)
        self.pushButton.setIconSize(QSize(60, 60))
        self.pushButton.setIcon(self.resource.project_png)
        self.groupBox.setProperty('label_center', 'True')
        self.groupBox_2.setProperty('label_center', 'True')
        self.label_3.setProperty('label_1', 'True')
        self.bar = self

    def set_signal(self):
        super(AboutDecoration, self).set_signal()
        self.pushButton_2.clicked.connect(self.accept)
