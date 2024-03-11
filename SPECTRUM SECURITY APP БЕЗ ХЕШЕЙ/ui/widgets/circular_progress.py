from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class CicularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.value = 0
        self.width = 180
        self.height = 180
        self.progress_width = 5
        self.progress_rounded_cap = True
        self.progress_color = "#FFF"
        self.max_value = 100
        self.suffix = "%"
        self.text_color = "#FFF"
        self.enable_shadow = True
        self.enable_text = True
        self.enable_bg = True
        self.bg_color = '#383838'

        self.resize(self.width, self.height)

    def set_value(self, value):
        if self.value != value:
            self.value = value
            self.update()

    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)

        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        paint.setFont(font)

        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        if self.progress_rounded_cap:
             pen.setCapStyle(Qt.RoundCap)

        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, 90*16, -value*16)


        if self.enable_text:
            pen.setColor(self.text_color)
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")


        paint.end()