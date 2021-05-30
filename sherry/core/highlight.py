# coding=utf-8
# 

"""
    create by pymu
    on 2020/6/26
    at 13:20

    编辑器高亮, 根据输入的关键字进行正则匹配高亮
"""
import json
import sys
from typing import List, Dict

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont, QCursor, QTextBlockFormat, QFontMetrics
from PyQt5.QtWidgets import QApplication, QTextEdit


class EditHighLighter(QSyntaxHighlighter):
    """
    qt 编辑器语法高亮 todo 可以从外部json 加载关键字
    """

    # 默认字体
    __font: str = "Consolas"
    # 默认字体大小
    __font_size: int = 14
    # 默认配色
    __color_config: Dict[str, QColor] = {
        "normal": QColor(Qt.gray),  # 一般字符
        "keyword": QColor(Qt.darkRed),  # 关键字
        "builtin": QColor("#8888c6"),  # 内嵌关键字
        "constant": QColor("#9876aa"),  # 特殊常量
        "decorator": QColor(Qt.darkBlue),  # 装饰器
        "comment": QColor(Qt.darkGreen),  # 文档
        "string": QColor(Qt.darkGreen),  # 字符串
        "number": QColor("#6879bb"),  # 数字
        "error": QColor(Qt.darkRed),  # 异常
    }

    # 一般关键字
    __key_word: List[str] = [
        "and", "as", "assert", "break", "class",
        "continue", "def", "del", "elif", "else", "except",
        "exec", "finally", "for", "from", "global", "if",
        "import", "in", "is", "lambda", "not", "or", "pass",
        "print", "raise", "return", "try", "while", "with",
        "yield"
    ]

    # 内嵌关键字
    __builtins: List[str] = [
        "abs", "all", "any", "basestring", "bool",
        "callable", "chr", "classmethod", "cmp", "compile",
        "complex", "delattr", "dict", "dir", "divmod",
        "enumerate", "eval", "execfile", "exit", "file",
        "filter", "float", "frozenset", "getattr", "globals",
        "hasattr", "hex", "id", "int", "isinstance",
        "issubclass", "iter", "len", "list", "locals", "map",
        "max", "min", "object", "oct", "open", "ord", "pow",
        "property", "range", "reduce", "repr", "reversed",
        "round", "set", "setattr", "slice", "sorted",
        "staticmethod", "str", "sum", "super", "tuple", "type",
        "vars", "zip", "in"
    ]

    # 特殊常量
    __constants: List[str] = ["False", "True", "None", "NotImplemented", "Ellipsis"]

    # 默认规则(基本不会发生改变)
    __default_rules: Dict[str, QRegExp] = {
        # 数值类型
        "number":
            QRegExp(
                r"\b[+-]?[0-9]+[lL]?\b|\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b|\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b"),
        # 装饰器类型
        "decorator": QRegExp(r"\b@\w+\b"),
        # 字符串类型
        "string": QRegExp(r"""(?:'[^']*'|"[^"]*")"""),
    }

    # 匹配规则
    Rules: Dict[str, QRegExp] = {}
    # 关于类型与渲染模板
    __formats: Dict[str, QTextCharFormat] = {}

    def __init__(self, parent: QTextEdit, block_format: QTextBlockFormat = None):
        """
        编辑器语法高亮， 如果需要设置行高，
        应该由block_format设置好再对高亮编辑器初始化(当前默认的行高是6)

        :param parent: 输入框
        :param block_format: 格式
        """
        self.init_block_format(parent, block_format)
        super().__init__(parent.document())
        self.master = parent
        self.init_editor()
        self.init_rule()

    def format_from_json(self, path: str, encoding='utf-8') -> None:
        """从外部的json解析关键字"""
        with open(path, encoding) as f:
            data = json.load(f) or {}
            self.builtins = data.get("builtins", [])
            self.constants = data.get("constants", [])
            self.key_word = data.get("key_word", [])

    @property
    def font(self) -> str:
        """编辑器字体"""
        return self.__font

    @font.setter
    def font(self, font: str):
        """设置编辑器字体"""
        self.__font = font
        self.init_editor()

    @property
    def font_size(self) -> int:
        """编辑器字体大小"""
        return self.__font_size

    @font_size.setter
    def font_size(self, size: int):
        """设置编辑器字体大小"""
        self.__font_size = size
        self.init_editor()

    @property
    def color_config(self) -> Dict[str, QColor]:
        """配色方案"""
        return self.__color_config

    @color_config.setter
    def color_config(self, config: Dict[str, QColor]):
        """设置配色"""
        self.__color_config.update(config)

    @property
    def key_word(self) -> List[str]:
        """高亮关键字"""
        return self.__key_word

    @key_word.setter
    def key_word(self, key_word: List[str]):
        """设置关键字"""
        self.__key_word = key_word
        self.init_rule()

    @property
    def builtins(self) -> List[str]:
        """内嵌关键字"""
        return self.__builtins

    @builtins.setter
    def builtins(self, builtins: List[str]):
        """设置内嵌关键字"""
        self.__builtins = builtins
        self.init_rule()

    @property
    def constants(self) -> List[str]:
        """返回常量关键字"""
        return self.__constants

    @constants.setter
    def constants(self, constants: List[str]):
        """设置常量关键字"""
        self.__constants = constants
        self.init_rule()

    @property
    def rules(self) -> Dict[str, QRegExp]:
        """规则列表"""
        return self.Rules

    @rules.setter
    def rules(self, rules: Dict[str, QRegExp]):
        """设置规则 (update)"""
        self.Rules.update(rules)

    @property
    def text_format(self) -> Dict[str, QTextCharFormat]:
        """类型渲染模板"""
        return self.__formats

    @text_format.setter
    def text_format(self, formats: Dict[str, QTextCharFormat]):
        """通过外部设定具体类型的渲染模板"""
        self.__formats.update(formats)

    def set_tab_size(self, length=4):
        """
        替换默认的tab

        :param length: 替换长度
        """
        self.master.setTabStopDistance(length * QFontMetrics(QFont(self.font, self.font_size)).width(" "))

    def init_editor(self):
        """初始化编辑器, 定义类型应该显示的模板块， 可以同外部的 text_format设定其中具体的类型模板"""
        base_formats = QTextCharFormat()
        base_formats.setFont(QFont(self.font, self.font_size))
        # 设置配色
        for name, color in self.color_config.items():
            block_format = QTextCharFormat(base_formats)
            block_format.setForeground(color)
            # 关键字跟装饰器类型，字体应该加粗
            if name in ("keyword", "decorator"):
                block_format.setFontWeight(QFont.Bold)
            # 如果是文档类型，字体应该是斜体
            if name == "comment":
                block_format.setFontItalic(True)
            self.text_format = {name: block_format}

    @staticmethod
    def init_block_format(parent: QTextEdit, block_format: QTextBlockFormat):
        """设置行间距，行高"""
        text_cursor = parent.textCursor()
        if not block_format:
            block_format = QTextBlockFormat()
            block_format.setLineHeight(6, QTextBlockFormat.LineDistanceHeight)
        text_cursor.setBlockFormat(block_format)

    def init_rule(self):
        """初始化默认的匹配规则， 在更新keyword、builtin、constant后也会调用, 只会更新匹配三种格式（关键字、内嵌关键字、特殊常量）"""
        if not self.Rules:
            self.Rules.update(self.__default_rules)
        self.Rules.update({
            "keyword": QRegExp("|".join([r"\b%s\b" % keyword for keyword in self.key_word])),
            "builtin": QRegExp("|".join([r"\b%s\b" % builtin for builtin in self.builtins])),
            "constant": QRegExp("|".join([r"\b%s\b" % constant for constant in self.constants])),
        })

    def highlightBlock(self, text: str) -> None:
        """渲染高亮代码块（这个是重点）"""
        base_formats = QTextCharFormat()
        base_formats.setFont(QFont(self.font, self.font_size))
        base_formats.setForeground(self.__color_config.get("normal"))
        NORMAL, TRIPLING, TRIPLED, ERROR = range(4)
        textLength = len(text)
        # 前块状态
        prevState = self.previousBlockState()

        # 设置默认的渲染块（从 0 到 textLength 长度 替换成 normal）
        self.setFormat(0, textLength, self.text_format.get("normal", base_formats))

        # 异常渲染(这里都是一些自定义的 比如异常栈 打印等)
        if text.startswith("Traceback") or text.startswith("Error: "):
            self.setCurrentBlockState(ERROR)
            base_formats.setForeground(self.__color_config.get("error"))
            self.setFormat(0, textLength, self.text_format.get("error", base_formats))
            return
        if prevState == ERROR and not (text.startswith(sys.ps1) or text.startswith("#")):
            self.setCurrentBlockState(ERROR)
            base_formats.setForeground(self.__color_config.get("error"))
            self.setFormat(0, textLength, self.text_format.get("error", base_formats))
            return

        # 匹配规则(此处才是对规则的匹配)
        base_formats.setForeground(self.__color_config.get("normal"))
        # 遍历所有的规则，查看是否存在对应类型需要高亮的代码块，如果存在则全部替换
        for format_name, regex in self.Rules.items():
            i = regex.indexIn(text)
            while i >= 0:
                length = regex.matchedLength()
                self.setFormat(i, length, self.text_format.get(format_name, base_formats))
                i = regex.indexIn(text, i + length)
        self.setCurrentBlockState(NORMAL)

    # noinspection SpellCheckingInspection
    def rehighlight(self) -> None:
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        QSyntaxHighlighter.rehighlight(self)
        QApplication.restoreOverrideCursor()
