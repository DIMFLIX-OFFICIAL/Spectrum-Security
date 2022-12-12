# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrum_ui.ui'
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
        MainWindow.resize(900, 555)
        MainWindow.setMinimumSize(QSize(900, 555))
        MainWindow.setMaximumSize(QSize(900, 555))
        MainWindow.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 5px;\n"
"    margin: 0px 80px 0px 80px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:  rgb(255, 255, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 2px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 1px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 1px;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 6px;\n"
"    margin: 10px 0 10px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(255, 255,"
                        " 255);\n"
"    min-height: 25px;\n"
"	border-radius: 3px\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: none;\n"
"     height: 1px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: none;\n"
"     height: 1px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.BackGround = QWidget(MainWindow)
        self.BackGround.setObjectName(u"BackGround")
        self.BackGround.setStyleSheet(u"background-color: #1F1F1F;\n"
"border-radius: 15px;\n"
"")
        self.top_menu = QFrame(self.BackGround)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setGeometry(QRect(0, 0, 900, 50))
        self.top_menu.setMinimumSize(QSize(900, 50))
        self.top_menu.setMaximumSize(QSize(16777215, 50))
        self.top_menu.setStyleSheet(u"background-color: #2C2C2C;\n"
"border-radius: 0px;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;")
        self.top_menu.setFrameShape(QFrame.StyledPanel)
        self.top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_menu_header = QFrame(self.top_menu)
        self.top_menu_header.setObjectName(u"top_menu_header")
        self.top_menu_header.setFrameShape(QFrame.StyledPanel)
        self.top_menu_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.top_menu_header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.top_menu_icon = QLabel(self.top_menu_header)
        self.top_menu_icon.setObjectName(u"top_menu_icon")
        self.top_menu_icon.setMinimumSize(QSize(30, 30))
        self.top_menu_icon.setMaximumSize(QSize(30, 30))
        self.top_menu_icon.setPixmap(QPixmap(u":/general/imgs/general/icon.png"))

        self.horizontalLayout_4.addWidget(self.top_menu_icon)

        self.top_menu_title = QLabel(self.top_menu_header)
        self.top_menu_title.setObjectName(u"top_menu_title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.top_menu_title.setFont(font)
        self.top_menu_title.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_4.addWidget(self.top_menu_title)


        self.horizontalLayout_2.addWidget(self.top_menu_header)

        self.top_menu_btns = QFrame(self.top_menu)
        self.top_menu_btns.setObjectName(u"top_menu_btns")
        self.top_menu_btns.setMinimumSize(QSize(100, 50))
        self.top_menu_btns.setMaximumSize(QSize(100, 50))
        self.top_menu_btns.setFrameShape(QFrame.StyledPanel)
        self.top_menu_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_menu_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_menu_minimize_btn = QPushButton(self.top_menu_btns)
        self.top_menu_minimize_btn.setObjectName(u"top_menu_minimize_btn")
        self.top_menu_minimize_btn.setMinimumSize(QSize(50, 50))
        self.top_menu_minimize_btn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #3C3C3C;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #3C3C3C;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/general/imgs/general/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.top_menu_minimize_btn.setIcon(icon)
        self.top_menu_minimize_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.top_menu_minimize_btn)

        self.top_menu_close_btn = QPushButton(self.top_menu_btns)
        self.top_menu_close_btn.setObjectName(u"top_menu_close_btn")
        self.top_menu_close_btn.setMinimumSize(QSize(50, 50))
        self.top_menu_close_btn.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: none;\n"
"	border-radius: 0px;\n"
"	border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #3C3C3C;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #3C3C3C;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/general/imgs/general/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.top_menu_close_btn.setIcon(icon1)
        self.top_menu_close_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.top_menu_close_btn)


        self.horizontalLayout_2.addWidget(self.top_menu_btns)

        self.Pages = QStackedWidget(self.BackGround)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setGeometry(QRect(12, 62, 876, 364))
        self.Pages.setMinimumSize(QSize(876, 364))
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.verticalLayout = QVBoxLayout(self.HomePage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_main_menu = QFrame(self.HomePage)
        self.home_main_menu.setObjectName(u"home_main_menu")
        self.home_main_menu.setStyleSheet(u"background-color: #2C2C2C;\n"
"border-radius: 15px;")
        self.home_main_menu.setFrameShape(QFrame.StyledPanel)
        self.home_main_menu.setFrameShadow(QFrame.Raised)
        self.home_white_left_line = QFrame(self.home_main_menu)
        self.home_white_left_line.setObjectName(u"home_white_left_line")
        self.home_white_left_line.setGeometry(QRect(10, 12, 6, 340))
        self.home_white_left_line.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 3px;")
        self.home_white_left_line.setFrameShape(QFrame.StyledPanel)
        self.home_white_left_line.setFrameShadow(QFrame.Raised)
        self.RAM_background_white = QFrame(self.home_main_menu)
        self.RAM_background_white.setObjectName(u"RAM_background_white")
        self.RAM_background_white.setGeometry(QRect(30, 140, 470, 81))
        self.RAM_background_white.setMinimumSize(QSize(470, 34))
        self.RAM_background_white.setMaximumSize(QSize(470, 16777215))
        self.RAM_background_white.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.RAM_background_white.setFrameShape(QFrame.StyledPanel)
        self.RAM_background_white.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.RAM_background_white)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(6, 0, 0, 0)
        self.RAM_background_grey = QFrame(self.RAM_background_white)
        self.RAM_background_grey.setObjectName(u"RAM_background_grey")
        self.RAM_background_grey.setMinimumSize(QSize(465, 35))
        self.RAM_background_grey.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.RAM_background_grey.setFrameShape(QFrame.StyledPanel)
        self.RAM_background_grey.setFrameShadow(QFrame.Raised)
        self.RAM_progress = QLabel(self.RAM_background_grey)
        self.RAM_progress.setObjectName(u"RAM_progress")
        self.RAM_progress.setGeometry(QRect(10, 0, 120, 35))
        self.RAM_progress.setFont(font)
        self.RAM_progress.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.RAM_total_info = QLabel(self.RAM_background_grey)
        self.RAM_total_info.setObjectName(u"RAM_total_info")
        self.RAM_total_info.setGeometry(QRect(10, 35, 441, 16))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.RAM_total_info.setFont(font1)
        self.RAM_total_info.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.RAM_used_info = QLabel(self.RAM_background_grey)
        self.RAM_used_info.setObjectName(u"RAM_used_info")
        self.RAM_used_info.setGeometry(QRect(10, 55, 441, 16))
        self.RAM_used_info.setFont(font1)
        self.RAM_used_info.setStyleSheet(u"color: #FFF;\n"
"background: none;")

        self.verticalLayout_20.addWidget(self.RAM_background_grey)

        self.CPU_background_white = QFrame(self.home_main_menu)
        self.CPU_background_white.setObjectName(u"CPU_background_white")
        self.CPU_background_white.setGeometry(QRect(30, 20, 470, 101))
        self.CPU_background_white.setMinimumSize(QSize(470, 34))
        self.CPU_background_white.setMaximumSize(QSize(470, 16777215))
        self.CPU_background_white.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.CPU_background_white.setFrameShape(QFrame.StyledPanel)
        self.CPU_background_white.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.CPU_background_white)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(6, 0, 0, 0)
        self.CPU_background_grey = QFrame(self.CPU_background_white)
        self.CPU_background_grey.setObjectName(u"CPU_background_grey")
        self.CPU_background_grey.setMinimumSize(QSize(465, 35))
        self.CPU_background_grey.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.CPU_background_grey.setFrameShape(QFrame.StyledPanel)
        self.CPU_background_grey.setFrameShadow(QFrame.Raised)
        self.CPU_progress = QLabel(self.CPU_background_grey)
        self.CPU_progress.setObjectName(u"CPU_progress")
        self.CPU_progress.setGeometry(QRect(10, 0, 112, 35))
        self.CPU_progress.setFont(font)
        self.CPU_progress.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.CPU_info = QLabel(self.CPU_background_grey)
        self.CPU_info.setObjectName(u"CPU_info")
        self.CPU_info.setGeometry(QRect(10, 35, 441, 16))
        self.CPU_info.setFont(font1)
        self.CPU_info.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.Physical_cores_info = QLabel(self.CPU_background_grey)
        self.Physical_cores_info.setObjectName(u"Physical_cores_info")
        self.Physical_cores_info.setGeometry(QRect(10, 55, 441, 21))
        self.Physical_cores_info.setFont(font1)
        self.Physical_cores_info.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.Frequency_info = QLabel(self.CPU_background_grey)
        self.Frequency_info.setObjectName(u"Frequency_info")
        self.Frequency_info.setGeometry(QRect(10, 75, 441, 21))
        self.Frequency_info.setFont(font1)
        self.Frequency_info.setStyleSheet(u"color: #FFF;\n"
"background: none;")

        self.verticalLayout_19.addWidget(self.CPU_background_grey)

        self.GPU_background_white = QFrame(self.home_main_menu)
        self.GPU_background_white.setObjectName(u"GPU_background_white")
        self.GPU_background_white.setGeometry(QRect(30, 240, 470, 101))
        self.GPU_background_white.setMinimumSize(QSize(470, 34))
        self.GPU_background_white.setMaximumSize(QSize(470, 16777215))
        self.GPU_background_white.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.GPU_background_white.setFrameShape(QFrame.StyledPanel)
        self.GPU_background_white.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.GPU_background_white)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(6, 0, 0, 0)
        self.GPU_background_grey = QFrame(self.GPU_background_white)
        self.GPU_background_grey.setObjectName(u"GPU_background_grey")
        self.GPU_background_grey.setMinimumSize(QSize(465, 35))
        self.GPU_background_grey.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}\n"
"")
        self.GPU_background_grey.setFrameShape(QFrame.StyledPanel)
        self.GPU_background_grey.setFrameShadow(QFrame.Raised)
        self.GPU_progress = QLabel(self.GPU_background_grey)
        self.GPU_progress.setObjectName(u"GPU_progress")
        self.GPU_progress.setGeometry(QRect(10, 0, 114, 35))
        self.GPU_progress.setFont(font)
        self.GPU_progress.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.GPU_model_info = QLabel(self.GPU_background_grey)
        self.GPU_model_info.setObjectName(u"GPU_model_info")
        self.GPU_model_info.setGeometry(QRect(10, 35, 441, 16))
        self.GPU_model_info.setFont(font1)
        self.GPU_model_info.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.GPU_vram_total_info = QLabel(self.GPU_background_grey)
        self.GPU_vram_total_info.setObjectName(u"GPU_vram_total_info")
        self.GPU_vram_total_info.setGeometry(QRect(10, 55, 441, 16))
        self.GPU_vram_total_info.setFont(font1)
        self.GPU_vram_total_info.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.GPU_vram_used_info = QLabel(self.GPU_background_grey)
        self.GPU_vram_used_info.setObjectName(u"GPU_vram_used_info")
        self.GPU_vram_used_info.setGeometry(QRect(10, 75, 441, 16))
        self.GPU_vram_used_info.setFont(font1)
        self.GPU_vram_used_info.setStyleSheet(u"color: #FFF;\n"
"background: none;")

        self.verticalLayout_21.addWidget(self.GPU_background_grey)

        self.home_logo = QLabel(self.home_main_menu)
        self.home_logo.setObjectName(u"home_logo")
        self.home_logo.setGeometry(QRect(510, 0, 361, 361))
        self.home_logo.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.home_logo.setPixmap(QPixmap(u":/general/imgs/general/SpectrumLogo.png"))
        self.home_secret_way = QFrame(self.home_main_menu)
        self.home_secret_way.setObjectName(u"home_secret_way")
        self.home_secret_way.setGeometry(QRect(760, 47, 53, 47))
        self.home_secret_way.setStyleSheet(u"background: none;")
        self.home_secret_way.setFrameShape(QFrame.StyledPanel)
        self.home_secret_way.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.home_main_menu)

        self.Pages.addWidget(self.HomePage)
        self.ScanningPage = QWidget()
        self.ScanningPage.setObjectName(u"ScanningPage")
        self.verticalLayout_2 = QVBoxLayout(self.ScanningPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scanning_main_menu = QFrame(self.ScanningPage)
        self.scanning_main_menu.setObjectName(u"scanning_main_menu")
        self.scanning_main_menu.setStyleSheet(u"background-color: #2C2C2C;\n"
"border-radius: 15px;")
        self.scanning_main_menu.setFrameShape(QFrame.StyledPanel)
        self.scanning_main_menu.setFrameShadow(QFrame.Raised)
        self.scanning_white_left_line = QFrame(self.scanning_main_menu)
        self.scanning_white_left_line.setObjectName(u"scanning_white_left_line")
        self.scanning_white_left_line.setGeometry(QRect(10, 12, 6, 340))
        self.scanning_white_left_line.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 3px;")
        self.scanning_white_left_line.setFrameShape(QFrame.StyledPanel)
        self.scanning_white_left_line.setFrameShadow(QFrame.Raised)
        self.scanning_top_menu = QFrame(self.scanning_main_menu)
        self.scanning_top_menu.setObjectName(u"scanning_top_menu")
        self.scanning_top_menu.setGeometry(QRect(60, 20, 395, 51))
        self.scanning_top_menu.setFrameShape(QFrame.StyledPanel)
        self.scanning_top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.scanning_top_menu)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scanning_choose_btn_full = QRadioButton(self.scanning_top_menu)
        self.scanning_choose_btn_full.setObjectName(u"scanning_choose_btn_full")
        self.scanning_choose_btn_full.setMinimumSize(QSize(131, 40))
        self.scanning_choose_btn_full.setMaximumSize(QSize(131, 40))
        self.scanning_choose_btn_full.setFont(font)
        self.scanning_choose_btn_full.setStyleSheet(u"QRadioButton {	\n"
"	background-color: #383838;\n"
"	border-radius: 0px;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	border: 1px solid #FFF;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"	background-color: #3C3C3C;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	width: 35px;\n"
"	height: 1px;\n"
"	background-color: #383838;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	border: 1px solid #BD93F9;	\n"
"	color: #BD93F9;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.scanning_choose_btn_full)

        self.scanning_choose_btn_folder = QRadioButton(self.scanning_top_menu)
        self.scanning_choose_btn_folder.setObjectName(u"scanning_choose_btn_folder")
        self.scanning_choose_btn_folder.setMinimumSize(QSize(131, 40))
        self.scanning_choose_btn_folder.setMaximumSize(QSize(131, 40))
        self.scanning_choose_btn_folder.setFont(font)
        self.scanning_choose_btn_folder.setStyleSheet(u"QRadioButton {	\n"
"	background-color: #383838;\n"
"	border-radius: 0px;\n"
"	border: 1px solid #FFF;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"	background-color: #3C3C3C;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	width: 22px;\n"
"	height: 1px;\n"
"	background-color: #383838;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	border: 1px solid #BD93F9;	\n"
"	color: #BD93F9;\n"
"}")

        self.horizontalLayout_19.addWidget(self.scanning_choose_btn_folder)

        self.scanning_choose_btn_file = QRadioButton(self.scanning_top_menu)
        self.scanning_choose_btn_file.setObjectName(u"scanning_choose_btn_file")
        self.scanning_choose_btn_file.setMinimumSize(QSize(131, 40))
        self.scanning_choose_btn_file.setMaximumSize(QSize(131, 40))
        self.scanning_choose_btn_file.setFont(font)
        self.scanning_choose_btn_file.setStyleSheet(u"QRadioButton {	\n"
"	background-color: #383838;\n"
"	border-radius: 0px;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 1px solid #FFF;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"	background-color: #3C3C3C;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	width: 37px;\n"
"	height: 1px;\n"
"	background-color: #383838;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	border: 1px solid #BD93F9;	\n"
"	color: #BD93F9;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.scanning_choose_btn_file)

        self.layoutWidget = QWidget(self.scanning_main_menu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 90, 181, 181))
        self.scanning_progress_bar_widget = QVBoxLayout(self.layoutWidget)
        self.scanning_progress_bar_widget.setSpacing(0)
        self.scanning_progress_bar_widget.setObjectName(u"scanning_progress_bar_widget")
        self.scanning_progress_bar_widget.setContentsMargins(0, 0, 0, 0)
        self.scanning_start_btn = QPushButton(self.scanning_main_menu)
        self.scanning_start_btn.setObjectName(u"scanning_start_btn")
        self.scanning_start_btn.setGeometry(QRect(161, 290, 193, 40))
        self.scanning_start_btn.setMinimumSize(QSize(193, 40))
        self.scanning_start_btn.setMaximumSize(QSize(193, 40))
        self.scanning_start_btn.setFont(font)
        self.scanning_start_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #3C3C3C;\n"
"}\n"
"")
        self.scanning_logo = QLabel(self.scanning_main_menu)
        self.scanning_logo.setObjectName(u"scanning_logo")
        self.scanning_logo.setGeometry(QRect(510, 0, 341, 361))
        self.scanning_logo.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.scanning_logo.setPixmap(QPixmap(u":/general/imgs/general/SpectrumLogo.png"))
        self.scanning_secret_way = QFrame(self.scanning_main_menu)
        self.scanning_secret_way.setObjectName(u"scanning_secret_way")
        self.scanning_secret_way.setGeometry(QRect(760, 47, 53, 47))
        self.scanning_secret_way.setStyleSheet(u"background: none;")
        self.scanning_secret_way.setFrameShape(QFrame.StyledPanel)
        self.scanning_secret_way.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.scanning_main_menu)

        self.Pages.addWidget(self.ScanningPage)
        self.FaqPage = QWidget()
        self.FaqPage.setObjectName(u"FaqPage")
        self.verticalLayout_3 = QVBoxLayout(self.FaqPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.faq_main_menu = QFrame(self.FaqPage)
        self.faq_main_menu.setObjectName(u"faq_main_menu")
        self.faq_main_menu.setStyleSheet(u"background-color: #2C2C2C;\n"
"border-radius: 15px;")
        self.faq_main_menu.setFrameShape(QFrame.StyledPanel)
        self.faq_main_menu.setFrameShadow(QFrame.Raised)
        self.faq_scroll_area = QScrollArea(self.faq_main_menu)
        self.faq_scroll_area.setObjectName(u"faq_scroll_area")
        self.faq_scroll_area.setGeometry(QRect(10, 12, 491, 340))
        self.faq_scroll_area.setLayoutDirection(Qt.RightToLeft)
        self.faq_scroll_area.setStyleSheet(u"margin: 0px;")
        self.faq_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.faq_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.faq_scroll_area.setWidgetResizable(True)
        self.faq_scroll_area.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_scroll_area_widget = QWidget()
        self.faq_scroll_area_widget.setObjectName(u"faq_scroll_area_widget")
        self.faq_scroll_area_widget.setGeometry(QRect(0, 0, 485, 340))
        self.verticalLayout_5 = QVBoxLayout(self.faq_scroll_area_widget)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.faq_scroll_area_frame = QFrame(self.faq_scroll_area_widget)
        self.faq_scroll_area_frame.setObjectName(u"faq_scroll_area_frame")
        self.faq_scroll_area_frame.setFrameShape(QFrame.StyledPanel)
        self.faq_scroll_area_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.faq_scroll_area_frame)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.faq_small_description_white_background = QFrame(self.faq_scroll_area_frame)
        self.faq_small_description_white_background.setObjectName(u"faq_small_description_white_background")
        self.faq_small_description_white_background.setMinimumSize(QSize(470, 34))
        self.faq_small_description_white_background.setMaximumSize(QSize(470, 34))
        self.faq_small_description_white_background.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.faq_small_description_white_background.setFrameShape(QFrame.StyledPanel)
        self.faq_small_description_white_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.faq_small_description_white_background)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(6, 0, 0, 0)
        self.faq_small_description_grey_background = QFrame(self.faq_small_description_white_background)
        self.faq_small_description_grey_background.setObjectName(u"faq_small_description_grey_background")
        self.faq_small_description_grey_background.setMinimumSize(QSize(465, 35))
        self.faq_small_description_grey_background.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.faq_small_description_grey_background.setFrameShape(QFrame.StyledPanel)
        self.faq_small_description_grey_background.setFrameShadow(QFrame.Raised)
        self.faq_small_description_title = QLabel(self.faq_small_description_grey_background)
        self.faq_small_description_title.setObjectName(u"faq_small_description_title")
        self.faq_small_description_title.setGeometry(QRect(10, 0, 401, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.faq_small_description_title.setFont(font2)
        self.faq_small_description_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_small_description_btn = QPushButton(self.faq_small_description_grey_background)
        self.faq_small_description_btn.setObjectName(u"faq_small_description_btn")
        self.faq_small_description_btn.setGeometry(QRect(410, 0, 55, 31))
        self.faq_small_description_btn.setMinimumSize(QSize(55, 31))
        self.faq_small_description_btn.setMaximumSize(QSize(55, 31))
        self.faq_small_description_btn.setStyleSheet(u"background: none;")
        icon2 = QIcon()
        icon2.addFile(u":/general/imgs/general/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.faq_small_description_btn.setIcon(icon2)
        self.faq_small_description_btn.setIconSize(QSize(20, 20))
        self.faq_small_description_text = QLabel(self.faq_small_description_grey_background)
        self.faq_small_description_text.setObjectName(u"faq_small_description_text")
        self.faq_small_description_text.setGeometry(QRect(10, 30, 421, 111))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.faq_small_description_text.setFont(font3)
        self.faq_small_description_text.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_small_description_text.setScaledContents(True)
        self.faq_small_description_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_small_description_text.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.faq_small_description_grey_background)


        self.verticalLayout_18.addWidget(self.faq_small_description_white_background)

        self.faq_home_page_white_background = QFrame(self.faq_scroll_area_frame)
        self.faq_home_page_white_background.setObjectName(u"faq_home_page_white_background")
        self.faq_home_page_white_background.setMinimumSize(QSize(470, 34))
        self.faq_home_page_white_background.setMaximumSize(QSize(470, 34))
        self.faq_home_page_white_background.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.faq_home_page_white_background.setFrameShape(QFrame.StyledPanel)
        self.faq_home_page_white_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.faq_home_page_white_background)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(6, 0, 0, 0)
        self.faq_home_page_grey_background = QFrame(self.faq_home_page_white_background)
        self.faq_home_page_grey_background.setObjectName(u"faq_home_page_grey_background")
        self.faq_home_page_grey_background.setMinimumSize(QSize(465, 35))
        self.faq_home_page_grey_background.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.faq_home_page_grey_background.setFrameShape(QFrame.StyledPanel)
        self.faq_home_page_grey_background.setFrameShadow(QFrame.Raised)
        self.faq_home_page_title = QLabel(self.faq_home_page_grey_background)
        self.faq_home_page_title.setObjectName(u"faq_home_page_title")
        self.faq_home_page_title.setGeometry(QRect(10, 0, 401, 35))
        self.faq_home_page_title.setFont(font2)
        self.faq_home_page_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_home_page_btn = QPushButton(self.faq_home_page_grey_background)
        self.faq_home_page_btn.setObjectName(u"faq_home_page_btn")
        self.faq_home_page_btn.setGeometry(QRect(410, 0, 55, 31))
        self.faq_home_page_btn.setMinimumSize(QSize(55, 31))
        self.faq_home_page_btn.setMaximumSize(QSize(55, 31))
        self.faq_home_page_btn.setStyleSheet(u"background: none;")
        self.faq_home_page_btn.setIcon(icon2)
        self.faq_home_page_btn.setIconSize(QSize(20, 20))
        self.faq_home_page_text = QLabel(self.faq_home_page_grey_background)
        self.faq_home_page_text.setObjectName(u"faq_home_page_text")
        self.faq_home_page_text.setGeometry(QRect(10, 30, 421, 91))
        self.faq_home_page_text.setFont(font3)
        self.faq_home_page_text.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_home_page_text.setScaledContents(True)
        self.faq_home_page_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_home_page_text.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.faq_home_page_grey_background)


        self.verticalLayout_18.addWidget(self.faq_home_page_white_background)

        self.faq_scan_page_white_background = QFrame(self.faq_scroll_area_frame)
        self.faq_scan_page_white_background.setObjectName(u"faq_scan_page_white_background")
        self.faq_scan_page_white_background.setMinimumSize(QSize(470, 34))
        self.faq_scan_page_white_background.setMaximumSize(QSize(470, 34))
        self.faq_scan_page_white_background.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.faq_scan_page_white_background.setFrameShape(QFrame.StyledPanel)
        self.faq_scan_page_white_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.faq_scan_page_white_background)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(6, 0, 0, 0)
        self.faq_scan_page_grey_background = QFrame(self.faq_scan_page_white_background)
        self.faq_scan_page_grey_background.setObjectName(u"faq_scan_page_grey_background")
        self.faq_scan_page_grey_background.setMinimumSize(QSize(465, 35))
        self.faq_scan_page_grey_background.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.faq_scan_page_grey_background.setFrameShape(QFrame.StyledPanel)
        self.faq_scan_page_grey_background.setFrameShadow(QFrame.Raised)
        self.faq_scan_page_title = QLabel(self.faq_scan_page_grey_background)
        self.faq_scan_page_title.setObjectName(u"faq_scan_page_title")
        self.faq_scan_page_title.setGeometry(QRect(10, 0, 401, 35))
        self.faq_scan_page_title.setFont(font2)
        self.faq_scan_page_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_scan_page_btn = QPushButton(self.faq_scan_page_grey_background)
        self.faq_scan_page_btn.setObjectName(u"faq_scan_page_btn")
        self.faq_scan_page_btn.setGeometry(QRect(410, 0, 55, 31))
        self.faq_scan_page_btn.setMinimumSize(QSize(55, 31))
        self.faq_scan_page_btn.setMaximumSize(QSize(55, 31))
        self.faq_scan_page_btn.setStyleSheet(u"background: none;")
        self.faq_scan_page_btn.setIcon(icon2)
        self.faq_scan_page_btn.setIconSize(QSize(20, 20))
        self.faq_scan_page_text = QLabel(self.faq_scan_page_grey_background)
        self.faq_scan_page_text.setObjectName(u"faq_scan_page_text")
        self.faq_scan_page_text.setGeometry(QRect(10, 30, 421, 211))
        self.faq_scan_page_text.setFont(font3)
        self.faq_scan_page_text.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_scan_page_text.setScaledContents(True)
        self.faq_scan_page_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_scan_page_text.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.faq_scan_page_grey_background)


        self.verticalLayout_18.addWidget(self.faq_scan_page_white_background)

        self.faq_virus_storage_page_white_background = QFrame(self.faq_scroll_area_frame)
        self.faq_virus_storage_page_white_background.setObjectName(u"faq_virus_storage_page_white_background")
        self.faq_virus_storage_page_white_background.setMinimumSize(QSize(470, 34))
        self.faq_virus_storage_page_white_background.setMaximumSize(QSize(470, 34))
        self.faq_virus_storage_page_white_background.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.faq_virus_storage_page_white_background.setFrameShape(QFrame.StyledPanel)
        self.faq_virus_storage_page_white_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.faq_virus_storage_page_white_background)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(6, 0, 0, 0)
        self.faq_virus_storage_page_grey_background = QFrame(self.faq_virus_storage_page_white_background)
        self.faq_virus_storage_page_grey_background.setObjectName(u"faq_virus_storage_page_grey_background")
        self.faq_virus_storage_page_grey_background.setMinimumSize(QSize(465, 35))
        self.faq_virus_storage_page_grey_background.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.faq_virus_storage_page_grey_background.setFrameShape(QFrame.StyledPanel)
        self.faq_virus_storage_page_grey_background.setFrameShadow(QFrame.Raised)
        self.faq_virus_storage_page_title = QLabel(self.faq_virus_storage_page_grey_background)
        self.faq_virus_storage_page_title.setObjectName(u"faq_virus_storage_page_title")
        self.faq_virus_storage_page_title.setGeometry(QRect(10, 0, 401, 35))
        self.faq_virus_storage_page_title.setFont(font2)
        self.faq_virus_storage_page_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_virus_storage_page_btn = QPushButton(self.faq_virus_storage_page_grey_background)
        self.faq_virus_storage_page_btn.setObjectName(u"faq_virus_storage_page_btn")
        self.faq_virus_storage_page_btn.setGeometry(QRect(410, 0, 55, 31))
        self.faq_virus_storage_page_btn.setMinimumSize(QSize(55, 31))
        self.faq_virus_storage_page_btn.setMaximumSize(QSize(55, 31))
        self.faq_virus_storage_page_btn.setStyleSheet(u"background: none;")
        self.faq_virus_storage_page_btn.setIcon(icon2)
        self.faq_virus_storage_page_btn.setIconSize(QSize(20, 20))
        self.faq_virus_storage_page_text = QLabel(self.faq_virus_storage_page_grey_background)
        self.faq_virus_storage_page_text.setObjectName(u"faq_virus_storage_page_text")
        self.faq_virus_storage_page_text.setGeometry(QRect(10, 30, 421, 161))
        self.faq_virus_storage_page_text.setFont(font3)
        self.faq_virus_storage_page_text.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_virus_storage_page_text.setScaledContents(True)
        self.faq_virus_storage_page_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_virus_storage_page_text.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.faq_virus_storage_page_grey_background)


        self.verticalLayout_18.addWidget(self.faq_virus_storage_page_white_background)

        self.faq_faq_page_white_background = QFrame(self.faq_scroll_area_frame)
        self.faq_faq_page_white_background.setObjectName(u"faq_faq_page_white_background")
        self.faq_faq_page_white_background.setMinimumSize(QSize(470, 34))
        self.faq_faq_page_white_background.setMaximumSize(QSize(470, 34))
        self.faq_faq_page_white_background.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.faq_faq_page_white_background.setFrameShape(QFrame.StyledPanel)
        self.faq_faq_page_white_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.faq_faq_page_white_background)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(6, 0, 0, 0)
        self.faq_faq_page_grey_background = QFrame(self.faq_faq_page_white_background)
        self.faq_faq_page_grey_background.setObjectName(u"faq_faq_page_grey_background")
        self.faq_faq_page_grey_background.setMinimumSize(QSize(465, 35))
        self.faq_faq_page_grey_background.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.faq_faq_page_grey_background.setFrameShape(QFrame.StyledPanel)
        self.faq_faq_page_grey_background.setFrameShadow(QFrame.Raised)
        self.faq_faq_page_title = QLabel(self.faq_faq_page_grey_background)
        self.faq_faq_page_title.setObjectName(u"faq_faq_page_title")
        self.faq_faq_page_title.setGeometry(QRect(10, 0, 401, 35))
        self.faq_faq_page_title.setFont(font2)
        self.faq_faq_page_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_faq_page_btn = QPushButton(self.faq_faq_page_grey_background)
        self.faq_faq_page_btn.setObjectName(u"faq_faq_page_btn")
        self.faq_faq_page_btn.setGeometry(QRect(410, 0, 55, 31))
        self.faq_faq_page_btn.setMinimumSize(QSize(55, 31))
        self.faq_faq_page_btn.setMaximumSize(QSize(55, 31))
        self.faq_faq_page_btn.setStyleSheet(u"background: none;")
        self.faq_faq_page_btn.setIcon(icon2)
        self.faq_faq_page_btn.setIconSize(QSize(20, 20))
        self.faq_faq_page_text = QLabel(self.faq_faq_page_grey_background)
        self.faq_faq_page_text.setObjectName(u"faq_faq_page_text")
        self.faq_faq_page_text.setGeometry(QRect(10, 30, 421, 91))
        self.faq_faq_page_text.setFont(font3)
        self.faq_faq_page_text.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_faq_page_text.setScaledContents(True)
        self.faq_faq_page_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_faq_page_text.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.faq_faq_page_grey_background)


        self.verticalLayout_18.addWidget(self.faq_faq_page_white_background)

        self.faq_settings_page_white_background = QFrame(self.faq_scroll_area_frame)
        self.faq_settings_page_white_background.setObjectName(u"faq_settings_page_white_background")
        self.faq_settings_page_white_background.setMinimumSize(QSize(470, 34))
        self.faq_settings_page_white_background.setMaximumSize(QSize(470, 34))
        self.faq_settings_page_white_background.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.faq_settings_page_white_background.setFrameShape(QFrame.StyledPanel)
        self.faq_settings_page_white_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.faq_settings_page_white_background)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(6, 0, 0, 0)
        self.faq_settings_page_grey_background = QFrame(self.faq_settings_page_white_background)
        self.faq_settings_page_grey_background.setObjectName(u"faq_settings_page_grey_background")
        self.faq_settings_page_grey_background.setMinimumSize(QSize(465, 35))
        self.faq_settings_page_grey_background.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.faq_settings_page_grey_background.setFrameShape(QFrame.StyledPanel)
        self.faq_settings_page_grey_background.setFrameShadow(QFrame.Raised)
        self.faq_settings_page_title = QLabel(self.faq_settings_page_grey_background)
        self.faq_settings_page_title.setObjectName(u"faq_settings_page_title")
        self.faq_settings_page_title.setGeometry(QRect(10, 0, 401, 35))
        self.faq_settings_page_title.setFont(font2)
        self.faq_settings_page_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_settings_page_btn = QPushButton(self.faq_settings_page_grey_background)
        self.faq_settings_page_btn.setObjectName(u"faq_settings_page_btn")
        self.faq_settings_page_btn.setGeometry(QRect(410, 0, 55, 31))
        self.faq_settings_page_btn.setMinimumSize(QSize(55, 31))
        self.faq_settings_page_btn.setMaximumSize(QSize(55, 31))
        self.faq_settings_page_btn.setStyleSheet(u"background: none;")
        self.faq_settings_page_btn.setIcon(icon2)
        self.faq_settings_page_btn.setIconSize(QSize(20, 20))
        self.faq_settings_page_text = QLabel(self.faq_settings_page_grey_background)
        self.faq_settings_page_text.setObjectName(u"faq_settings_page_text")
        self.faq_settings_page_text.setGeometry(QRect(10, 30, 401, 71))
        self.faq_settings_page_text.setFont(font3)
        self.faq_settings_page_text.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_settings_page_text.setScaledContents(True)
        self.faq_settings_page_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_settings_page_text.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.faq_settings_page_grey_background)


        self.verticalLayout_18.addWidget(self.faq_settings_page_white_background)

        self.faq_authors_white_background = QFrame(self.faq_scroll_area_frame)
        self.faq_authors_white_background.setObjectName(u"faq_authors_white_background")
        self.faq_authors_white_background.setMinimumSize(QSize(470, 34))
        self.faq_authors_white_background.setMaximumSize(QSize(470, 34))
        self.faq_authors_white_background.setFont(font3)
        self.faq_authors_white_background.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.faq_authors_white_background.setFrameShape(QFrame.StyledPanel)
        self.faq_authors_white_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.faq_authors_white_background)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(6, 0, 0, 0)
        self.faq_authors_grey_background = QFrame(self.faq_authors_white_background)
        self.faq_authors_grey_background.setObjectName(u"faq_authors_grey_background")
        self.faq_authors_grey_background.setMinimumSize(QSize(465, 35))
        self.faq_authors_grey_background.setMaximumSize(QSize(16777215, 16777215))
        self.faq_authors_grey_background.setStyleSheet(u"QFrame {	\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.faq_authors_grey_background.setFrameShape(QFrame.StyledPanel)
        self.faq_authors_grey_background.setFrameShadow(QFrame.Raised)
        self.faq_authors_title = QLabel(self.faq_authors_grey_background)
        self.faq_authors_title.setObjectName(u"faq_authors_title")
        self.faq_authors_title.setGeometry(QRect(10, 0, 401, 35))
        self.faq_authors_title.setFont(font2)
        self.faq_authors_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_authors_btn = QPushButton(self.faq_authors_grey_background)
        self.faq_authors_btn.setObjectName(u"faq_authors_btn")
        self.faq_authors_btn.setGeometry(QRect(410, 0, 55, 31))
        self.faq_authors_btn.setMinimumSize(QSize(55, 31))
        self.faq_authors_btn.setMaximumSize(QSize(55, 31))
        self.faq_authors_btn.setStyleSheet(u"background: none;")
        self.faq_authors_btn.setIcon(icon2)
        self.faq_authors_btn.setIconSize(QSize(20, 20))
        self.faq_authors_text = QLabel(self.faq_authors_grey_background)
        self.faq_authors_text.setObjectName(u"faq_authors_text")
        self.faq_authors_text.setGeometry(QRect(10, 40, 421, 91))
        self.faq_authors_text.setFont(font3)
        self.faq_authors_text.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.faq_authors_text.setScaledContents(True)
        self.faq_authors_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.faq_authors_text.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.faq_authors_grey_background)


        self.verticalLayout_18.addWidget(self.faq_authors_white_background)


        self.verticalLayout_5.addWidget(self.faq_scroll_area_frame, 0, Qt.AlignTop)

        self.faq_scroll_area.setWidget(self.faq_scroll_area_widget)
        self.faq_logo = QLabel(self.faq_main_menu)
        self.faq_logo.setObjectName(u"faq_logo")
        self.faq_logo.setGeometry(QRect(510, 0, 361, 361))
        self.faq_logo.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.faq_logo.setPixmap(QPixmap(u":/general/imgs/general/SpectrumLogo.png"))
        self.faq_secret_way = QFrame(self.faq_main_menu)
        self.faq_secret_way.setObjectName(u"faq_secret_way")
        self.faq_secret_way.setGeometry(QRect(760, 47, 53, 47))
        self.faq_secret_way.setStyleSheet(u"background: none;")
        self.faq_secret_way.setFrameShape(QFrame.StyledPanel)
        self.faq_secret_way.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.faq_main_menu)

        self.Pages.addWidget(self.FaqPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.verticalLayout_4 = QVBoxLayout(self.SettingsPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settings_main_menu = QFrame(self.SettingsPage)
        self.settings_main_menu.setObjectName(u"settings_main_menu")
        self.settings_main_menu.setStyleSheet(u"background-color: #2C2C2C;\n"
"border-radius: 15px;")
        self.settings_main_menu.setFrameShape(QFrame.StyledPanel)
        self.settings_main_menu.setFrameShadow(QFrame.Raised)
        self.settings_scroll_area = QScrollArea(self.settings_main_menu)
        self.settings_scroll_area.setObjectName(u"settings_scroll_area")
        self.settings_scroll_area.setGeometry(QRect(10, 12, 491, 340))
        self.settings_scroll_area.setLayoutDirection(Qt.RightToLeft)
        self.settings_scroll_area.setAutoFillBackground(False)
        self.settings_scroll_area.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;")
        self.settings_scroll_area.setFrameShadow(QFrame.Sunken)
        self.settings_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.settings_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.settings_scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.settings_scroll_area.setWidgetResizable(True)
        self.settings_scroll_area.setAlignment(Qt.AlignCenter)
        self.settings_scroll_area_widget = QWidget()
        self.settings_scroll_area_widget.setObjectName(u"settings_scroll_area_widget")
        self.settings_scroll_area_widget.setGeometry(QRect(0, 0, 485, 340))
        self.verticalLayout_6 = QVBoxLayout(self.settings_scroll_area_widget)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settings_scroll_area_frame = QFrame(self.settings_scroll_area_widget)
        self.settings_scroll_area_frame.setObjectName(u"settings_scroll_area_frame")
        self.settings_scroll_area_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_scroll_area_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.settings_scroll_area_frame)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.settings_lang_white = QFrame(self.settings_scroll_area_frame)
        self.settings_lang_white.setObjectName(u"settings_lang_white")
        self.settings_lang_white.setMinimumSize(QSize(470, 35))
        self.settings_lang_white.setMaximumSize(QSize(470, 35))
        self.settings_lang_white.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.settings_lang_white.setFrameShape(QFrame.StyledPanel)
        self.settings_lang_white.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.settings_lang_white)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 0, 0, 0)
        self.settings_lang_grey = QFrame(self.settings_lang_white)
        self.settings_lang_grey.setObjectName(u"settings_lang_grey")
        self.settings_lang_grey.setMinimumSize(QSize(465, 35))
        self.settings_lang_grey.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.settings_lang_grey.setFrameShape(QFrame.StyledPanel)
        self.settings_lang_grey.setFrameShadow(QFrame.Raised)
        self.settings_lang_title = QLabel(self.settings_lang_grey)
        self.settings_lang_title.setObjectName(u"settings_lang_title")
        self.settings_lang_title.setGeometry(QRect(10, 0, 395, 34))
        self.settings_lang_title.setMinimumSize(QSize(380, 0))
        self.settings_lang_title.setFont(font2)
        self.settings_lang_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.settings_lang_btn = QPushButton(self.settings_lang_grey)
        self.settings_lang_btn.setObjectName(u"settings_lang_btn")
        self.settings_lang_btn.setGeometry(QRect(410, 0, 55, 31))
        self.settings_lang_btn.setMinimumSize(QSize(55, 31))
        self.settings_lang_btn.setMaximumSize(QSize(55, 31))
        self.settings_lang_btn.setStyleSheet(u"background: none;")
        self.settings_lang_btn.setIcon(icon2)
        self.settings_lang_btn.setIconSize(QSize(20, 20))
        self.settings_lang_rus_frame = QFrame(self.settings_lang_grey)
        self.settings_lang_rus_frame.setObjectName(u"settings_lang_rus_frame")
        self.settings_lang_rus_frame.setGeometry(QRect(0, 33, 464, 31))
        self.settings_lang_rus_frame.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.settings_lang_rus_frame.setStyleSheet(u"QFrame {\n"
"	background-color: none;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.settings_lang_rus_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_lang_rus_frame.setFrameShadow(QFrame.Raised)
        self.settings_lang_rus_title = QLabel(self.settings_lang_rus_frame)
        self.settings_lang_rus_title.setObjectName(u"settings_lang_rus_title")
        self.settings_lang_rus_title.setGeometry(QRect(10, 0, 401, 31))
        self.settings_lang_rus_title.setFont(font2)
        self.settings_lang_rus_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.settings_lang_rus_title.setScaledContents(True)
        self.settings_lang_rus_title.setWordWrap(True)
        self.settings_lang_rus_icon = QLabel(self.settings_lang_rus_frame)
        self.settings_lang_rus_icon.setObjectName(u"settings_lang_rus_icon")
        self.settings_lang_rus_icon.setGeometry(QRect(426, 0, 25, 35))
        self.settings_lang_rus_icon.setMinimumSize(QSize(25, 35))
        self.settings_lang_rus_icon.setMaximumSize(QSize(25, 35))
        self.settings_lang_rus_icon.setStyleSheet(u"")
        self.settings_lang_rus_icon.setPixmap(QPixmap(u":/general/imgs/general/checked.png"))
        self.settings_lang_eng_frame = QFrame(self.settings_lang_grey)
        self.settings_lang_eng_frame.setObjectName(u"settings_lang_eng_frame")
        self.settings_lang_eng_frame.setGeometry(QRect(0, 63, 464, 31))
        self.settings_lang_eng_frame.setStyleSheet(u"QFrame {\n"
"	background-color: none;\n"
"	border-radius: 0px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.settings_lang_eng_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_lang_eng_frame.setFrameShadow(QFrame.Raised)
        self.settings_lang_eng_title = QLabel(self.settings_lang_eng_frame)
        self.settings_lang_eng_title.setObjectName(u"settings_lang_eng_title")
        self.settings_lang_eng_title.setGeometry(QRect(10, 0, 411, 31))
        self.settings_lang_eng_title.setFont(font2)
        self.settings_lang_eng_title.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.settings_lang_eng_title.setScaledContents(True)
        self.settings_lang_eng_title.setWordWrap(True)
        self.settings_lang_eng_icon = QLabel(self.settings_lang_eng_frame)
        self.settings_lang_eng_icon.setObjectName(u"settings_lang_eng_icon")
        self.settings_lang_eng_icon.setGeometry(QRect(426, 0, 25, 35))
        self.settings_lang_eng_icon.setMinimumSize(QSize(25, 35))
        self.settings_lang_eng_icon.setMaximumSize(QSize(25, 35))
        self.settings_lang_eng_icon.setStyleSheet(u"")
        self.settings_lang_eng_icon.setPixmap(QPixmap(u":/general/imgs/general/checked.png"))

        self.verticalLayout_8.addWidget(self.settings_lang_grey)


        self.verticalLayout_14.addWidget(self.settings_lang_white)


        self.verticalLayout_6.addWidget(self.settings_scroll_area_frame, 0, Qt.AlignTop)

        self.settings_scroll_area.setWidget(self.settings_scroll_area_widget)
        self.settings_logo = QLabel(self.settings_main_menu)
        self.settings_logo.setObjectName(u"settings_logo")
        self.settings_logo.setGeometry(QRect(510, 0, 361, 361))
        self.settings_logo.setStyleSheet(u"background: transparent;\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.settings_logo.setPixmap(QPixmap(u":/general/imgs/general/SpectrumLogo.png"))
        self.settings_secret_way = QFrame(self.settings_main_menu)
        self.settings_secret_way.setObjectName(u"settings_secret_way")
        self.settings_secret_way.setGeometry(QRect(760, 47, 53, 47))
        self.settings_secret_way.setStyleSheet(u"background: none;")
        self.settings_secret_way.setFrameShape(QFrame.StyledPanel)
        self.settings_secret_way.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.settings_main_menu)

        self.Pages.addWidget(self.SettingsPage)
        self.VirusStoragePage = QWidget()
        self.VirusStoragePage.setObjectName(u"VirusStoragePage")
        self.verticalLayout_31 = QVBoxLayout(self.VirusStoragePage)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.virus_storage_main_menu = QFrame(self.VirusStoragePage)
        self.virus_storage_main_menu.setObjectName(u"virus_storage_main_menu")
        self.virus_storage_main_menu.setStyleSheet(u"background-color: #2C2C2C;\n"
"border-radius: 15px;")
        self.virus_storage_main_menu.setFrameShape(QFrame.StyledPanel)
        self.virus_storage_main_menu.setFrameShadow(QFrame.Raised)
        self.virus_storage_scroll_area = QScrollArea(self.virus_storage_main_menu)
        self.virus_storage_scroll_area.setObjectName(u"virus_storage_scroll_area")
        self.virus_storage_scroll_area.setGeometry(QRect(10, 10, 851, 341))
        self.virus_storage_scroll_area.setLayoutDirection(Qt.RightToLeft)
        self.virus_storage_scroll_area.setAutoFillBackground(False)
        self.virus_storage_scroll_area.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;")
        self.virus_storage_scroll_area.setFrameShadow(QFrame.Sunken)
        self.virus_storage_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.virus_storage_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.virus_storage_scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.virus_storage_scroll_area.setWidgetResizable(True)
        self.virus_storage_scroll_area.setAlignment(Qt.AlignCenter)
        self.virus_storage_scroll_area_widget = QWidget()
        self.virus_storage_scroll_area_widget.setObjectName(u"virus_storage_scroll_area_widget")
        self.virus_storage_scroll_area_widget.setGeometry(QRect(0, 0, 845, 341))
        self.verticalLayout_22 = QVBoxLayout(self.virus_storage_scroll_area_widget)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.virus_storage_scroll_area_frame = QFrame(self.virus_storage_scroll_area_widget)
        self.virus_storage_scroll_area_frame.setObjectName(u"virus_storage_scroll_area_frame")
        self.virus_storage_scroll_area_frame.setFrameShape(QFrame.StyledPanel)
        self.virus_storage_scroll_area_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.virus_storage_scroll_area_frame)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.virus_storage_main_title = QFrame(self.virus_storage_scroll_area_frame)
        self.virus_storage_main_title.setObjectName(u"virus_storage_main_title")
        self.virus_storage_main_title.setMinimumSize(QSize(830, 100))
        self.virus_storage_main_title.setMaximumSize(QSize(830, 130))
        self.virus_storage_main_title.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.virus_storage_main_title.setFrameShape(QFrame.StyledPanel)
        self.virus_storage_main_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.virus_storage_main_title)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(6, 0, 0, 0)
        self.virus_storage_title_grey = QFrame(self.virus_storage_main_title)
        self.virus_storage_title_grey.setObjectName(u"virus_storage_title_grey")
        self.virus_storage_title_grey.setMinimumSize(QSize(0, 0))
        self.virus_storage_title_grey.setStyleSheet(u"QFrame {\n"
"background-color: #383838;\n"
"border-radius: 10px;\n"
"border-top-left-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.virus_storage_title_grey.setFrameShape(QFrame.StyledPanel)
        self.virus_storage_title_grey.setFrameShadow(QFrame.Raised)
        self.virus_storage_main_title_label = QLabel(self.virus_storage_title_grey)
        self.virus_storage_main_title_label.setObjectName(u"virus_storage_main_title_label")
        self.virus_storage_main_title_label.setGeometry(QRect(10, 5, 451, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.virus_storage_main_title_label.setFont(font4)
        self.virus_storage_main_title_label.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.virus_storage_warning = QLabel(self.virus_storage_title_grey)
        self.virus_storage_warning.setObjectName(u"virus_storage_warning")
        self.virus_storage_warning.setGeometry(QRect(10, 40, 721, 51))
        self.virus_storage_warning.setFont(font1)
        self.virus_storage_warning.setStyleSheet(u"color: #FFF;\n"
"background: none;")
        self.virus_storage_warning.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.virus_storage_title_grey)


        self.verticalLayout_23.addWidget(self.virus_storage_main_title)

        self.virus_storage_finded_viruses = QFrame(self.virus_storage_scroll_area_frame)
        self.virus_storage_finded_viruses.setObjectName(u"virus_storage_finded_viruses")
        self.virus_storage_finded_viruses.setMinimumSize(QSize(500, 230))
        self.virus_storage_finded_viruses.setMaximumSize(QSize(830, 16777215))
        self.virus_storage_finded_viruses.setStyleSheet(u"background-color: #FFF;\n"
"border-radius: 10px;\n"
"border-top-right-radius: 17px;\n"
"border-bottom-right-radius: 17px;")
        self.virus_storage_finded_viruses.setFrameShape(QFrame.StyledPanel)
        self.virus_storage_finded_viruses.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.virus_storage_finded_viruses)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(6, 0, 0, 0)
        self.virus_storage_finded_viruses_grey = QFrame(self.virus_storage_finded_viruses)
        self.virus_storage_finded_viruses_grey.setObjectName(u"virus_storage_finded_viruses_grey")
        self.virus_storage_finded_viruses_grey.setMinimumSize(QSize(465, 35))
        self.virus_storage_finded_viruses_grey.setStyleSheet(u"QFrame {\n"
"	background-color: #383838;\n"
"	border-radius: 10px;\n"
"	border-top-left-radius: 8px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	background-color: #3C3C3C;\n"
"}")
        self.virus_storage_finded_viruses_grey.setFrameShape(QFrame.StyledPanel)
        self.virus_storage_finded_viruses_grey.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.virus_storage_finded_viruses_grey)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(10, 4, 0, 4)
        self.virus_storage_table = QTableWidget(self.virus_storage_finded_viruses_grey)
        if (self.virus_storage_table.columnCount() < 6):
            self.virus_storage_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.virus_storage_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.virus_storage_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.virus_storage_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.virus_storage_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.virus_storage_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.virus_storage_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.virus_storage_table.setObjectName(u"virus_storage_table")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.virus_storage_table.setFont(font5)
        self.virus_storage_table.setFocusPolicy(Qt.NoFocus)
        self.virus_storage_table.setLayoutDirection(Qt.LeftToRight)
        self.virus_storage_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"}\n"
"QTableWidget::item{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	margin-left: 10px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.virus_storage_table.setFrameShape(QFrame.StyledPanel)
        self.virus_storage_table.setFrameShadow(QFrame.Sunken)
        self.virus_storage_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.virus_storage_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.virus_storage_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.virus_storage_table.setAutoScroll(False)
        self.virus_storage_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.virus_storage_table.setTabKeyNavigation(False)
        self.virus_storage_table.setProperty("showDropIndicator", False)
        self.virus_storage_table.setDragDropOverwriteMode(False)
        self.virus_storage_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.virus_storage_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.virus_storage_table.setTextElideMode(Qt.ElideNone)
        self.virus_storage_table.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.virus_storage_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.virus_storage_table.setShowGrid(False)
        self.virus_storage_table.setWordWrap(False)
        self.virus_storage_table.setCornerButtonEnabled(False)
        self.virus_storage_table.horizontalHeader().setVisible(False)
        self.virus_storage_table.horizontalHeader().setHighlightSections(False)
        self.virus_storage_table.verticalHeader().setVisible(False)

        self.horizontalLayout_32.addWidget(self.virus_storage_table)


        self.verticalLayout_30.addWidget(self.virus_storage_finded_viruses_grey)


        self.verticalLayout_23.addWidget(self.virus_storage_finded_viruses)


        self.verticalLayout_22.addWidget(self.virus_storage_scroll_area_frame, 0, Qt.AlignTop)

        self.virus_storage_scroll_area.setWidget(self.virus_storage_scroll_area_widget)

        self.verticalLayout_31.addWidget(self.virus_storage_main_menu)

        self.Pages.addWidget(self.VirusStoragePage)
        self.bottom_menu_scroll_area = QScrollArea(self.BackGround)
        self.bottom_menu_scroll_area.setObjectName(u"bottom_menu_scroll_area")
        self.bottom_menu_scroll_area.setGeometry(QRect(12, 435, 876, 113))
        self.bottom_menu_scroll_area.setStyleSheet(u"")
        self.bottom_menu_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.bottom_menu_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.bottom_menu_scroll_area.setWidgetResizable(True)
        self.bottom_menu_scroll_area.setAlignment(Qt.AlignCenter)
        self.bottom_menu_scroll_area_widget = QWidget()
        self.bottom_menu_scroll_area_widget.setObjectName(u"bottom_menu_scroll_area_widget")
        self.bottom_menu_scroll_area_widget.setGeometry(QRect(0, 0, 1098, 108))
        self.bottom_menu_scroll_area_widget.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.bottom_menu_scroll_area_widget)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.bottom_menu_frame = QFrame(self.bottom_menu_scroll_area_widget)
        self.bottom_menu_frame.setObjectName(u"bottom_menu_frame")
        self.bottom_menu_frame.setMinimumSize(QSize(0, 0))
        self.bottom_menu_frame.setStyleSheet(u"")
        self.bottom_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_menu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottom_menu_frame)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bottom_menu_home = QFrame(self.bottom_menu_frame)
        self.bottom_menu_home.setObjectName(u"bottom_menu_home")
        self.bottom_menu_home.setMinimumSize(QSize(210, 100))
        self.bottom_menu_home.setMaximumSize(QSize(210, 100))
        self.bottom_menu_home.setStyleSheet(u"QFrame {\n"
"	background-color: #2C2C2C;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid #FFF;\n"
"	background-color: #3C3C3C;\n"
"}\n"
"")
        self.bottom_menu_home.setFrameShape(QFrame.StyledPanel)
        self.bottom_menu_home.setFrameShadow(QFrame.Raised)
        self.home_title = QLabel(self.bottom_menu_home)
        self.home_title.setObjectName(u"home_title")
        self.home_title.setGeometry(QRect(60, 10, 141, 41))
        self.home_title.setFont(font)
        self.home_title.setStyleSheet(u"border: none;\n"
"color: #FFF;\n"
"background: none")
        self.home_description = QLabel(self.bottom_menu_home)
        self.home_description.setObjectName(u"home_description")
        self.home_description.setGeometry(QRect(0, 74, 211, 20))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setWeight(75)
        self.home_description.setFont(font6)
        self.home_description.setStyleSheet(u"border: none;\n"
"color: #FFFFFF;\n"
"background-color: none;")
        self.home_description.setAlignment(Qt.AlignCenter)
        self.home_icon = QLabel(self.bottom_menu_home)
        self.home_icon.setObjectName(u"home_icon")
        self.home_icon.setGeometry(QRect(10, 10, 41, 41))
        self.home_icon.setStyleSheet(u"border: none;\n"
"border-radius: 0px;\n"
"background: none;")
        self.home_icon.setPixmap(QPixmap(u":/bottom_menu/imgs/bottom_menu/home_icon.png"))

        self.horizontalLayout.addWidget(self.bottom_menu_home)

        self.bottom_menu_scanning = QFrame(self.bottom_menu_frame)
        self.bottom_menu_scanning.setObjectName(u"bottom_menu_scanning")
        self.bottom_menu_scanning.setMinimumSize(QSize(210, 100))
        self.bottom_menu_scanning.setMaximumSize(QSize(210, 100))
        self.bottom_menu_scanning.setStyleSheet(u"QFrame {\n"
"	background-color: #2C2C2C;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid #FFF;	\n"
"	background-color: #3C3C3C;\n"
"}")
        self.bottom_menu_scanning.setFrameShape(QFrame.StyledPanel)
        self.bottom_menu_scanning.setFrameShadow(QFrame.Raised)
        self.scanning_title = QLabel(self.bottom_menu_scanning)
        self.scanning_title.setObjectName(u"scanning_title")
        self.scanning_title.setGeometry(QRect(60, 10, 141, 41))
        self.scanning_title.setFont(font)
        self.scanning_title.setStyleSheet(u"border: none;\n"
"color: #FFF;\n"
"background: none;")
        self.scanning_description = QLabel(self.bottom_menu_scanning)
        self.scanning_description.setObjectName(u"scanning_description")
        self.scanning_description.setGeometry(QRect(0, 74, 211, 20))
        self.scanning_description.setFont(font6)
        self.scanning_description.setStyleSheet(u"border: none;\n"
"color: #FFFFFF;\n"
"background-color: none;")
        self.scanning_description.setAlignment(Qt.AlignCenter)
        self.scanning_icon = QLabel(self.bottom_menu_scanning)
        self.scanning_icon.setObjectName(u"scanning_icon")
        self.scanning_icon.setGeometry(QRect(10, 10, 41, 41))
        self.scanning_icon.setStyleSheet(u"border: none;\n"
"border-radius: 0px;\n"
"background: none;")
        self.scanning_icon.setPixmap(QPixmap(u":/bottom_menu/imgs/bottom_menu/scanning_icon.png"))

        self.horizontalLayout.addWidget(self.bottom_menu_scanning)

        self.bottom_menu_virus_storage = QFrame(self.bottom_menu_frame)
        self.bottom_menu_virus_storage.setObjectName(u"bottom_menu_virus_storage")
        self.bottom_menu_virus_storage.setMinimumSize(QSize(210, 100))
        self.bottom_menu_virus_storage.setMaximumSize(QSize(210, 100))
        self.bottom_menu_virus_storage.setStyleSheet(u"QFrame {\n"
"	background-color: #2C2C2C;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid #FFF;\n"
"	background-color: #3C3C3C;\n"
"}\n"
"")
        self.bottom_menu_virus_storage.setFrameShape(QFrame.StyledPanel)
        self.bottom_menu_virus_storage.setFrameShadow(QFrame.Raised)
        self.virus_storage_title = QLabel(self.bottom_menu_virus_storage)
        self.virus_storage_title.setObjectName(u"virus_storage_title")
        self.virus_storage_title.setGeometry(QRect(60, 10, 141, 41))
        self.virus_storage_title.setFont(font)
        self.virus_storage_title.setStyleSheet(u"border: none;\n"
"color: #FFF;\n"
"background: none")
        self.virus_storage_description = QLabel(self.bottom_menu_virus_storage)
        self.virus_storage_description.setObjectName(u"virus_storage_description")
        self.virus_storage_description.setGeometry(QRect(0, 74, 211, 20))
        self.virus_storage_description.setFont(font6)
        self.virus_storage_description.setStyleSheet(u"border: none;\n"
"color: #FFFFFF;\n"
"background-color: none;")
        self.virus_storage_description.setAlignment(Qt.AlignCenter)
        self.virus_storage_icon = QLabel(self.bottom_menu_virus_storage)
        self.virus_storage_icon.setObjectName(u"virus_storage_icon")
        self.virus_storage_icon.setGeometry(QRect(10, 10, 41, 41))
        self.virus_storage_icon.setStyleSheet(u"border: none;\n"
"border-radius: 0px;\n"
"background: none;")
        self.virus_storage_icon.setPixmap(QPixmap(u":/bottom_menu/imgs/bottom_menu/virus_storage_icon.png"))

        self.horizontalLayout.addWidget(self.bottom_menu_virus_storage)

        self.bottom_menu_faq = QFrame(self.bottom_menu_frame)
        self.bottom_menu_faq.setObjectName(u"bottom_menu_faq")
        self.bottom_menu_faq.setMinimumSize(QSize(210, 100))
        self.bottom_menu_faq.setMaximumSize(QSize(210, 100))
        self.bottom_menu_faq.setStyleSheet(u"QFrame {\n"
"	background-color: #2C2C2C;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid #FFF;\n"
"	background-color: #3C3C3C;\n"
"}")
        self.bottom_menu_faq.setFrameShape(QFrame.StyledPanel)
        self.bottom_menu_faq.setFrameShadow(QFrame.Raised)
        self.faq_description = QLabel(self.bottom_menu_faq)
        self.faq_description.setObjectName(u"faq_description")
        self.faq_description.setGeometry(QRect(0, 74, 211, 20))
        self.faq_description.setFont(font6)
        self.faq_description.setStyleSheet(u"border: none;\n"
"color: #FFFFFF;\n"
"background-color: none;")
        self.faq_description.setAlignment(Qt.AlignCenter)
        self.faq_title = QLabel(self.bottom_menu_faq)
        self.faq_title.setObjectName(u"faq_title")
        self.faq_title.setGeometry(QRect(60, 10, 141, 41))
        self.faq_title.setFont(font)
        self.faq_title.setStyleSheet(u"border: none;\n"
"color: #FFF;\n"
"background: none;")
        self.faq_icon = QLabel(self.bottom_menu_faq)
        self.faq_icon.setObjectName(u"faq_icon")
        self.faq_icon.setGeometry(QRect(10, 10, 41, 41))
        self.faq_icon.setStyleSheet(u"border: none;\n"
"border-radius: 0px;\n"
"background: none;")
        self.faq_icon.setPixmap(QPixmap(u":/bottom_menu/imgs/bottom_menu/faq_icon.png"))

        self.horizontalLayout.addWidget(self.bottom_menu_faq)

        self.bottom_menu_settings = QFrame(self.bottom_menu_frame)
        self.bottom_menu_settings.setObjectName(u"bottom_menu_settings")
        self.bottom_menu_settings.setMinimumSize(QSize(210, 100))
        self.bottom_menu_settings.setStyleSheet(u"QFrame {\n"
"	background-color: #2C2C2C;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid #FFF;\n"
"	background-color: #3C3C3C;\n"
"}")
        self.bottom_menu_settings.setFrameShape(QFrame.StyledPanel)
        self.bottom_menu_settings.setFrameShadow(QFrame.Raised)
        self.settings_title = QLabel(self.bottom_menu_settings)
        self.settings_title.setObjectName(u"settings_title")
        self.settings_title.setGeometry(QRect(60, 10, 141, 41))
        self.settings_title.setFont(font)
        self.settings_title.setStyleSheet(u"border: none;\n"
"color: #FFF;\n"
"background: none;")
        self.settings_description = QLabel(self.bottom_menu_settings)
        self.settings_description.setObjectName(u"settings_description")
        self.settings_description.setGeometry(QRect(0, 74, 211, 20))
        self.settings_description.setFont(font6)
        self.settings_description.setStyleSheet(u"border: none;\n"
"color: #FFFFFF;\n"
"background-color: none;")
        self.settings_description.setAlignment(Qt.AlignCenter)
        self.settiongs_icon = QLabel(self.bottom_menu_settings)
        self.settiongs_icon.setObjectName(u"settiongs_icon")
        self.settiongs_icon.setGeometry(QRect(10, 10, 41, 41))
        self.settiongs_icon.setStyleSheet(u"border: none;\n"
"border-radius: 0px;\n"
"background: none;")
        self.settiongs_icon.setPixmap(QPixmap(u":/bottom_menu/imgs/bottom_menu/settings_icon.png"))

        self.horizontalLayout.addWidget(self.bottom_menu_settings)


        self.verticalLayout_25.addWidget(self.bottom_menu_frame, 0, Qt.AlignTop)

        self.bottom_menu_scroll_area.setWidget(self.bottom_menu_scroll_area_widget)
        MainWindow.setCentralWidget(self.BackGround)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.top_menu_icon.setText("")
        self.top_menu_title.setText(QCoreApplication.translate("MainWindow", u"SPECTRUM SECURITY", None))
        self.top_menu_minimize_btn.setText("")
        self.top_menu_close_btn.setText("")
        self.RAM_progress.setText(QCoreApplication.translate("MainWindow", u"RAM - 0%", None))
        self.RAM_total_info.setText(QCoreApplication.translate("MainWindow", u"Total: 0GB", None))
        self.RAM_used_info.setText(QCoreApplication.translate("MainWindow", u"Used: 0GB", None))
        self.CPU_progress.setText(QCoreApplication.translate("MainWindow", u"CPU - 0%", None))
        self.CPU_info.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.Physical_cores_info.setText(QCoreApplication.translate("MainWindow", u"Physical cores: 0", None))
        self.Frequency_info.setText(QCoreApplication.translate("MainWindow", u"Frequency: 0MHz", None))
        self.GPU_progress.setText(QCoreApplication.translate("MainWindow", u"GPU - 0%", None))
        self.GPU_model_info.setText(QCoreApplication.translate("MainWindow", u"Model: not found", None))
        self.GPU_vram_total_info.setText(QCoreApplication.translate("MainWindow", u"Total VRAM: 0.0MB", None))
        self.GPU_vram_used_info.setText(QCoreApplication.translate("MainWindow", u"Used VRAM: 0.0MB", None))
        self.home_logo.setText("")
        self.scanning_choose_btn_full.setText(QCoreApplication.translate("MainWindow", u"FULL", None))
        self.scanning_choose_btn_folder.setText(QCoreApplication.translate("MainWindow", u"FOLDER", None))
        self.scanning_choose_btn_file.setText(QCoreApplication.translate("MainWindow", u"FILE", None))
        self.scanning_start_btn.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
        self.scanning_logo.setText("")
        self.faq_small_description_title.setText(QCoreApplication.translate("MainWindow", u"Small description", None))
        self.faq_small_description_btn.setText("")
        self.faq_small_description_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Spectrum Security is a start-up project that is rapidly gaining momentum.  We have a fairly large database of viruses, in the amount of 30 million, as well as our own artificial intelligence that can detect any malware.</p></body></html>", None))
        self.faq_home_page_title.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.faq_home_page_btn.setText("")
        self.faq_home_page_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The Home page, or the Main page, is responsible for displaying information about the load of your PC. It presents the most important parameters, namely the CPU, RAM and GPU load.</p></body></html>", None))
        self.faq_scan_page_title.setText(QCoreApplication.translate("MainWindow", u"Scanning Page", None))
        self.faq_scan_page_btn.setText("")
        self.faq_scan_page_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>In the scan tab on top we are greeted by a small menu consisting of 3 buttons: Full, Folder and File. It is responsible for selecting the scanning mode. Full - scan of your entire computer for viruses. Folder - checking the folder you selected. File - checking the file you selected. Just below this menu is a circular indicator of the scanning process. At the very bottom there is a &quot;Scan&quot; button, after clicking on which a scan will be performed in the mode you selected.</p></body></html>", None))
        self.faq_virus_storage_page_title.setText(QCoreApplication.translate("MainWindow", u"Virus Storage Page", None))
        self.faq_virus_storage_page_btn.setText("")
        self.faq_virus_storage_page_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The Storage tab is responsible for storing and interacting with found viruses. The line with the found threat will contain information: the date of the scan, the type of threat and the path to the malicious file. There are also three buttons, the first is responsible for copying the path to the file, the second for deleting the infected file, and the third for removing it from the list of threats found.</p></body></html>", None))
        self.faq_faq_page_title.setText(QCoreApplication.translate("MainWindow", u"FAQ Page", None))
        self.faq_faq_page_btn.setText("")
        self.faq_faq_page_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The FAQ tab, in which you are actually now, provides various instructions and answers to your questions. In the process of updates, the FAQ library will expand rapidly.</p></body></html>", None))
        self.faq_settings_page_title.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.faq_settings_page_btn.setText("")
        self.faq_settings_page_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The Settings tab is responsible for flexibly changing various program parameters to improve its performance.</p></body></html>", None))
        self.faq_authors_title.setText(QCoreApplication.translate("MainWindow", u"Authors", None))
        self.faq_authors_btn.setText("")
        self.faq_authors_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Developer - DIMFLIX</p><p>UX/UI Designer and Developer - DIMFLIX </p><p>Logo and Company name- PlayStack </p></body></html>", None))
        self.faq_logo.setText("")
        self.settings_lang_title.setText(QCoreApplication.translate("MainWindow", u"Language: English", None))
        self.settings_lang_btn.setText("")
        self.settings_lang_rus_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0420\u0443\u0441\u0441\u043a\u0438\u0439</p></body></html>", None))
        self.settings_lang_rus_icon.setText("")
        self.settings_lang_eng_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>English</p></body></html>", None))
        self.settings_lang_eng_icon.setText("")
        self.settings_logo.setText("")
        self.virus_storage_main_title_label.setText(QCoreApplication.translate("MainWindow", u"VIRUS STORAGE", None))
        self.virus_storage_warning.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Warning - the antivirus is under development, which may cause inaccurate virus definitions.  A huge request to check the file yourself, in order to avoid deleting valuable information or system files</p></body></html>", None))
        ___qtablewidgetitem = self.virus_storage_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"time", None));
        ___qtablewidgetitem1 = self.virus_storage_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"threats", None));
        ___qtablewidgetitem2 = self.virus_storage_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"path", None));
        ___qtablewidgetitem3 = self.virus_storage_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"copy_btn", None));
        ___qtablewidgetitem4 = self.virus_storage_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"delete_btn", None));
        ___qtablewidgetitem5 = self.virus_storage_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"close_btn", None));
        self.home_title.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.home_description.setText(QCoreApplication.translate("MainWindow", u"PC performance monitoring", None))
        self.home_icon.setText("")
        self.scanning_title.setText(QCoreApplication.translate("MainWindow", u"Scanning", None))
        self.scanning_description.setText(QCoreApplication.translate("MainWindow", u"Scan your PC for viruses", None))
        self.scanning_icon.setText("")
        self.virus_storage_title.setText(QCoreApplication.translate("MainWindow", u"Virus storage", None))
        self.virus_storage_description.setText(QCoreApplication.translate("MainWindow", u"Storage of found viruses", None))
        self.virus_storage_icon.setText("")
        self.faq_description.setText(QCoreApplication.translate("MainWindow", u"Frequently asked questions", None))
        self.faq_title.setText(QCoreApplication.translate("MainWindow", u"FAQ", None))
        self.faq_icon.setText("")
        self.settings_title.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.settings_description.setText(QCoreApplication.translate("MainWindow", u"Application Settings", None))
        self.settiongs_icon.setText("")
    # retranslateUi

