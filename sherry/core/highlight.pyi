from typing import Dict, List, TypedDict

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QTextBlockFormat, QFont
from PyQt5.QtWidgets import QTextEdit


class Font(TypedDict):
    family: str
    size: int


class Scheme(TypedDict):
    name: str
    key: List[str]
    regex: List[str]
    color: str
    bold: bool  # Note: 粗体
    italic: bool  # Note: 斜体


class RulesScheme(TypedDict):
    font: Font
    scheme: List[Scheme]


class Prism(QSyntaxHighlighter):
    rules_scheme: RulesScheme
    __block_format: Dict[str, QTextCharFormat]
    __font: QFont
    __rules: Dict[str, List[QRegExp]]

    def __init__(self, master: QTextEdit, block_format: QTextBlockFormat = None):
        super().__init__(master)

    def set_block_format(self, block_format: QTextBlockFormat): ...

    @property
    def font(self) -> QFont: ...

    def set_tab_size(self, length: int = 4): ...

    def highlightBlock(self, text: str): ...
