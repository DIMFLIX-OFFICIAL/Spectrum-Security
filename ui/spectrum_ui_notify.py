# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrum_ui_notify.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 101)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"")
        self.BackGround = QWidget(MainWindow)
        self.BackGround.setObjectName(u"BackGround")
        self.BackGround.setStyleSheet(u"")
        self.white_background = QFrame(self.BackGround)
        self.white_background.setObjectName(u"white_background")
        self.white_background.setGeometry(QRect(0, 0, 400, 100))
        self.white_background.setMinimumSize(QSize(400, 100))
        self.white_background.setMaximumSize(QSize(16777215, 16777215))
        self.white_background.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.white_background.setFrameShape(QFrame.StyledPanel)
        self.white_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.white_background)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 0, 0)
        self.grey_background = QFrame(self.white_background)
        self.grey_background.setObjectName(u"grey_background")
        self.grey_background.setMinimumSize(QSize(0, 0))
        self.grey_background.setStyleSheet(u"background-color: #1F1F1F;\n"
"border-radius: 10px;")
        self.grey_background.setFrameShape(QFrame.StyledPanel)
        self.grey_background.setFrameShadow(QFrame.Raised)
        self.window_title = QLabel(self.grey_background)
        self.window_title.setObjectName(u"window_title")
        self.window_title.setGeometry(QRect(10, 0, 201, 35))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.window_title.setFont(font)
        self.window_title.setStyleSheet(u"color: #FFF;")
        self.close_btn = QPushButton(self.grey_background)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(359, 0, 35, 35))
        self.close_btn.setMinimumSize(QSize(0, 0))
        self.close_btn.setMaximumSize(QSize(35, 35))
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: none;\n"
" 	border-radius: 0px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/general/imgs/general/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(18, 18))
        self.notify_text = QLabel(self.grey_background)
        self.notify_text.setObjectName(u"notify_text")
        self.notify_text.setGeometry(QRect(10, 36, 371, 51))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.notify_text.setFont(font1)
        self.notify_text.setStyleSheet(u"color: #FFF;")
        self.notify_text.setScaledContents(True)
        self.notify_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.notify_text.setWordWrap(True)

        self.verticalLayout.addWidget(self.grey_background)

        MainWindow.setCentralWidget(self.BackGround)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_title.setText(QCoreApplication.translate("MainWindow", u"SPECTRUM SECURITY", None))
        self.close_btn.setText("")
        self.notify_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>I Love your computer and the data stored on it :3</p></body></html>", None))
    # retranslateUi

