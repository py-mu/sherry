# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 20:03
"""


def qss_style(*qss, **kwargs):
    qss = qss or Qss,

    class CQss(type('QSS', qss, kwargs)):
        def __getattribute__(self, item):
            """读取样式，如果是其他类的属性那应该直接返回"""
            _property_ = super(CQss, self).__getattribute__(item)
            if isinstance(_property_, str) and item in Qss.__dict__ and "_" in item:
                return item, "True"
            return _property_

    return CQss()


class Qss:
    """"""

    # 容器类
    widget_primary = "基本容器"
    frame_primary = "基本容器"

    # 使用元组放置属性筛选描述
    btn_style_simplicity = "朴素按钮, 按钮的另一种形式，可以与其他按钮样式组合"
    btn_primary = "原始按钮，不被注意的按钮如取消"
    btn_warning = "警告按钮，橙黄色带有冲击性的颜色，具有警告意味，但是无关紧要"
    btn_danger = "危险按钮，红色带有冲击性的颜色, 表示动作很危险， 具有强烈警告"
    btn_info = "禁用按钮，通常用于表示，当前动作不可用"
    btn_success = "成功按钮，通常用于表示，正确、可用"

    # 工具按钮
    tool_btn_primary = "默认的tool button"

    # 复选框
    checkbox_normal = "常用的复选框"
    checkbox_primary = "原生的复选框"

    # 日历
    calendar_primary = "默认日期选择"

    # 输入框
    line_edit_primary = "默认输入框"
    line_edit_error = "输入错误显示红色边框"
    text_edit_primary = "默认的文本输入框"
    plain_edit_primary = "默认的文本输入框"

    # 单选框
    radio_btn_primary = "原生的单选框"
    radio_btn_normal = "常用的单选框，开关切换样式"

    # tab 选项卡
    tab_widget_primary = "原生的选项卡"

    # 字体下拉框
    font_box_primary = "原生的字体选择框"

    # 下拉框
    combo_box_primary = "原生的下拉选择框"

    # 可变选择框
    spin_box_primary = "原生的啥啥框，就是右边有两个按钮可以改变数字的"
    time_edit_primary = "原生的时间选择框"
    date_edit_primary = "原生的日期选择框"

    # 进度条
    progress_bar_primary = "原生进度条"
    # 滑动块
    slider_primary = "原生滑动块"

    # 滚动条
    scroll_bar_primary = "原生滚动条"

    # tips
    tool_tip_primary = "默认的提示框"

    # 其他
    border_red = "红色边框一般用于警示，输入错误"
