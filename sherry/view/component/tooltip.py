# encoding=utf-8
"""
    create by pymu
    on 2021/6/7
    at 10:50
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QLabel, QDialog


class Tooltip(QDialog):
    BORDER_RADIUS = 15

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place()
        self.configure()

    def configure(self):
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModal)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def place(self):
        m_ImgLabel = QLabel(self)
        m_TextLabel = QLabel(self)

        m_ImgLabel.setGeometry(5, 8, 32, 32)
        pixmap = QPixmap("warning_128px.ico")
        pixmap.scaled(m_ImgLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        m_ImgLabel.setScaledContents(True)
        m_ImgLabel.setPixmap(pixmap)
        m_ImgLabel.setAlignment(Qt.AlignCenter)

        lbl_font = QFont()
        lbl_font.setPixelSize(20)
        m_TextLabel.setFont(lbl_font)
        m_TextLabel.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        m_TextLabel.setGeometry(40, 14, 100, 20)
        m_TextLabel.setMinimumHeight(20)
        m_TextLabel.setText('测试')

    def paintEvent(self, event):
        Painter = QPainter(self)
        Painter.setRenderHint(QPainter.Antialiasing, True)
        Painter.setPen(Qt.SolidLine)
        Painter.setBrush(QColor(218, 250, 250, 255))

        PainterPath = QPainterPath()
        PainterPath.moveTo(10, 65)
        PainterPath.lineTo(25, 48)
        PainterPath.lineTo(self.width() - self.BORDER_RADIUS, 48)
        PainterPath.arcTo(self.width() - self.BORDER_RADIUS, 48 - self.BORDER_RADIUS, self.BORDER_RADIUS,
                          self.BORDER_RADIUS, 270, 90)
        PainterPath.lineTo(self.width(), self.BORDER_RADIUS)
        PainterPath.arcTo(self.width() - self.BORDER_RADIUS, 0, self.BORDER_RADIUS, self.BORDER_RADIUS, 0, 90)
        PainterPath.lineTo(self.BORDER_RADIUS, 0)
        PainterPath.arcTo(0, 0, self.BORDER_RADIUS, self.BORDER_RADIUS, 90, 90)
        PainterPath.lineTo(0, 48 - self.BORDER_RADIUS)
        PainterPath.arcTo(0, 48 - self.BORDER_RADIUS, self.BORDER_RADIUS, self.BORDER_RADIUS, 180, 90)
        PainterPath.lineTo(10, 65)
        Painter.drawPath(PainterPath)
