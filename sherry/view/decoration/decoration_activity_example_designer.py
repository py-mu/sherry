# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 2:18
    页面描述
"""
from PyQt5.QtWidgets import QAbstractItemView

from sherry.core.badge import Badge
from sherry.view.activity.activity_example_designer import DesignerActivity
from sherry.view.activity.componet_base_bar import BarComponent


class DesignerDecoration(DesignerActivity):
    """基本样式类"""

    def get_bar(self):
        return Badge(self, source=BarComponent)

    def configure(self):
        """配置页面及控件属性"""
        super(DesignerDecoration, self).configure()
        self.move(340, 0)
        # 常用按钮
        self.pushButton.setIcon(self.resource.font_icon('fa.frown-o', 'red'))
        self.pushButton_2.setProperty(*self.resource.qss_value().btn_primary)
        self.pushButton_3.setProperty(*self.resource.qss_value().btn_success)
        self.pushButton_4.setProperty(*self.resource.qss_value().btn_warning)
        self.pushButton_5.setProperty(*self.resource.qss_value().btn_danger)
        self.pushButton_6.setProperty(*self.resource.qss_value().btn_info)
        self.pushButton_7.setDisabled(True)

        # 朴素按钮
        self.pushButton_8.setProperty(*self.resource.qss_value().btn_style_simplicity)

        self.pushButton_9.setProperty(*self.resource.qss_value().btn_style_simplicity)
        self.pushButton_9.setProperty(*self.resource.qss_value().btn_primary)

        self.pushButton_10.setProperty(*self.resource.qss_value().btn_style_simplicity)
        self.pushButton_10.setProperty(*self.resource.qss_value().btn_success)

        self.pushButton_11.setProperty(*self.resource.qss_value().btn_style_simplicity)
        self.pushButton_11.setProperty(*self.resource.qss_value().btn_warning)

        self.pushButton_12.setProperty(*self.resource.qss_value().btn_style_simplicity)
        self.pushButton_12.setProperty(*self.resource.qss_value().btn_danger)

        self.pushButton_13.setProperty(*self.resource.qss_value().btn_style_simplicity)
        self.pushButton_13.setProperty(*self.resource.qss_value().btn_info)
        # self.pushButton_3.setText(r'\e6ad')

        self.pushButton_14.setDisabled(True)

        # 按钮大小
        self.pushButton_17.setProperty("btn_size_small", "True")
        self.pushButton_18.setProperty("btn_size_mini", "True")

        # 单选按钮
        # self.radioButton_2.setProperty('radio_primary', 'True')
        self.radioButton_3.setDisabled(True)

        # 复选框
        self.checkBox_3.setDisabled(True)

        self.lineEdit_3.setDisabled(True)

        # self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader()
        # self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # print(self.tableWidget.verticalHeader().property('enabled'))

        self.textEdit.setToolTip("测试123213")
        self.plainTextEdit.setToolTip('sssssss')
        self.textEdit_2.setToolTip('1232222')
