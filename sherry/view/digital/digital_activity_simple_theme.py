# coding=utf-8
"""
    create by pymu
    on 2021/8/12
    at 20:37
"""
from qtpy.QtWidgets import QTreeWidgetItem

from sherry.view.activity.activity_simple_theme import SimpleThemeActivity


class SimpleThemeDigital(SimpleThemeActivity):

    def procedure(self):
        super(SimpleThemeDigital, self).procedure()
        self.add_menu(self.treeWidget, self.get_menu_data())
        # 默认选择第一项
        self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0))

    def get_menu_data(self):
        """返回一个关于左侧菜单栏的数据块"""
        return {
            "首页": {
                "icon": self.resource.font_icon('fa.home', color='#333'),
                "disabled": False,
            },
            "UI元素": {
                "icon": self.resource.font_icon('fa.tachometer', color='#333',
                                                # color_active='orange',
                                                # options=[{'active': 'fa5s.balance-scale'}]
                                                ),
                "children": {
                    "按钮": {},
                    "表格": {},
                    "弹窗": {},
                    "标签": {},
                    "日历": {},
                    "配色": {},
                    "图标": {},
                    "多媒体": {},
                    "通知消息": {},
                    "流式布局": {},
                }
            },
            "主题": {
                "icon": self.resource.font_icon('fa.themeisle', color='#333'),
            },
            "文件浏览器": {
                "icon": self.resource.font_icon('fa.chrome', color='#333'),
            },
            "多媒体": {"indentation": 9},
            "图表": {"indentation": 9},
            "聊天窗口": {"indentation": 9},
        }

    def add_menu(self, root, data, indentation=4):
        """这种一般是自己写一个遍历添加数据"""
        for k, v in data.items():
            item = QTreeWidgetItem(root)
            # 添加空格是为了与图标在导航栏收缩的时候不被看到
            if "indentation" in v:
                indentation = v.get('indentation')
            item.setText(0, ' ' * indentation + k.strip())
            item.setDisabled(v.get('disabled', False))
            if 'icon' in v:
                item.setIcon(0, v.get('icon'))
            self.add_menu(item, v.get('children', {}), 10)
