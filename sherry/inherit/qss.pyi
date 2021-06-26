# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 20:03
"""
from typing import Tuple


class Qss:
    """"""

    # 容器类
    widget_primary: Tuple[str, str]
    frame_primary: Tuple[str, str]

    # 使用元组放置属性筛选描述
    btn_style_simplicity: Tuple[str, str]
    btn_primary: Tuple[str, str]
    btn_warning: Tuple[str, str]
    btn_danger: Tuple[str, str]
    btn_info: Tuple[str, str]
    btn_success: Tuple[str, str]

    # 工具按钮
    tool_btn_primary: Tuple[str, str]

    # 复选框
    checkbox_normal: Tuple[str, str]
    checkbox_primary: Tuple[str, str]

    # 日历
    calendar_primary: Tuple[str, str]

    # 输入框
    line_edit_primary: Tuple[str, str]
    line_edit_error: Tuple[str, str]
    text_edit_primary: Tuple[str, str]
    plain_edit_primary: Tuple[str, str]

    # 单选框
    radio_btn_primary: Tuple[str, str]
    radio_btn_normal: Tuple[str, str]

    # tab 选项卡
    tab_widget_primary: Tuple[str, str]

    # 字体下拉框
    font_box_primary: Tuple[str, str]

    # 下拉框
    combo_box_primary: Tuple[str, str]

    # 可变选择框
    spin_box_primary: Tuple[str, str]
    time_edit_primary: Tuple[str, str]
    date_edit_primary: Tuple[str, str]

    # 进度条
    progress_bar_primary: Tuple[str, str]
    # 滑动块
    slider_primary: Tuple[str, str]

    # 滚动条
    scroll_bar_primary: Tuple[str, str]

    # tips
    tool_tip_primary: Tuple[str, str]

    # 其他
    border_red: Tuple[str, str]

    def __getattribute__(self, item): ...
