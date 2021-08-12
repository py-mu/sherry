# coding=utf-8
"""
    create by pymu
    on 2021/8/11
    at 21:02
"""
from sherry.view.decoration.decoration_activity_simple_theme import SimpleThemeDecoration


class SimpleThemeSignal(SimpleThemeDecoration):

    def set_signal(self):
        super(SimpleThemeSignal, self).set_signal()
        self.pushButton_6.clicked.connect(self.change_normal)
        self.pushButton_5.clicked.connect(self.accept)
        self.pushButton_7.clicked.connect(self.showMinimized)

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
        if self.bar and event.pos().y() < self.bar.y() + self.bar.height():
            self.pushButton_6.click()
