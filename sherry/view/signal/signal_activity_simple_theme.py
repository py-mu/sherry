# coding=utf-8
"""
    create by pymu
    on 2021/8/11
    at 21:02
"""
from qtpy.QtCore import QPropertyAnimation, QEasingCurve
from qtpy.QtWidgets import QTreeWidgetItem

from sherry.view.decoration.decoration_activity_simple_theme import SimpleThemeDecoration


class SimpleThemeSignal(SimpleThemeDecoration):
    # 左侧展开的item 索引
    expanded_item = None
    tree_menu_action = None

    def set_signal(self):
        super(SimpleThemeSignal, self).set_signal()
        self.pushButton_6.clicked.connect(self.change_normal)
        self.pushButton_5.clicked.connect(self.accept)
        self.pushButton_7.clicked.connect(self.showMinimized)
        self.pushButton.clicked.connect(self.unfold_menu)
        self.pushButton_8.clicked.connect(self.unfold_menu)
        self.treeWidget.itemClicked.connect(self.tree_unfold)

    def change_normal(self):
        """
        切换到恢复窗口大小按钮,
        """
        self.layout().setContentsMargins(*[0] * 4)
        self.showMaximized()  # 先实现窗口最大化
        self.pushButton_6.setIcon(self.resource.font_icon("fa.window-restore", color="black"))
        self.pushButton_6.setToolTip(self.resource.translate('Bar', "恢复"))  # 更改按钮提示
        self.pushButton_6.disconnect()  # 断开原本的信号槽连接
        self.pushButton_6.clicked.connect(self.change_max)  # 重新连接信号和槽

    # noinspection PyUnresolvedReferences
    def change_max(self):
        """
        切换到最大化按钮
        """
        self.layout().setContentsMargins(*[self.border_width] * 4)
        self.showNormal()
        self.pushButton_6.setIcon(self.resource.font_icon("fa.window-maximize", color="black"))
        self.pushButton_6.setToolTip(self.resource.translate('Bar', "最大化"))
        self.pushButton_6.disconnect()  # 关闭信号与原始槽连接
        self.pushButton_6.clicked.connect(self.change_normal)

    def mouseDoubleClickEvent(self, event):
        """鼠标双击(在y轴上小于标题栏高度的双击均被认为是双击头部，随后进行窗体的最大化跟恢复效果)"""
        if self.bar and event.pos().y() < self.bar.y() + self.bar.height() \
                and event.pos().x() < self.bar.x() + self.bar.width():
            self.pushButton_6.click()

    def unfold_menu(self):
        """展开/收起菜单"""
        self.tree_menu_action = QPropertyAnimation(self.widget, b'minimumWidth')
        self.tree_menu_action.stop()
        mini_width = 60
        start = self.widget.width()
        if self.widget.width() > mini_width:
            icon = self.resource.font_icon('ei.chevron-right', color="#d2d2d2")
            end = mini_width
        else:
            icon = self.resource.font_icon('ei.chevron-left', color="#d2d2d2")
            end = 180
        self.pushButton_8.setIcon(icon)
        self.tree_menu_action.setStartValue(start)
        self.tree_menu_action.setEndValue(end)
        self.tree_menu_action.setEasingCurve(QEasingCurve.InOutBack)
        self.tree_menu_action.setDuration(500)
        self.tree_menu_action.start()

        # self.widget.setFixedWidth(width)

    def close_all_expand(self):
        """关闭所有非当前选中的展开"""
        for i in range(self.treeWidget.topLevelItemCount()):
            current_item = self.treeWidget.currentItem()
            current_top_index = self.treeWidget.indexOfTopLevelItem(current_item)
            top_level_item = self.treeWidget.topLevelItem(i)
            if current_top_index > -1 and id(current_item) != id(self.expanded_item) and top_level_item.isExpanded():
                top_level_item.setExpanded(False)

    def tree_unfold(self, item: QTreeWidgetItem):
        """
        点击存在子项的父类项，如果其没有展开则展开，
        同时关闭其他已经展开的top item，
        反之，若点击已经展开的item则将其关闭
        """
        if item.childCount():
            item = self.treeWidget.currentItem()
            if item.isExpanded():
                item.setExpanded(False)
                return
            item.setExpanded(True)
            index = self.treeWidget.indexOfTopLevelItem(item)
            if index > -1:
                self.expanded_item = item
        self.close_all_expand()
