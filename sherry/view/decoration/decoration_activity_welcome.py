# coding=utf-8
"""
    create by pymu
    on 2020/12/31
    at 9:37
    使用EQ开发示例：
"""

from sherry.view.activity.activity_welcome import WelcomeActivity


class WelcomeDecoration(WelcomeActivity):

    def configure(self):
        """配置页面及控件属性, 要分清哪些是需要在重写之前，哪些是在重写之后哦"""
        super(WelcomeDecoration, self).configure()
        self.setWindowTitle("与君初相识，犹如故人归")
        self.body_widget.setObjectName("example_index_activity")
        effect = self.get_effect_shadow()
        self.set_widget_shadow(effect, self.index_show_image)
        self.set_random_image()
        self.index_show_image.setToolTip("by daylight.")
        self.event_flags.event_switch_border_bottom_right = False
        self.event_flags.event_switch_border_bottom = False
        self.event_flags.event_switch_border_right = False
