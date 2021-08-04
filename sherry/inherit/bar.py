# encoding=utf-8
"""
    create by pymu
    on 2021/6/6
    at 2:09
"""

from sherry.inherit.component import Component


class BaseBar(Component):
    bar_normal = None  # 自定义标题栏的最大化最小化及关闭按钮
    bar_close = None
    bar_mini = None

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        if not master:
            raise ValueError("父类窗体不能为空")

    # noinspection PyUnresolvedReferences
    def set_signal(self):
        """设置标题栏信号"""
        super(BaseBar, self).set_signal()
        if not self.master:
            return
        if self.bar_normal:
            self.bar_normal.clicked.connect(self.change_normal)
        if self.bar_close:
            self.bar_close.clicked.connect(self.master.accept)
        if self.bar_mini:
            self.bar_mini.clicked.connect(self.master.showMinimized)

    def configure(self):
        super(BaseBar, self).configure()
        self.set_default_btn_icon()

    def set_default_btn_icon(self):
        """设置默认按钮图标"""
        if self.bar_normal:
            self.bar_normal.setIcon(self.resource.font_icon("fa.window-maximize", color="black"))
        if self.bar_mini:
            self.bar_mini.setIcon(self.resource.font_icon("fa.window-minimize", color="black"))
        if self.bar_close:
            self.bar_close.setIcon(self.resource.font_icon("fa.close", color="black"))

    # noinspection PyUnresolvedReferences
    def change_normal(self):
        """
        切换到恢复窗口大小按钮,
        """
        if not self.bar_normal:
            return
        self.master.layout().setContentsMargins(*[0] * 4)
        self.master.showMaximized()  # 先实现窗口最大化
        self.bar_normal.setIcon(self.resource.font_icon("fa.window-restore", color="black"))
        self.bar_normal.setToolTip("恢复")  # 更改按钮提示
        self.bar_normal.disconnect()  # 断开原本的信号槽连接
        self.bar_normal.clicked.connect(self.change_max)  # 重新连接信号和槽

    # noinspection PyUnresolvedReferences
    def change_max(self):
        """
        切换到最大化按钮
        """
        if not hasattr(self, "bar_normal"):
            return
        if not hasattr(self.master, "border_width"):
            self.master.border_width = 0
        self.master.layout().setContentsMargins(*[self.master.border_width] * 4)
        self.master.showNormal()
        self.bar_normal.setIcon(self.resource.font_icon("fa.window-maximize", color="black"))
        self.bar_normal.setToolTip("最大化")
        self.bar_normal.disconnect()  # 关闭信号与原始槽连接
        self.bar_normal.clicked.connect(self.change_normal)

    def mouseDoubleClickEvent(self, event):
        """鼠标双击(在y轴上小于标题栏高度的双击均被认为是双击头部，随后进行窗体的最大化跟恢复效果)"""
        if not self.bar_normal:
            return
        if event.pos().y() < self.y() + self.height():
            self.bar_normal.click()
