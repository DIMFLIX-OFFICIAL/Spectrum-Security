import time
from math import pow

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *






class AnimationHandler:
    def __init__(self, widget, startv, endv, type):
        self.widget = widget
        self.type = type
        self.startv = startv
        self.endv = endv
        self.value = 0
        self.speed = 3.45
        self.sensitivity = 0.001
        self.reverse = False
        self.loop = False
        self.started = None
        self._tickfunc = None

    def tick(self, func):
        self._tickfunc = func
        return func

    def start(self, reverse=False, loop=False):
        self.reverse = reverse
        self.loop = loop
        self.started = True
        self.orgstart_time = time.time()
        self.value = 0
        self.widget.update()


    def done(self):
        return self.started is None

    def update(self):
        if not self.done():
            ep = time.time() - self.orgstart_time

            self.value = self.type(ep * self.speed)

            if self.reverse:
                if self.current() <= self.startv + self.sensitivity: self.started = None
            else:
                if self.current() >= self.endv - self.sensitivity: self.started = None

            if self.done():
                if self.loop:
                    self.start(reverse=not self.reverse, loop=True)
                return

            if self._tickfunc: self._tickfunc()

    def current(self):
        if self.reverse:
            return self.endv - (self.value * (self.endv-self.startv))
        else:
            return self.value * (self.endv-self.startv)







class Toast(QWidget):
    def __init__(self, parent, text=""):
        super().__init__(parent)

        self.setFixedHeight(45)

        w = self.width()
        h = self.height()
        ww = self.parent().width()
        hh = self.parent().height()
        self.setGeometry(ww/2-w/2, hh-h-5, w, h)


        self.styleDict = {
            "background-color" : (56, 56, 56, 200),
            "border-radius" : 16,
            "color" : (255, 255, 255),
        }


        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(15, 0, 7, 0)
        self.setLayout(self.layout)



        self.conwdt = QWidget()
        self.conlyt = QHBoxLayout()
        self.conlyt.setContentsMargins(0, 0, 0, 0)
        self.conwdt.setLayout(self.conlyt)
        self.layout.addWidget(self.conwdt, alignment=Qt.AlignLeft)

        self.close_btn = QPushButton()
        self.close_btn.setFixedSize(self.height()/1.6, self.height()/1.6)
        self.close_btn.setStyleSheet("""QPushButton {  
                background-image: url(imgs/close.png);
                background-position: center;
                background-repeat: no-repeat;
                border-radius: 14;
            }""")
        self.layout.addWidget(self.close_btn)
        self.close_btn.clicked.connect(self.fall)

        self.textLbl = QLabel(text)
        self.conlyt.addWidget(self.textLbl, alignment=Qt.AlignCenter)

        self.risen = False

        self.anim = AnimationHandler(self, 0, 1, lambda x: 1 - pow(1 - x, 4))
        self.anim.speed = 1.7







    def setStyleDict(self, styledict):
        for k in styledict:
            self.styleDict[k] = styledict[k]

    def rise(self, duration):
        if not self.risen: 

            self.duration = duration
            self.risen = True
            self.anim.start()
            self.show()
            self.raise_()
            self.update()

    def fall(self):
        if self.risen: 
            self.anim.start(reverse=True)
            self.risen = False
            self.update()

    def update(self):
        self.anim.update()
        super().update()

    def paintEvent(self, event):

        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing, on=True)

        plt = self.textLbl.palette()
        plt.setColor(self.textLbl.foregroundRole(), QColor(*self.styleDict["color"]))
        self.textLbl.setPalette(plt)

        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.textLbl.setFont(font1)

        pt.setPen(QPen(QColor(0, 0, 0, 0)))
        pt.setBrush(QBrush(QColor(*self.styleDict["background-color"])))
        r = self.styleDict["border-radius"]

        pt.drawRoundedRect(0, 0, self.width(), self.height(), r, r)

        pt.end()

        if not self.anim.done():
            w = self.width()
            h = self.height()
            ww = self.parent().width()
            hh = self.parent().height()

            self.setGeometry(ww/2-w/2, hh-(self.anim.current()*(h+5))-0.01, w, h)

        if not self.anim.done(): self.update()
        else:
            if self.isVisible() and not self.risen: self.hide()
