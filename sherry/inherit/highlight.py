# coding=utf-8
# 

"""
    create by pymu
    on 2020/6/26
    at 13:20

    编辑器高亮, 根据输入的关键字进行正则匹配高亮
"""
import json

from qtpy.QtCore import Qt, QRegExp
from qtpy.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont, QCursor, QTextBlockFormat, QFontMetrics
from qtpy.QtWidgets import QApplication


class Prism(QSyntaxHighlighter):
    """
    TODO 从文件中读取资产
    """
    rules_scheme = {}  # Note: 映射规则
    __block_format = {}
    __font = None
    __rules = {}

    def __init__(self, master, block_format=None):
        super().__init__(master.document())
        self.master = master
        # 设置行间距、行高
        # set line height
        if not block_format:
            block_format = QTextBlockFormat()
            block_format.setLineHeight(6, QTextBlockFormat.LineDistanceHeight)
        self.set_block_format(block_format)

    def set_block_format(self, block_format):
        """
        设置行间距，行高

        Set line spacing, line height.
        """
        text_cursor = self.master.textCursor()
        text_cursor.setBlockFormat(block_format)

    def set_tab_size(self, length=4):
        """
        设置tab占位长度

        Set tab length.
        """
        self.master.setTabStopDistance(length * QFontMetrics(self.font).width(" "))

    @property
    def font(self):
        return QFont(self.rules['font']['family'], self.rules['font']['size'])

    def init_scheme(self):
        """初始化字体方案, 定义类型应该显示的模板块， 可以同外部的 text_format设定其中具体的类型模板"""
        base_formats = QTextCharFormat()
        base_formats.setFont(self.font)
        # 设置一个默认的字块
        # set a default text block
        self.__block_format.update({'normal': base_formats})
        # 设置配色
        # set block scheme
        for scheme in self.rules_scheme['scheme']:
            block_scheme = QTextCharFormat(base_formats)
            block_scheme.setForeground(QColor(scheme.get('color', '#000000')))
            if scheme['bold']:
                block_scheme.setFontWeight(QFont.Bold)
            if scheme['italic']:
                block_scheme.setFontItalic(True)
            self.__block_format.update({scheme['name']: block_scheme})

    def init_regex(self):
        self.__rules.update({
            scheme['name']: [QRegExp(i) for i in scheme['regex']] + [
                QRegExp("|".join([r"\b%s\b" % keyword for keyword in scheme['key']]))]
            for scheme in self.rules_scheme['scheme']
        })

    def highlightBlock(self, text):
        text_len = len(text)
        default_scheme = self.__scheme_template.get('normal')
        self.setFormat(0, text_len, default_scheme)
        for name, scheme in self.__rules.items():
            for regex in scheme:
                i = regex.indexIn(text)
                while i >= 0:
                    length = regex.matchedLength()
                    self.setFormat(i, length, self.__scheme_template.get(name, default_scheme))
                    i = regex.indexIn(text, i + length)
        self.setCurrentBlockState(0)

    # noinspection SpellCheckingInspection
    def rehighlight(self):
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        QSyntaxHighlighter.rehighlight(self)
        QApplication.restoreOverrideCursor()

    def format_from_json(self, path, encoding='utf-8'):
        """从外部的json解析关键字"""
        with open(path, encoding) as f:
            data = json.load(f) or {}
            print(data)
            print(self.__rules)
