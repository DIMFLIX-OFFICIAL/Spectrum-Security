import time

from PySide2.QtCore    import *
from PySide2.QtWidgets import *
from PySide2.QtGui     import *




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
            if self._tickfunc:
                self._tickfunc()

    def current(self):
        if self.reverse:
            return self.endv - (self.value * (self.endv-self.startv))
        else:
            return self.value * (self.endv-self.startv)





class ToggleSwitch(QWidget):

    toggled = Signal()

    def __init__(self, text="", onColor=QColor(189, 147, 249), offColor=QColor(136, 136, 136), handleColor=QColor(255, 255, 255),on=False, width=25, radius=23):
        super().__init__()

        self.text = text

        self.on = on

        self.opacity = QGraphicsOpacityEffect(self)
        self.opacity.setOpacity(1)
        self.setGraphicsEffect(self.opacity)

        self.onColor  = onColor
        self.offColor = offColor
        self.handleAlpha = False
        self.handleColor = handleColor
        self.width = width
        self.radius = radius


        self.setMinimumSize(self.width + (self.radius*2) + (len(self.text)*10), self.radius+2)

        self.anim = AnimationHandler(self, 0, self.width, lambda x: 1 - ((1 - x)**3))
        if self.on: self.anim.value = 1

    def isToggled(self):
        return not self.on

    def desaturate(self, color):
        cc = getattr(self, color)
        h = cc.hue()
        if h < 0: h = 0
        s = cc.saturation()//4
        if s > 255: s = 255
        c = QColor.fromHsv(h, s, cc.value())
        setattr(self, color, c)

    def saturate(self, color):
        cc = getattr(self, color)
        h = cc.hue()
        if h < 0: h = 0
        s = cc.saturation()*4
        if s > 255: s = 255
        c = QColor.fromHsv(h, s, cc.value())
        setattr(self, color, c)

    def update(self, *args, **kwargs):
        self.anim.update()
        super().update(*args, **kwargs)

    def mousePressEvent(self, event):
        if self.isEnabled():
            if self.on:
                self.on = False
                self.anim.start(reverse=True)
            else:
                self.on = True
                self.anim.start()
            self.update()

            self.toggled.emit()

    def changeEvent(self, event):
        if event.type() == QEvent.EnabledChange:
            if self.isEnabled():
                self.saturate("onColor")
                self.saturate("offColor")
                self.saturate("handleColor")
                self.opacity.setOpacity(1.00)
            else:
                self.desaturate("onColor")
                self.desaturate("offColor")
                self.desaturate("handleColor")
                self.opacity.setOpacity(0.4)

            self.update()

        else:
            super().changeEvent(event)

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

        if self.on:
            pen = QPen(self.onColor, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            pt.setPen(pen)
            brush = QBrush(self.onColor)
            pt.setBrush(brush)

            r = self.radius
            w = self.width

            pt.drawChord(r, 1, r, r, 90*16, 180*16)
            pt.drawChord(r+w, 1, r, r, -90*16, 180*16)
            pt.drawRect(r+r//2, 1, w, r)

            if self.handleAlpha: pt.setBrush(pt.background())
            else: pt.setBrush(QBrush(self.handleColor))
            offset = r*0.025
            pt.drawEllipse(r+offset/2+self.anim.current() , 1+offset/2 , r-offset , r-offset)

        else:
            pen = QPen(self.offColor.darker(135), 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            pt.setPen(pen)
            brush = QBrush(self.offColor)
            pt.setBrush(brush)

            r = self.radius
            w = self.width

            pt.drawChord(r, 1, r, r, 90*16, 180*16)
            pt.drawChord(r+w, 1, r, r, -90*16, 180*16)
            pt.drawRect(r+r//2, 1, w, r)
            pt.setPen(QPen(self.offColor))
            pt.drawRect(r+r//2-2, 2, w+4, r-2)

            if self.handleAlpha: pt.setBrush(pt.background())
            else: pt.setBrush(QBrush(self.handleColor))
            pt.setPen(QPen(self.handleColor.darker(160)))
            offset = r*0.025
            pt.drawEllipse(r+offset/2+self.anim.current() , 1+offset/2 , r-offset , r-offset)


        font = pt.font()
        pt.setFont(font)
        pt.setPen(QPen(Qt.black))

        pt.drawText(w+r*2+10, r//2+r//4, self.text)

        pt.end()

        if not self.anim.done(): self.update()
