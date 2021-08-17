# coding=utf-8
"""
    create by pymu
    on 2021/8/12
    at 20:37
"""
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QTreeWidgetItem

from sherry.view.activity.activity_simple_theme import SimpleThemeActivity


class SimpleThemeDigital(SimpleThemeActivity):

    def procedure(self):
        super(SimpleThemeDigital, self).procedure()
        self.add_menu()

    def add_menu(self):
        item = QTreeWidgetItem(self.treeWidget)
        item.setIcon(0, self.resource.project_png)
        item.setText(0, '    测试')
        item.setBackground(1, QBrush(QColor("#333")))
        item.setDisabled(True)
