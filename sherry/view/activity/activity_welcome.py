# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发示例：
"""
import random

from PyQt5.QtWidgets import QWidget

import sherry
from sherry.core.badge import Badge
from sherry.core.paths import SherryPath
from sherry.inherit.activity import FrameLessWindowHintActivity
from sherry.view.prototype.activity_welcome import Ui_index_body


class WelcomeActivity(FrameLessWindowHintActivity, Ui_index_body):
    """图像来源：https://tieba.baidu.com/p/5273658104?pid=110599529244"""
    _base_show_img_style_ = """#index_show_image{border-image: var(--index_image); border-radius: 8px;}"""
    random_img = ["index-show-%s.png" % _ for _ in range(1, 6)]
    __u = ""

    def __init__(self, *args, **kwargs):
        self.app_path = Badge(source=SherryPath)
        super(WelcomeActivity, self).__init__(*args, **kwargs)

    def set_signal(self):
        super(WelcomeActivity, self).set_signal()
        self.index_close_btn.clicked.connect(self.accept)

    def place(self):
        """放置组件"""
        super(WelcomeActivity, self).place()
        content = QWidget()
        self.setupUi(content)
        self.body_layout.addWidget(content)
        self.body_layout.addStretch()

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        super(WelcomeActivity, self).configure()
        self.setWindowTitle("与君初相识，犹如故人归")
        self.body_widget.setObjectName("example_index_activity")
        effect = self.get_effect_shadow()
        self.set_widget_shadow(effect, self.index_show_image)
        self.set_random_image()
        self.index_show_image.setToolTip("by daylight.")
        self.event_flags.event_switch_border_bottom_right = False
        self.event_flags.event_switch_border_bottom = False
        self.event_flags.event_switch_border_right = False

    def mousePressEvent(self, event):
        """单机图像切换"""
        super(WelcomeActivity, self).mousePressEvent(event)
        widget = self.index_show_image
        x, w, y, h = widget.pos().x(), widget.width(), widget.pos().y(), widget.height()
        if x < event.pos().x() < x + w and y < event.pos().y() < y + h:
            self.set_random_image()

    def set_random_image(self):
        """随机返回一个"""
        while True:
            img_name = random.choice(list(self.random_img))
            if self.__u != img_name:
                self.__u = img_name
                break
        with open(self.app_path.file_path('sherry/index-show.html'), 'r', encoding='utf-8') as f:
            html = f.read()
            info = sherry.__sherry_info__
            html = html.replace("__document_url__", info["project_urls"]["Documentation"])
            html = html.replace("__project_url__", info["project_urls"]["Source"])
            self.index_text_show.setHtml(html)
        img_path = self.app_path.file_path('img/{}'.format(img_name))
        url = "url({})".format(img_path).replace("\\", "/")
        qss = self._base_show_img_style_.replace("var(--index_image)", url)
        self.index_show_image.setStyleSheet(qss)
