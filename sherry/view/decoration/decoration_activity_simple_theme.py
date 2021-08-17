# coding=utf-8
"""
    create by pymu
    on 2021/8/11
    at 11:15
"""
from PyQt5.QtCore import QSize

from sherry.view.digital.digital_activity_simple_theme import SimpleThemeDigital


class SimpleThemeDecoration(SimpleThemeDigital):

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
        # 关闭双击展开
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.pushButton.setProperty('icon_button', 'True')
        self.pushButton_2.setProperty('icon_button', 'True')
        self.pushButton_3.setProperty('icon_button', 'True')
        self.pushButton_8.setProperty('icon_button', 'True')

        self.widget_5.setProperty('content_border', 'True')
        self.treeWidget.setProperty('menu_tree', 'True')
        # 子项Item与顶层TopLevelItem顶端对其
        self.treeWidget.setIndentation(0)
        # 设置其icon的大小
        self.treeWidget.setIconSize(QSize(30, 30))

    def set_default_btn_icon(self):
        """设置默认按钮图标"""
        self.pushButton.setIcon(self.resource.project_png)
        self.pushButton_2.setIcon(self.resource.font_icon('fa.question-circle', color="black"))
        self.pushButton_8.setIcon(self.resource.font_icon('ei.chevron-left', color="#d2d2d2"))
        self.pushButton_3.setIcon(self.resource.font_icon('fa.cog', color="black"))
        self.pushButton_6.setIcon(self.resource.font_icon("fa.window-maximize", color="black"))
        self.pushButton_7.setIcon(self.resource.font_icon("fa.window-minimize", color="black"))
        self.pushButton_5.setIcon(self.resource.font_icon("fa.close", color="black"))
