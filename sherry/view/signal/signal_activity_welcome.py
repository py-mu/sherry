# coding=utf-8
"""
    create by pymu
    on 2021/8/7
    at 20:02
"""
import random

import sherry
from sherry.view.decoration.decoration_activity_welcome import WelcomeDecoration


class WelcomeSignal(WelcomeDecoration):
    _base_show_img_style_ = """#index_show_image{border-image: var(--index_image); border-radius: 8px;}"""
    random_img = ["index-show-%s.png" % _ for _ in range(1, 6)]
    __u = ""

    def set_signal(self):
        super(WelcomeSignal, self).set_signal()
        self.index_close_btn.clicked.connect(self.accept)

    def mousePressEvent(self, event):
        """单机图像切换"""
        super(WelcomeSignal, self).mousePressEvent(event)
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
