# coding=utf-8
"""
    create by pymu
    on 2021/8/11
    at 11:15
"""
from PyQt5.QtCore import QSize

from sherry.view.activity.activity_simple_theme import SimpleThemeActivity


class SimpleThemeDecoration(SimpleThemeActivity):

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        super(SimpleThemeDecoration, self).configure()
        self.set_default_btn_icon()
        translate = self.resource.translate
        self.pushButton_6.setToolTip(translate('Bar', "最大化"))
        self.pushButton_7.setToolTip(translate('Bar', "最小化"))
        self.pushButton_5.setToolTip(translate('Bar', "关闭"))
        # 内置的按钮样式
        self.pushButton_6.setObjectName('btn_bar_normal')
        self.pushButton_7.setObjectName('btn_bar_min')
        self.pushButton_5.setObjectName('btn_bar_close')
        self.bar = self.widget_3

        self.widget.setProperty('label_1', 'True')
        self.widget_3.setProperty('label_1', 'True')

    def set_default_btn_icon(self):
        """设置默认按钮图标"""
        self.pushButton_6.setIcon(self.resource.font_icon("fa.window-maximize", color="black"))
        self.pushButton_7.setIcon(self.resource.font_icon("fa.window-minimize", color="black"))
        self.pushButton_5.setIcon(self.resource.font_icon("fa.close", color="black"))
        self.pushButton.setIcon(self.resource.project_png)
        self.pushButton.setIconSize(QSize(30, 30))
        # self.pushButton.setText('')
