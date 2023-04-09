from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def setPixmap(self, image):
        super().setPixmap(image)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()


class Ui_add_student(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1081)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 700))
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "                background-color: rgb(246, 245, 244);\n"
                                 "                }\n"
                                 "            ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.horizontalFrame.setStyleSheet("QFrame{\n"
                                           "                                                background-color: rgb(217, 217, 217);\n"
                                           "                                                border-radius: 20px;\n"
                                           "                                                }\n"
                                           "                                            ")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalFrame_2 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalFrame_2.setMinimumSize(QtCore.QSize(195, 0))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_37 = QtWidgets.QLabel(self.verticalFrame_2)
        self.label_37.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_3.addWidget(self.label_37)
        self.label_34 = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_3.addWidget(self.label_34)
        self.spo_11th_grade = QtWidgets.QRadioButton(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spo_11th_grade.setFont(font)
        self.spo_11th_grade.setStyleSheet("")
        self.spo_11th_grade.setChecked(True)
        self.spo_11th_grade.setObjectName("spo_11th_grade")
        self.verticalLayout_3.addWidget(self.spo_11th_grade)
        self.spo_9th_grade = QtWidgets.QRadioButton(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spo_9th_grade.setFont(font)
        self.spo_9th_grade.setCheckable(True)
        self.spo_9th_grade.setChecked(False)
        self.spo_9th_grade.setObjectName("spo_9th_grade")
        self.verticalLayout_3.addWidget(self.spo_9th_grade)
        self.label_36 = QtWidgets.QLabel(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_3.addWidget(self.label_36)
        self.hei_11th_grade = QtWidgets.QRadioButton(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hei_11th_grade.setFont(font)
        self.hei_11th_grade.setObjectName("hei_11th_grade")
        self.verticalLayout_3.addWidget(self.hei_11th_grade)
        self.hei_spo = QtWidgets.QRadioButton(self.verticalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hei_spo.setFont(font)
        self.hei_spo.setObjectName("hei_spo")
        self.verticalLayout_3.addWidget(self.hei_spo)
        self.horizontalLayout.addWidget(self.verticalFrame_2, 0, QtCore.Qt.AlignTop)
        self.verticalFrame = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_and_close_button = QtWidgets.QPushButton(self.verticalFrame)
        self.open_and_close_button.setMinimumSize(QtCore.QSize(40, 40))
        self.open_and_close_button.setMaximumSize(QtCore.QSize(40, 40))
        self.open_and_close_button.setStyleSheet("QPushButton{\n"
                                                 "                                                                        background-color: rgb(255, 255, 255);\n"
                                                 "                                                                        border-radius: 15px;\n"
                                                 "                                                                        }\n"
                                                 "\n"
                                                 "                                                                        QPushButton:hover{\n"
                                                 "                                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                 "                                                                        }\n"
                                                 "\n"
                                                 "                                                                        QPushButton:pressed{\n"
                                                 "                                                                        background-color: rgb(87, 227, 137);\n"
                                                 "                                                                        }\n"
                                                 "                                                                    ")
        self.open_and_close_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_and_close_button.setIcon(icon)
        self.open_and_close_button.setIconSize(QtCore.QSize(18, 18))
        self.open_and_close_button.setObjectName("open_and_close_button")
        self.verticalLayout.addWidget(self.open_and_close_button, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.verticalFrame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.horizontalFrame)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.education_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.education_tab.setEnabled(True)
        self.education_tab.setMaximumSize(QtCore.QSize(16777215, 16777195))
        self.education_tab.setStyleSheet("QTabWidget{\n"
                                         "                                                background-color: rgb(190, 207, 191);\n"
                                         "                                                }\n"
                                         "                                                QTabWidget::tab-bar {\n"
                                         "                                                alternate-background-color: rgb(224, 27, 36);\n"
                                         "                                                }\n"
                                         "                                                QTabBar::tab {\n"
                                         "                                                background-color: qlineargradient(x1:0.5, y1:1, x2:0.5, y2:0, stop:0\n"
                                         "                                                rgb(253,250,250), stop:0.2 rgb(253,250,250), stop:1 rgb(255,249,234));\n"
                                         "\n"
                                         "                                                border-top-left-radius: 7px;\n"
                                         "                                                border-top-right-radius: 7px;\n"
                                         "\n"
                                         "                                                min-width: 17ex;\n"
                                         "                                                padding: 5px;\n"
                                         "                                                }\n"
                                         "\n"
                                         "                                                QTabBar::tab:selected {\n"
                                         "                                                background-color: rgb(143, 240, 164);\n"
                                         "                                                color: rgb(255, 255, 255);\n"
                                         "                                                }\n"
                                         "\n"
                                         "                                                QTabBar::tab:!selected {\n"
                                         "                                                margin-top: 5px;\n"
                                         "                                                background: qlineargradient(x1:0.5, y1:1, x2:0.5, y2:0, stop:0\n"
                                         "                                                rgb(253,250,250), stop:0.2 rgb(253,250,250), stop:1 rgb(250,244,229));\n"
                                         "                                                color: rgb(93, 109, 109)\n"
                                         "                                                }\n"
                                         "                                            ")
        self.education_tab.setElideMode(QtCore.Qt.ElideNone)
        self.education_tab.setDocumentMode(True)
        self.education_tab.setTabsClosable(False)
        self.education_tab.setMovable(True)
        self.education_tab.setTabBarAutoHide(False)
        self.education_tab.setObjectName("education_tab")
        self.personal_data = QtWidgets.QWidget()
        self.personal_data.setObjectName("personal_data")
        self.label_2 = QtWidgets.QLabel(self.personal_data)
        self.label_2.setGeometry(QtCore.QRect(30, 440, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.calendar_birthday = QtWidgets.QCalendarWidget(self.personal_data)
        self.calendar_birthday.setGeometry(QtCore.QRect(30, 550, 401, 241))
        self.calendar_birthday.setStyleSheet("QCalendarWidget QWidget {\n"
                                             "                                                        alternate-background-color: rgb(143, 240, 164);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_navigationbar {\n"
                                             "                                                        background-color: #fff;\n"
                                             "                                                        border: 2px solid rgb(255, 255, 255);\n"
                                             "                                                        border-bottom: 0px;\n"
                                             "                                                        border-top-left-radius: 15px;\n"
                                             "                                                        border-top-right-radius: 15px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_prevmonth,\n"
                                             "                                                        #qt_calendar_nextmonth {\n"
                                             "                                                        /* border delete */\n"
                                             "                                                        border: none;\n"
                                             "                                                        /* delete default icons */\n"
                                             "                                                        qproperty-icon: none;\n"
                                             "\n"
                                             "                                                        min-width: 13px;\n"
                                             "                                                        max-width: 13px;\n"
                                             "                                                        min-height: 13px;\n"
                                             "                                                        max-height: 13px;\n"
                                             "\n"
                                             "                                                        border-radius: 15px;\n"
                                             "                                                        /* set background transparent */\n"
                                             "                                                        background-color: transparent;\n"
                                             "                                                        padding: 5px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        /* style for pre month button\n"
                                             "                                                        ############################################ */\n"
                                             "\n"
                                             "                                                        #qt_calendar_prevmonth {\n"
                                             "                                                        /* set text for button */\n"
                                             "                                                        /*qproperty-text: \">\";*/\n"
                                             "                                                        margin-left:5px;\n"
                                             "                                                        image: url(images/arrow-left.png);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        /* style for next month button\n"
                                             "                                                        ########################################### */\n"
                                             "                                                        #qt_calendar_nextmonth {\n"
                                             "                                                        margin-right:5px;\n"
                                             "                                                        image: url(images/arrow-right.png);\n"
                                             "                                                        /* qproperty-text: \">\"; */\n"
                                             "                                                        }\n"
                                             "                                                        #qt_calendar_prevmonth:hover,\n"
                                             "                                                        #qt_calendar_nextmonth:hover {\n"
                                             "                                                        background-color: rgb(143, 240, 164);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_prevmonth:pressed,\n"
                                             "                                                        #qt_calendar_nextmonth:pressed {\n"
                                             "                                                        background-color: rgba(235, 235, 235, 100);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "\n"
                                             "                                                        /* Style for month and yeat buttons\n"
                                             "                                                        #################################### */\n"
                                             "\n"
                                             "                                                        #qt_calendar_yearbutton {\n"
                                             "                                                        color: #000;\n"
                                             "                                                        margin:5px;\n"
                                             "                                                        border-radius: 15px;\n"
                                             "                                                        font-size: 13px;\n"
                                             "                                                        padding:0px 10px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_monthbutton {\n"
                                             "                                                        width: 110px;\n"
                                             "                                                        color: #000;\n"
                                             "                                                        font-size: 13px;\n"
                                             "                                                        margin:5px 0px;\n"
                                             "                                                        border-radius: 15px;\n"
                                             "                                                        padding:0px 2px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_yearbutton:hover,\n"
                                             "                                                        #qt_calendar_monthbutton:hover {\n"
                                             "                                                        background-color: rgb(143, 240, 164);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_yearbutton:pressed,\n"
                                             "                                                        #qt_calendar_monthbutton:pressed {\n"
                                             "                                                        background-color: rgba(143, 240, 164, 100);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        /* Style for year input lineEdit\n"
                                             "                                                        ######################################*/\n"
                                             "\n"
                                             "                                                        #qt_calendar_yearedit {\n"
                                             "                                                        min-width: 53px;\n"
                                             "                                                        color: #000;\n"
                                             "                                                        background: transparent;\n"
                                             "                                                        font-size: 13px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        /* Style for year change buttons\n"
                                             "                                                        ######################################*/\n"
                                             "\n"
                                             "                                                        #qt_calendar_yearedit::up-button {\n"
                                             "                                                        image: url(images/arrow-up.png);\n"
                                             "                                                        subcontrol-position: right;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_yearedit::down-button {\n"
                                             "                                                        image: url(images/arrow-down.png);\n"
                                             "                                                        subcontrol-position: left;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_yearedit::down-button,\n"
                                             "                                                        #qt_calendar_yearedit::up-button {\n"
                                             "                                                        width:10px;\n"
                                             "                                                        padding: 0px 5px;\n"
                                             "                                                        border-radius:3px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_yearedit::down-button:hover,\n"
                                             "                                                        #qt_calendar_yearedit::up-button:hover {\n"
                                             "                                                        background-color: rgb(143, 240, 164);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        /* Style for month select menu\n"
                                             "                                                        ##################################### */\n"
                                             "\n"
                                             "                                                        #calendarWidget QToolButton QMenu {\n"
                                             "                                                        background-color: white;\n"
                                             "\n"
                                             "                                                        }\n"
                                             "                                                        #calendarWidget QToolButton QMenu::item {\n"
                                             "                                                        /*padding: 10px;*/\n"
                                             "                                                        }\n"
                                             "                                                        #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
                                             "                                                        background-color: rgb(143, 240, 164);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #calendarWidget QToolButton::menu-indicator {\n"
                                             "                                                        /* Remove toolButton arrow */\n"
                                             "                                                        /*image: none; */\n"
                                             "                                                        nosubcontrol-origin: margin;\n"
                                             "                                                        subcontrol-position: right center;\n"
                                             "                                                        margin-top: 10px;\n"
                                             "                                                        width:20px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        /* Style for calendar table\n"
                                             "                                                        ########################################## */\n"
                                             "                                                        #qt_calendar_calendarview {\n"
                                             "                                                        /* Remove the selected dashed box */\n"
                                             "                                                        outline: 0px;\n"
                                             "\n"
                                             "                                                        border: 2px solid rgb(143, 240, 164);\n"
                                             "                                                        border-top: 0px;\n"
                                             "                                                        border-bottom-left-radius: 10px;\n"
                                             "                                                        border-bottom-right-radius: 10px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_calendarview::item:hover {\n"
                                             "                                                        border-radius: 15px;\n"
                                             "                                                        background-color: rgb(143, 240, 164);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        #qt_calendar_calendarview::item:selected {\n"
                                             "                                                        background-color: rgb(143, 240, 164);\n"
                                             "                                                        border-radius: 15px;\n"
                                             "                                                        }\n"
                                             "                                                    ")
        self.calendar_birthday.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendar_birthday.setNavigationBarVisible(True)
        self.calendar_birthday.setObjectName("calendar_birthday")
        self.date_of_birth = QtWidgets.QDateEdit(self.personal_data)
        self.date_of_birth.setGeometry(QtCore.QRect(30, 470, 181, 42))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_of_birth.setFont(font)
        self.date_of_birth.setStyleSheet("")
        self.date_of_birth.setObjectName("date_of_birth")
        self.label_38 = QtWidgets.QLabel(self.personal_data)
        self.label_38.setGeometry(QtCore.QRect(270, 440, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_5 = QtWidgets.QLabel(self.personal_data)
        self.label_5.setGeometry(QtCore.QRect(30, 330, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.open_calendar_birthday = QtWidgets.QPushButton(self.personal_data)
        self.open_calendar_birthday.setGeometry(QtCore.QRect(220, 470, 41, 41))
        self.open_calendar_birthday.setStyleSheet("QPushButton{\n"
                                                  "                                                        background-color: rgb(255, 255, 255);\n"
                                                  "                                                        border-radius: 15px;\n"
                                                  "                                                        border: 1px solid #ced4da;\n"
                                                  "                                                        }\n"
                                                  "\n"
                                                  "                                                        QPushButton:hover{\n"
                                                  "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                  "                                                        }\n"
                                                  "\n"
                                                  "                                                        QPushButton:pressed{\n"
                                                  "                                                        background-color: rgb(87, 227, 137);\n"
                                                  "                                                        }\n"
                                                  "                                                    ")
        self.open_calendar_birthday.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_calendar_birthday.setIcon(icon1)
        self.open_calendar_birthday.setIconSize(QtCore.QSize(18, 18))
        self.open_calendar_birthday.setObjectName("open_calendar_birthday")
        self.fio = QtWidgets.QLineEdit(self.personal_data)
        self.fio.setGeometry(QtCore.QRect(30, 360, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fio.setFont(font)
        self.fio.setStyleSheet("border-radius: 15px;\n"
                               "                                                        background-color: rgb(255, 255, 255);\n"
                               "                                                        border: 1px solid #ced4da;\n"
                               "                                                        padding-left: 5px;\n"
                               "                                                    ")
        self.fio.setObjectName("fio")
        self.sex = QtWidgets.QComboBox(self.personal_data)
        self.sex.setGeometry(QtCore.QRect(270, 470, 136, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sex.setFont(font)
        self.sex.setStyleSheet("QComboBox {\n"
                               "                                                        border: 1px solid #ced4da;\n"
                               "                                                        border-radius: 15px;\n"
                               "                                                        padding-left: 10px;\n"
                               "                                                        background-color: rgb(255, 255, 255);\n"
                               "                                                        }\n"
                               "\n"
                               "                                                        QComboBox::drop-down {\n"
                               "                                                        border:0px;\n"
                               "                                                        }\n"
                               "\n"
                               "                                                        QComboBox::down-arrow {\n"
                               "                                                        image: url(images/arrow-down.png);\n"
                               "                                                        width: 24px;\n"
                               "                                                        height: 24px;\n"
                               "                                                        margin-right: 15px;\n"
                               "                                                        }\n"
                               "\n"
                               "                                                        QComboBox:on{\n"
                               "                                                        border: 2px solid rgb(87, 227, 137);\n"
                               "                                                        }\n"
                               "\n"
                               "                                                        QComboBox QListView {\n"
                               "                                                        border-radius: 15px;\n"
                               "                                                        font-size: 24px;\n"
                               "                                                        padding: 5px;\n"
                               "                                                        background-color: #fff;\n"
                               "                                                        outline: 0px;\n"
                               "\n"
                               "                                                        color: rgb(0, 0, 0);\n"
                               "                                                        }\n"
                               "\n"
                               "                                                        QComboBox QListView::item {\n"
                               "                                                        padding-left: 10px;\n"
                               "                                                        background-color: #00ff00;\n"
                               "                                                        }\n"
                               "\n"
                               "                                                        QComboBox QListView:item:hover {\n"
                               "                                                        background-color: rgb(87, 227, 137);\n"
                               "                                                        }\n"
                               "\n"
                               "                                                        QComboBox QListView:item:selected {\n"
                               "                                                        background-color: rgb(87, 227, 137);\n"
                               "                                                        }\n"
                               "                                                    ")
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.region = QtWidgets.QComboBox(self.personal_data)
        self.region.setEnabled(True)
        self.region.setGeometry(QtCore.QRect(480, 390, 251, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.region.setFont(font)
        self.region.setStyleSheet("QComboBox {\n"
                                  "                                                        border: 1px solid #ced4da;\n"
                                  "                                                        border-radius: 15px;\n"
                                  "                                                        padding-left: 10px;\n"
                                  "                                                        background-color: rgb(255, 255, 255);\n"
                                  "                                                        }\n"
                                  "\n"
                                  "                                                        QComboBox::drop-down {\n"
                                  "                                                        border:0px;\n"
                                  "                                                        }\n"
                                  "\n"
                                  "                                                        QComboBox::down-arrow {\n"
                                  "                                                        image: url(images/arrow-down.png);\n"
                                  "                                                        width: 24px;\n"
                                  "                                                        height: 24px;\n"
                                  "                                                        margin-right: 15px;\n"
                                  "                                                        }\n"
                                  "\n"
                                  "                                                        QComboBox:on{\n"
                                  "                                                        border: 2px solid rgb(87, 227, 137);\n"
                                  "                                                        }\n"
                                  "\n"
                                  "                                                        QComboBox QListView {\n"
                                  "                                                        border-radius: 15px;\n"
                                  "                                                        font-size: 24px;\n"
                                  "                                                        padding: 5px;\n"
                                  "                                                        background-color: #fff;\n"
                                  "                                                        outline: 0px;\n"
                                  "\n"
                                  "                                                        color: rgb(0, 0, 0);\n"
                                  "                                                        }\n"
                                  "\n"
                                  "                                                        QComboBox QListView::item {\n"
                                  "                                                        padding-left: 10px;\n"
                                  "                                                        background-color: #00ff00;\n"
                                  "                                                        }\n"
                                  "\n"
                                  "                                                        QComboBox QListView:item:hover {\n"
                                  "                                                        background-color: rgb(87, 227, 137);\n"
                                  "                                                        }\n"
                                  "\n"
                                  "                                                        QComboBox QListView:item:selected {\n"
                                  "                                                        background-color: rgb(87, 227, 137);\n"
                                  "                                                        }\n"
                                  "                                                    ")
        self.region.setEditable(False)
        self.region.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.region.setObjectName("region")
        self.address_error = QtWidgets.QLabel(self.personal_data)
        self.address_error.setGeometry(QtCore.QRect(480, 520, 471, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.address_error.setFont(font)
        self.address_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.address_error.setText("")
        self.address_error.setObjectName("address_error")
        self.label_10 = QtWidgets.QLabel(self.personal_data)
        self.label_10.setGeometry(QtCore.QRect(480, 440, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.personal_data)
        self.label_7.setGeometry(QtCore.QRect(480, 330, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.address = QtWidgets.QLineEdit(self.personal_data)
        self.address.setGeometry(QtCore.QRect(480, 470, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.address.setFont(font)
        self.address.setStyleSheet("border-radius: 15px;\n"
                                   "                                                        background-color: rgb(255, 255, 255);\n"
                                   "                                                        border: 1px solid #ced4da;\n"
                                   "                                                        padding-left: 5px;\n"
                                   "                                                    ")
        self.address.setObjectName("address")
        self.label_8 = QtWidgets.QLabel(self.personal_data)
        self.label_8.setGeometry(QtCore.QRect(480, 360, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.city = QtWidgets.QComboBox(self.personal_data)
        self.city.setGeometry(QtCore.QRect(740, 390, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.city.setFont(font)
        self.city.setStyleSheet("QComboBox {\n"
                                "                                                        border: 1px solid #ced4da;\n"
                                "                                                        border-radius: 15px;\n"
                                "                                                        padding-left: 10px;\n"
                                "                                                        background-color: rgb(255, 255, 255);\n"
                                "                                                        }\n"
                                "\n"
                                "                                                        QComboBox::drop-down {\n"
                                "                                                        border:0px;\n"
                                "                                                        }\n"
                                "\n"
                                "                                                        QComboBox::down-arrow {\n"
                                "                                                        image: url(images/arrow-down.png);\n"
                                "                                                        width: 24px;\n"
                                "                                                        height: 24px;\n"
                                "                                                        margin-right: 15px;\n"
                                "                                                        }\n"
                                "\n"
                                "                                                        QComboBox:on{\n"
                                "                                                        border: 2px solid rgb(87, 227, 137);\n"
                                "                                                        }\n"
                                "\n"
                                "                                                        QComboBox QListView {\n"
                                "                                                        border-radius: 15px;\n"
                                "                                                        font-size: 24px;\n"
                                "                                                        padding: 5px;\n"
                                "                                                        background-color: #fff;\n"
                                "                                                        outline: 0px;\n"
                                "\n"
                                "                                                        color: rgb(0, 0, 0);\n"
                                "                                                        }\n"
                                "\n"
                                "                                                        QComboBox QListView::item {\n"
                                "                                                        padding-left: 10px;\n"
                                "                                                        background-color: #00ff00;\n"
                                "                                                        }\n"
                                "\n"
                                "                                                        QComboBox QListView:item:hover {\n"
                                "                                                        background-color: rgb(87, 227, 137);\n"
                                "                                                        }\n"
                                "\n"
                                "                                                        QComboBox QListView:item:selected {\n"
                                "                                                        background-color: rgb(87, 227, 137);\n"
                                "                                                        }\n"
                                "                                                    ")
        self.city.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.city.setObjectName("city")
        self.label_9 = QtWidgets.QLabel(self.personal_data)
        self.label_9.setGeometry(QtCore.QRect(740, 360, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_60 = QtWidgets.QLabel(self.personal_data)
        self.label_60.setGeometry(QtCore.QRect(480, 550, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.applicants_number = QtWidgets.QLineEdit(self.personal_data)
        self.applicants_number.setGeometry(QtCore.QRect(570, 580, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.applicants_number.setFont(font)
        self.applicants_number.setStyleSheet("border-radius: 15px;\n"
                                             "                                                        background-color: rgb(255, 255, 255);\n"
                                             "                                                        border: 1px solid #ced4da;\n"
                                             "                                                        padding-left: 5px;\n"
                                             "                                                    ")
        self.applicants_number.setReadOnly(False)
        self.applicants_number.setObjectName("applicants_number")
        self.label_61 = QtWidgets.QLabel(self.personal_data)
        self.label_61.setGeometry(QtCore.QRect(990, 440, 621, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.parents1_number = QtWidgets.QLineEdit(self.personal_data)
        self.parents1_number.setGeometry(QtCore.QRect(1080, 470, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parents1_number.setFont(font)
        self.parents1_number.setStyleSheet("border-radius: 15px;\n"
                                           "                                                        background-color: rgb(255, 255, 255);\n"
                                           "                                                        border: 1px solid #ced4da;\n"
                                           "                                                    ")
        self.parents1_number.setObjectName("parents1_number")
        self.label_62 = QtWidgets.QLabel(self.personal_data)
        self.label_62.setGeometry(QtCore.QRect(250, 280, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.personal_data)
        self.label_63.setGeometry(QtCore.QRect(1130, 280, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.parents1_fio = QtWidgets.QLineEdit(self.personal_data)
        self.parents1_fio.setGeometry(QtCore.QRect(990, 360, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parents1_fio.setFont(font)
        self.parents1_fio.setStyleSheet("border-radius: 15px;\n"
                                        "                                                        background-color: rgb(255, 255, 255);\n"
                                        "                                                        border: 1px solid #ced4da;\n"
                                        "                                                    ")
        self.parents1_fio.setObjectName("parents1_fio")
        self.label_64 = QtWidgets.QLabel(self.personal_data)
        self.label_64.setGeometry(QtCore.QRect(990, 330, 441, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.personal_data)
        self.label_65.setGeometry(QtCore.QRect(990, 550, 631, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.parents2_fio = QtWidgets.QLineEdit(self.personal_data)
        self.parents2_fio.setGeometry(QtCore.QRect(990, 580, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parents2_fio.setFont(font)
        self.parents2_fio.setStyleSheet("border-radius: 15px;\n"
                                        "                                                        background-color: rgb(255, 255, 255);\n"
                                        "                                                        border: 1px solid #ced4da;\n"
                                        "                                                    ")
        self.parents2_fio.setObjectName("parents2_fio")
        self.fio_parent1_error = QtWidgets.QLabel(self.personal_data)
        self.fio_parent1_error.setGeometry(QtCore.QRect(990, 410, 631, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.fio_parent1_error.setFont(font)
        self.fio_parent1_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.fio_parent1_error.setText("")
        self.fio_parent1_error.setObjectName("fio_parent1_error")
        self.fio_parent2_error = QtWidgets.QLabel(self.personal_data)
        self.fio_parent2_error.setGeometry(QtCore.QRect(990, 630, 641, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.fio_parent2_error.setFont(font)
        self.fio_parent2_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.fio_parent2_error.setText("")
        self.fio_parent2_error.setObjectName("fio_parent2_error")
        self.applicants_number_error = QtWidgets.QLabel(self.personal_data)
        self.applicants_number_error.setGeometry(QtCore.QRect(480, 630, 481, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.applicants_number_error.setFont(font)
        self.applicants_number_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.applicants_number_error.setText("")
        self.applicants_number_error.setObjectName("applicants_number_error")
        self.label_66 = QtWidgets.QLabel(self.personal_data)
        self.label_66.setGeometry(QtCore.QRect(990, 660, 641, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.parents2_number = QtWidgets.QLineEdit(self.personal_data)
        self.parents2_number.setGeometry(QtCore.QRect(1080, 690, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parents2_number.setFont(font)
        self.parents2_number.setStyleSheet("border-radius: 15px;\n"
                                           "                                                        background-color: rgb(255, 255, 255);\n"
                                           "                                                        border: 1px solid #ced4da;\n"
                                           "                                                    ")
        self.parents2_number.setObjectName("parents2_number")
        self.parent1_number_error = QtWidgets.QLabel(self.personal_data)
        self.parent1_number_error.setGeometry(QtCore.QRect(990, 520, 641, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.parent1_number_error.setFont(font)
        self.parent1_number_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.parent1_number_error.setText("")
        self.parent1_number_error.setObjectName("parent1_number_error")
        self.parent2_number_error = QtWidgets.QLabel(self.personal_data)
        self.parent2_number_error.setGeometry(QtCore.QRect(990, 740, 641, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.parent2_number_error.setFont(font)
        self.parent2_number_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.parent2_number_error.setText("")
        self.parent2_number_error.setObjectName("parent2_number_error")
        self.fio_error = QtWidgets.QLabel(self.personal_data)
        self.fio_error.setGeometry(QtCore.QRect(30, 410, 431, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.fio_error.setFont(font)
        self.fio_error.setText("")
        self.fio_error.setObjectName("fio_error")
        self.age_student_error = QtWidgets.QLabel(self.personal_data)
        self.age_student_error.setGeometry(QtCore.QRect(30, 520, 421, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.age_student_error.setFont(font)
        self.age_student_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.age_student_error.setText("")
        self.age_student_error.setObjectName("age_student_error")
        self.passport_image_2 = QtWidgets.QLabel(self.personal_data)
        self.passport_image_2.setEnabled(True)
        self.passport_image_2.setGeometry(QtCore.QRect(720, 40, 161, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passport_image_2.setFont(font)
        self.passport_image_2.setAcceptDrops(True)
        self.passport_image_2.setStyleSheet("QLabel {\n"
                                            "                                                        border: 4px dashed #aaa;\n"
                                            "                                                        border-radius: 75px;\n"
                                            "                                                        }\n"
                                            "                                                    ")
        self.passport_image_2.setText("")
        self.passport_image_2.setPixmap(QtGui.QPixmap("images/camera-fill(1).png"))
        self.passport_image_2.setScaledContents(False)
        self.passport_image_2.setAlignment(QtCore.Qt.AlignCenter)
        self.passport_image_2.setObjectName("passport_image_2")
        self.delete_image3x4 = QtWidgets.QPushButton(self.personal_data)
        self.delete_image3x4.setGeometry(QtCore.QRect(700, 170, 40, 40))
        self.delete_image3x4.setStyleSheet("QPushButton{\n"
                                           "                                                        background-color: rgb(255, 255, 255);\n"
                                           "                                                        border-radius: 15px;\n"
                                           "                                                        }\n"
                                           "\n"
                                           "                                                        QPushButton:hover{\n"
                                           "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                           "                                                        }\n"
                                           "\n"
                                           "                                                        QPushButton:pressed{\n"
                                           "                                                        background-color: rgb(87, 227, 137);\n"
                                           "                                                        }\n"
                                           "                                                    ")
        self.delete_image3x4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_image3x4.setIcon(icon2)
        self.delete_image3x4.setObjectName("delete_image3x4")
        self.open_explorer_passport_2 = QtWidgets.QPushButton(self.personal_data)
        self.open_explorer_passport_2.setGeometry(QtCore.QRect(860, 170, 40, 40))
        self.open_explorer_passport_2.setMinimumSize(QtCore.QSize(40, 40))
        self.open_explorer_passport_2.setStyleSheet("QPushButton{\n"
                                                    "                                                        background-color: rgb(255, 255, 255);\n"
                                                    "                                                        border-radius: 15px;\n"
                                                    "                                                        }\n"
                                                    "\n"
                                                    "                                                        QPushButton:hover{\n"
                                                    "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                    "                                                        }\n"
                                                    "\n"
                                                    "                                                        QPushButton:pressed{\n"
                                                    "                                                        background-color: rgb(87, 227, 137);\n"
                                                    "                                                        }\n"
                                                    "                                                    ")
        self.open_explorer_passport_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/search.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_explorer_passport_2.setIcon(icon3)
        self.open_explorer_passport_2.setIconSize(QtCore.QSize(20, 20))
        self.open_explorer_passport_2.setObjectName("open_explorer_passport_2")
        self.code_of_applicants_number = QtWidgets.QComboBox(self.personal_data)
        self.code_of_applicants_number.setGeometry(QtCore.QRect(480, 580, 81, 41))
        self.code_of_applicants_number.setStyleSheet("QComboBox {\n"
                                                     "                                                        border: 1px solid #ced4da;\n"
                                                     "                                                        border-radius: 15px;\n"
                                                     "                                                        padding-left: 10px;\n"
                                                     "                                                        background-color: rgb(255, 255, 255);\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QComboBox::drop-down {\n"
                                                     "                                                        border:0px;\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QComboBox::down-arrow {\n"
                                                     "                                                        image: url(images/arrow-down.png);\n"
                                                     "                                                        width: 24px;\n"
                                                     "                                                        height: 24px;\n"
                                                     "                                                        margin-right: 15px;\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QComboBox:on{\n"
                                                     "                                                        border: 2px solid rgb(87, 227, 137);\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QComboBox QListView {\n"
                                                     "                                                        border-radius: 15px;\n"
                                                     "                                                        font-size: 24px;\n"
                                                     "                                                        padding: 5px;\n"
                                                     "                                                        background-color: #fff;\n"
                                                     "                                                        outline: 0px;\n"
                                                     "\n"
                                                     "                                                        color: rgb(0, 0, 0);\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QComboBox QListView::item {\n"
                                                     "                                                        padding-left: 10px;\n"
                                                     "                                                        background-color: #00ff00;\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QComboBox QListView:item:hover {\n"
                                                     "                                                        background-color: rgb(87, 227, 137);\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QComboBox QListView:item:selected {\n"
                                                     "                                                        background-color: rgb(87, 227, 137);\n"
                                                     "                                                        }\n"
                                                     "                                                    ")
        self.code_of_applicants_number.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.code_of_applicants_number.setObjectName("code_of_applicants_number")
        self.code_of_parents1_number = QtWidgets.QComboBox(self.personal_data)
        self.code_of_parents1_number.setGeometry(QtCore.QRect(990, 470, 81, 41))
        self.code_of_parents1_number.setStyleSheet("QComboBox {\n"
                                                   "                                                        border: 1px solid #ced4da;\n"
                                                   "                                                        border-radius: 15px;\n"
                                                   "                                                        padding-left: 10px;\n"
                                                   "                                                        background-color: rgb(255, 255, 255);\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox::drop-down {\n"
                                                   "                                                        border:0px;\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox::down-arrow {\n"
                                                   "                                                        image: url(images/arrow-down.png);\n"
                                                   "                                                        width: 24px;\n"
                                                   "                                                        height: 24px;\n"
                                                   "                                                        margin-right: 15px;\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox:on{\n"
                                                   "                                                        border: 2px solid rgb(87, 227, 137);\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox QListView {\n"
                                                   "                                                        border-radius: 15px;\n"
                                                   "                                                        font-size: 24px;\n"
                                                   "                                                        padding: 5px;\n"
                                                   "                                                        background-color: #fff;\n"
                                                   "                                                        outline: 0px;\n"
                                                   "\n"
                                                   "                                                        color: rgb(0, 0, 0);\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox QListView::item {\n"
                                                   "                                                        padding-left: 10px;\n"
                                                   "                                                        background-color: #00ff00;\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox QListView:item:hover {\n"
                                                   "                                                        background-color: rgb(87, 227, 137);\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox QListView:item:selected {\n"
                                                   "                                                        background-color: rgb(87, 227, 137);\n"
                                                   "                                                        }\n"
                                                   "                                                    ")
        self.code_of_parents1_number.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.code_of_parents1_number.setObjectName("code_of_parents1_number")
        self.code_of_parents2_number = QtWidgets.QComboBox(self.personal_data)
        self.code_of_parents2_number.setGeometry(QtCore.QRect(990, 690, 81, 41))
        self.code_of_parents2_number.setStyleSheet("QComboBox {\n"
                                                   "                                                        border: 1px solid #ced4da;\n"
                                                   "                                                        border-radius: 15px;\n"
                                                   "                                                        padding-left: 10px;\n"
                                                   "                                                        background-color: rgb(255, 255, 255);\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox::drop-down {\n"
                                                   "                                                        border:0px;\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox::down-arrow {\n"
                                                   "                                                        image: url(images/arrow-down.png);\n"
                                                   "                                                        width: 24px;\n"
                                                   "                                                        height: 24px;\n"
                                                   "                                                        margin-right: 15px;\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox:on{\n"
                                                   "                                                        border: 2px solid rgb(87, 227, 137);\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox QListView {\n"
                                                   "                                                        border-radius: 15px;\n"
                                                   "                                                        font-size: 24px;\n"
                                                   "                                                        padding: 5px;\n"
                                                   "                                                        background-color: #fff;\n"
                                                   "                                                        outline: 0px;\n"
                                                   "\n"
                                                   "                                                        color: rgb(0, 0, 0);\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox QListView::item {\n"
                                                   "                                                        padding-left: 10px;\n"
                                                   "                                                        background-color: #00ff00;\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox QListView:item:hover {\n"
                                                   "                                                        background-color: rgb(87, 227, 137);\n"
                                                   "                                                        }\n"
                                                   "\n"
                                                   "                                                        QComboBox QListView:item:selected {\n"
                                                   "                                                        background-color: rgb(87, 227, 137);\n"
                                                   "                                                        }\n"
                                                   "                                                    ")
        self.code_of_parents2_number.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.code_of_parents2_number.setObjectName("code_of_parents2_number")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.education_tab.addTab(self.personal_data, icon4, "")
        self.documents_tab = QtWidgets.QWidget()
        self.documents_tab.setObjectName("documents_tab")
        self.label_13 = QtWidgets.QLabel(self.documents_tab)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 441, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.series_and_number_passport = QtWidgets.QLineEdit(self.documents_tab)
        self.series_and_number_passport.setGeometry(QtCore.QRect(10, 70, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.series_and_number_passport.setFont(font)
        self.series_and_number_passport.setStyleSheet("border-radius: 15px;\n"
                                                      "padding-left: 5px;\n"
                                                      "                                                    ")
        self.series_and_number_passport.setInputMask("")
        self.series_and_number_passport.setObjectName("series_and_number_passport")
        self.label_17 = QtWidgets.QLabel(self.documents_tab)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.passport_error = QtWidgets.QLabel(self.documents_tab)
        self.passport_error.setGeometry(QtCore.QRect(10, 120, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.passport_error.setFont(font)
        self.passport_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.passport_error.setText("")
        self.passport_error.setObjectName("passport_error")
        self.label_14 = QtWidgets.QLabel(self.documents_tab)
        self.label_14.setGeometry(QtCore.QRect(10, 320, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.issued_by_whom = QtWidgets.QLineEdit(self.documents_tab)
        self.issued_by_whom.setGeometry(QtCore.QRect(10, 350, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.issued_by_whom.setFont(font)
        self.issued_by_whom.setStyleSheet("border-radius: 15px;\n"
                                          "                                                        padding-left: 5px;\n"
                                          "                                                    ")
        self.issued_by_whom.setObjectName("issued_by_whom")
        self.label_15 = QtWidgets.QLabel(self.documents_tab)
        self.label_15.setGeometry(QtCore.QRect(10, 430, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.open_calendar_issue = QtWidgets.QPushButton(self.documents_tab)
        self.open_calendar_issue.setGeometry(QtCore.QRect(200, 460, 41, 39))
        self.open_calendar_issue.setStyleSheet("QPushButton{\n"
                                               "                                                        background-color: rgb(255, 255, 255);\n"
                                               "                                                        border-radius: 15px;\n"
                                               "                                                        }\n"
                                               "\n"
                                               "                                                        QPushButton:hover{\n"
                                               "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                               "                                                        }\n"
                                               "\n"
                                               "                                                        QPushButton:pressed{\n"
                                               "                                                        background-color: rgb(87, 227, 137);\n"
                                               "                                                        }\n"
                                               "                                                    ")
        self.open_calendar_issue.setText("")
        self.open_calendar_issue.setIcon(icon1)
        self.open_calendar_issue.setIconSize(QtCore.QSize(18, 18))
        self.open_calendar_issue.setObjectName("open_calendar_issue")
        self.date_of_issue = QtWidgets.QDateEdit(self.documents_tab)
        self.date_of_issue.setGeometry(QtCore.QRect(10, 460, 181, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_of_issue.setFont(font)
        self.date_of_issue.setStyleSheet("")
        self.date_of_issue.setObjectName("date_of_issue")
        self.snils_error = QtWidgets.QLabel(self.documents_tab)
        self.snils_error.setGeometry(QtCore.QRect(490, 90, 481, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.snils_error.setFont(font)
        self.snils_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.snils_error.setText("")
        self.snils_error.setObjectName("snils_error")
        self.snils = QtWidgets.QLineEdit(self.documents_tab)
        self.snils.setGeometry(QtCore.QRect(490, 40, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.snils.setFont(font)
        self.snils.setStyleSheet("border-radius: 15px;\n"
                                 "                                                        padding-left: 5px;\n"
                                 "                                                    ")
        self.snils.setObjectName("snils")
        self.label_16 = QtWidgets.QLabel(self.documents_tab)
        self.label_16.setGeometry(QtCore.QRect(490, 10, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_11 = QtWidgets.QLabel(self.documents_tab)
        self.label_11.setGeometry(QtCore.QRect(990, 600, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.certificate_number = QtWidgets.QLineEdit(self.documents_tab)
        self.certificate_number.setGeometry(QtCore.QRect(990, 630, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.certificate_number.setFont(font)
        self.certificate_number.setStyleSheet("border-radius: 15px;\n"
                                              "                                                        padding-left: 5px;\n"
                                              "                                                    ")
        self.certificate_number.setObjectName("certificate_number")
        self.label_18 = QtWidgets.QLabel(self.documents_tab)
        self.label_18.setGeometry(QtCore.QRect(10, 790, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.division_code = QtWidgets.QLineEdit(self.documents_tab)
        self.division_code.setGeometry(QtCore.QRect(10, 820, 351, 39))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.division_code.setFont(font)
        self.division_code.setStyleSheet("border-radius: 15px;\n"
                                         "                                                        padding-left: 5px;\n"
                                         "                                                    ")
        self.division_code.setObjectName("division_code")
        self.calendar_issue = QtWidgets.QCalendarWidget(self.documents_tab)
        self.calendar_issue.setGeometry(QtCore.QRect(10, 510, 401, 239))
        self.calendar_issue.setStyleSheet("QCalendarWidget QWidget {\n"
                                          "                                                        alternate-background-color: rgb(143, 240, 164);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_navigationbar {\n"
                                          "                                                        background-color: #fff;\n"
                                          "                                                        border: 2px solid rgb(255, 255, 255);\n"
                                          "                                                        border-bottom: 0px;\n"
                                          "                                                        border-top-left-radius: 10px;\n"
                                          "                                                        border-top-right-radius: 10px;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_prevmonth,\n"
                                          "                                                        #qt_calendar_nextmonth {\n"
                                          "                                                        /* border delete */\n"
                                          "                                                        border: none;\n"
                                          "                                                        /* delete default icons */\n"
                                          "                                                        qproperty-icon: none;\n"
                                          "\n"
                                          "                                                        min-width: 13px;\n"
                                          "                                                        max-width: 13px;\n"
                                          "                                                        min-height: 13px;\n"
                                          "                                                        max-height: 13px;\n"
                                          "\n"
                                          "                                                        border-radius: 10px;\n"
                                          "                                                        /* set background transparent */\n"
                                          "                                                        background-color: transparent;\n"
                                          "                                                        padding: 5px;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        /* style for pre month button\n"
                                          "                                                        ############################################ */\n"
                                          "\n"
                                          "                                                        #qt_calendar_prevmonth {\n"
                                          "                                                        /* set text for button */\n"
                                          "                                                        /*qproperty-text: \">\";*/\n"
                                          "                                                        margin-left:5px;\n"
                                          "                                                        image: url(images/arrow-left.png);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        /* style for next month button\n"
                                          "                                                        ########################################### */\n"
                                          "                                                        #qt_calendar_nextmonth {\n"
                                          "                                                        margin-right:5px;\n"
                                          "                                                        image: url(images/arrow-right.png);\n"
                                          "                                                        /* qproperty-text: \">\"; */\n"
                                          "                                                        }\n"
                                          "                                                        #qt_calendar_prevmonth:hover,\n"
                                          "                                                        #qt_calendar_nextmonth:hover {\n"
                                          "                                                        background-color: rgb(143, 240, 164);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_prevmonth:pressed,\n"
                                          "                                                        #qt_calendar_nextmonth:pressed {\n"
                                          "                                                        background-color: rgba(235, 235, 235, 100);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "\n"
                                          "                                                        /* Style for month and yeat buttons\n"
                                          "                                                        #################################### */\n"
                                          "\n"
                                          "                                                        #qt_calendar_yearbutton {\n"
                                          "                                                        color: #000;\n"
                                          "                                                        margin:5px;\n"
                                          "                                                        border-radius: 10px;\n"
                                          "                                                        font-size: 13px;\n"
                                          "                                                        padding:0px 10px;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_monthbutton {\n"
                                          "                                                        width: 110px;\n"
                                          "                                                        color: #000;\n"
                                          "                                                        font-size: 13px;\n"
                                          "                                                        margin:5px 0px;\n"
                                          "                                                        border-radius: 10px;\n"
                                          "                                                        padding:0px 2px;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_yearbutton:hover,\n"
                                          "                                                        #qt_calendar_monthbutton:hover {\n"
                                          "                                                        background-color: rgb(143, 240, 164);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_yearbutton:pressed,\n"
                                          "                                                        #qt_calendar_monthbutton:pressed {\n"
                                          "                                                        background-color: rgba(143, 240, 164, 100);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        /* Style for year input lineEdit\n"
                                          "                                                        ######################################*/\n"
                                          "\n"
                                          "                                                        #qt_calendar_yearedit {\n"
                                          "                                                        min-width: 53px;\n"
                                          "                                                        color: #000;\n"
                                          "                                                        background: transparent;\n"
                                          "                                                        font-size: 13px;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        /* Style for year change buttons\n"
                                          "                                                        ######################################*/\n"
                                          "\n"
                                          "                                                        #qt_calendar_yearedit::up-button {\n"
                                          "                                                        image: url(images/arrow-up.png);\n"
                                          "                                                        subcontrol-position: right;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_yearedit::down-button {\n"
                                          "                                                        image: url(images/arrow-down.png);\n"
                                          "                                                        subcontrol-position: left;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_yearedit::down-button,\n"
                                          "                                                        #qt_calendar_yearedit::up-button {\n"
                                          "                                                        width:10px;\n"
                                          "                                                        padding: 0px 5px;\n"
                                          "                                                        border-radius:3px;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_yearedit::down-button:hover,\n"
                                          "                                                        #qt_calendar_yearedit::up-button:hover {\n"
                                          "                                                        background-color: rgb(143, 240, 164);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        /* Style for month select menu\n"
                                          "                                                        ##################################### */\n"
                                          "\n"
                                          "                                                        #calendarWidget QToolButton QMenu {\n"
                                          "                                                        background-color: white;\n"
                                          "\n"
                                          "                                                        }\n"
                                          "                                                        #calendarWidget QToolButton QMenu::item {\n"
                                          "                                                        /*padding: 10px;*/\n"
                                          "                                                        }\n"
                                          "                                                        #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
                                          "                                                        background-color: rgb(143, 240, 164);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #calendarWidget QToolButton::menu-indicator {\n"
                                          "                                                        /* Remove toolButton arrow */\n"
                                          "                                                        /*image: none; */\n"
                                          "                                                        nosubcontrol-origin: margin;\n"
                                          "                                                        subcontrol-position: right center;\n"
                                          "                                                        margin-top: 10px;\n"
                                          "                                                        width:20px;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        /* Style for calendar table\n"
                                          "                                                        ########################################## */\n"
                                          "                                                        #qt_calendar_calendarview {\n"
                                          "                                                        /* Remove the selected dashed box */\n"
                                          "                                                        outline: 0px;\n"
                                          "\n"
                                          "                                                        border: 2px solid rgb(143, 240, 164);\n"
                                          "                                                        border-top: 0px;\n"
                                          "                                                        border-bottom-left-radius: 6px;\n"
                                          "                                                        border-bottom-right-radius: 6px;\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_calendarview::item:hover {\n"
                                          "                                                        border-radius: 15px;\n"
                                          "                                                        background-color: rgb(143, 240, 164);\n"
                                          "                                                        }\n"
                                          "\n"
                                          "                                                        #qt_calendar_calendarview::item:selected {\n"
                                          "                                                        background-color: rgb(143, 240, 164);\n"
                                          "                                                        border-radius: 15px;\n"
                                          "                                                        }\n"
                                          "                                                    ")
        self.calendar_issue.setObjectName("calendar_issue")
        self.label_58 = QtWidgets.QLabel(self.documents_tab)
        self.label_58.setGeometry(QtCore.QRect(490, 280, 221, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.oms_policy_number = QtWidgets.QLineEdit(self.documents_tab)
        self.oms_policy_number.setGeometry(QtCore.QRect(490, 310, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.oms_policy_number.setFont(font)
        self.oms_policy_number.setStyleSheet("border-radius: 15px;\n"
                                             "                                                        padding-left: 5px;\n"
                                             "                                                    ")
        self.oms_policy_number.setObjectName("oms_policy_number")
        self.label_59 = QtWidgets.QLabel(self.documents_tab)
        self.label_59.setGeometry(QtCore.QRect(490, 550, 261, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.birth_certificate_number = QtWidgets.QLineEdit(self.documents_tab)
        self.birth_certificate_number.setGeometry(QtCore.QRect(490, 580, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birth_certificate_number.setFont(font)
        self.birth_certificate_number.setStyleSheet("border-radius: 15px;\n"
                                                    "                                                        padding-left: 5px;\n"
                                                    "                                                    ")
        self.birth_certificate_number.setObjectName("birth_certificate_number")
        self.label_67 = QtWidgets.QLabel(self.documents_tab)
        self.label_67.setGeometry(QtCore.QRect(1130, 10, 381, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.about_applicant_textedit = QtWidgets.QPlainTextEdit(self.documents_tab)
        self.about_applicant_textedit.setGeometry(QtCore.QRect(990, 50, 641, 341))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.about_applicant_textedit.setFont(font)
        self.about_applicant_textedit.setStyleSheet("QPlainTextEdit{\n"
                                                    "                                                        background-color: rgb(255, 255, 255);\n"
                                                    "                                                        border-radius: 15px;\n"
                                                    "                                                        padding-left: 5px;\n"
                                                    "                                                        }\n"
                                                    "\n"
                                                    "                                                        QScrollBar::handle:vertical {\n"
                                                    "                                                        background-color: #BFBFBF;\n"
                                                    "                                                        border-radius: 3px;\n"
                                                    "\n"
                                                    "                                                        }\n"
                                                    "\n"
                                                    "                                                        QScrollBar::handle:vertical:hover {\n"
                                                    "                                                        background-color: #43464D;\n"
                                                    "                                                        }\n"
                                                    "\n"
                                                    "                                                        QScrollBar::handle:vertical:pressed {\n"
                                                    "                                                        background-color: rgb(51, 209, 122);\n"
                                                    "                                                        }\n"
                                                    "                                                    ")
        self.about_applicant_textedit.setObjectName("about_applicant_textedit")
        self.passport_image = QtWidgets.QLabel(self.documents_tab)
        self.passport_image.setGeometry(QtCore.QRect(10, 160, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.passport_image.setFont(font)
        self.passport_image.setMouseTracking(True)
        self.passport_image.setAcceptDrops(True)
        self.passport_image.setStyleSheet("QLabel {\n"
                                          "                                                        border: 4px dashed #aaa;\n"
                                          "                                                        border-radius: 15px;\n"
                                          "                                                        }\n"
                                          "                                                    ")
        self.passport_image.setScaledContents(True)
        self.passport_image.setAlignment(QtCore.Qt.AlignCenter)
        self.passport_image.setObjectName("passport_image")
        self.birth_certificate_image = QtWidgets.QLabel(self.documents_tab)
        self.birth_certificate_image.setGeometry(QtCore.QRect(490, 660, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.birth_certificate_image.setFont(font)
        self.birth_certificate_image.setMouseTracking(True)
        self.birth_certificate_image.setAcceptDrops(True)
        self.birth_certificate_image.setStyleSheet("QLabel {\n"
                                                   "                                                        border: 4px dashed #aaa;\n"
                                                   "                                                        border-radius: 15px;\n"
                                                   "                                                        }\n"
                                                   "                                                    ")
        self.birth_certificate_image.setScaledContents(True)
        self.birth_certificate_image.setAlignment(QtCore.Qt.AlignCenter)
        self.birth_certificate_image.setObjectName("birth_certificate_image")
        self.open_attachments_passport = QtWidgets.QPushButton(self.documents_tab)
        self.open_attachments_passport.setGeometry(QtCore.QRect(285, 70, 41, 41))
        self.open_attachments_passport.setStyleSheet("QPushButton{\n"
                                                     "                                                        background-color: rgb(255, 255, 255);\n"
                                                     "                                                        border-radius: 15px;\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QPushButton:hover{\n"
                                                     "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QPushButton:pressed{\n"
                                                     "                                                        background-color: rgb(87, 227, 137);\n"
                                                     "                                                        }\n"
                                                     "                                                    ")
        self.open_attachments_passport.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/attachments.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_attachments_passport.setIcon(icon5)
        self.open_attachments_passport.setIconSize(QtCore.QSize(18, 18))
        self.open_attachments_passport.setObjectName("open_attachments_passport")
        self.open_attachments_snils = QtWidgets.QPushButton(self.documents_tab)
        self.open_attachments_snils.setGeometry(QtCore.QRect(845, 40, 41, 41))
        self.open_attachments_snils.setStyleSheet("QPushButton{\n"
                                                  "                                                        background-color: rgb(255, 255, 255);\n"
                                                  "                                                        border-radius: 15px;\n"
                                                  "                                                        }\n"
                                                  "\n"
                                                  "                                                        QPushButton:hover{\n"
                                                  "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                  "                                                        }\n"
                                                  "\n"
                                                  "                                                        QPushButton:pressed{\n"
                                                  "                                                        background-color: rgb(87, 227, 137);\n"
                                                  "                                                        }\n"
                                                  "                                                    ")
        self.open_attachments_snils.setText("")
        self.open_attachments_snils.setIcon(icon5)
        self.open_attachments_snils.setIconSize(QtCore.QSize(18, 18))
        self.open_attachments_snils.setObjectName("open_attachments_snils")
        self.open_attachments_certificate_number = QtWidgets.QPushButton(self.documents_tab)
        self.open_attachments_certificate_number.setGeometry(QtCore.QRect(1345, 630, 41, 41))
        self.open_attachments_certificate_number.setStyleSheet("QPushButton{\n"
                                                               "                                                        background-color: rgb(255, 255, 255);\n"
                                                               "                                                        border-radius: 15px;\n"
                                                               "                                                        }\n"
                                                               "\n"
                                                               "                                                        QPushButton:hover{\n"
                                                               "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                               "                                                        }\n"
                                                               "\n"
                                                               "                                                        QPushButton:pressed{\n"
                                                               "                                                        background-color: rgb(87, 227, 137);\n"
                                                               "                                                        }\n"
                                                               "                                                    ")
        self.open_attachments_certificate_number.setText("")
        self.open_attachments_certificate_number.setIcon(icon5)
        self.open_attachments_certificate_number.setIconSize(QtCore.QSize(18, 18))
        self.open_attachments_certificate_number.setObjectName("open_attachments_certificate_number")
        self.open_attachments_oms = QtWidgets.QPushButton(self.documents_tab)
        self.open_attachments_oms.setGeometry(QtCore.QRect(845, 310, 41, 41))
        self.open_attachments_oms.setStyleSheet("QPushButton{\n"
                                                "                                                        background-color: rgb(255, 255, 255);\n"
                                                "                                                        border-radius: 15px;\n"
                                                "                                                        }\n"
                                                "\n"
                                                "                                                        QPushButton:hover{\n"
                                                "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                "                                                        }\n"
                                                "\n"
                                                "                                                        QPushButton:pressed{\n"
                                                "                                                        background-color: rgb(87, 227, 137);\n"
                                                "                                                        }\n"
                                                "                                                    ")
        self.open_attachments_oms.setText("")
        self.open_attachments_oms.setIcon(icon5)
        self.open_attachments_oms.setIconSize(QtCore.QSize(18, 18))
        self.open_attachments_oms.setObjectName("open_attachments_oms")
        self.open_attachments_birth_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.open_attachments_birth_certificate.setGeometry(QtCore.QRect(845, 580, 41, 41))
        self.open_attachments_birth_certificate.setStyleSheet("QPushButton{\n"
                                                              "                                                        background-color: rgb(255, 255, 255);\n"
                                                              "                                                        border-radius: 15px;\n"
                                                              "                                                        }\n"
                                                              "\n"
                                                              "                                                        QPushButton:hover{\n"
                                                              "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                              "                                                        }\n"
                                                              "\n"
                                                              "                                                        QPushButton:pressed{\n"
                                                              "                                                        background-color: rgb(87, 227, 137);\n"
                                                              "                                                        }\n"
                                                              "                                                    ")
        self.open_attachments_birth_certificate.setText("")
        self.open_attachments_birth_certificate.setIcon(icon5)
        self.open_attachments_birth_certificate.setIconSize(QtCore.QSize(18, 18))
        self.open_attachments_birth_certificate.setObjectName("open_attachments_birth_certificate")
        self.oms_image = QtWidgets.QLabel(self.documents_tab)
        self.oms_image.setGeometry(QtCore.QRect(490, 390, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.oms_image.setFont(font)
        self.oms_image.setMouseTracking(True)
        self.oms_image.setAcceptDrops(True)
        self.oms_image.setStyleSheet("QLabel {\n"
                                     "                                                        border: 4px dashed #aaa;\n"
                                     "                                                        border-radius: 15px;\n"
                                     "                                                        }\n"
                                     "                                                    ")
        self.oms_image.setScaledContents(True)
        self.oms_image.setAlignment(QtCore.Qt.AlignCenter)
        self.oms_image.setObjectName("oms_image")
        self.open_explorer_birth_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.open_explorer_birth_certificate.setGeometry(QtCore.QRect(890, 580, 40, 40))
        self.open_explorer_birth_certificate.setMinimumSize(QtCore.QSize(40, 40))
        self.open_explorer_birth_certificate.setStyleSheet("QPushButton{\n"
                                                           "                                                        background-color: rgb(255, 255, 255);\n"
                                                           "                                                        border-radius: 15px;\n"
                                                           "                                                        }\n"
                                                           "\n"
                                                           "                                                        QPushButton:hover{\n"
                                                           "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                           "                                                        }\n"
                                                           "\n"
                                                           "                                                        QPushButton:pressed{\n"
                                                           "                                                        background-color: rgb(87, 227, 137);\n"
                                                           "                                                        }\n"
                                                           "                                                    ")
        self.open_explorer_birth_certificate.setText("")
        self.open_explorer_birth_certificate.setIcon(icon3)
        self.open_explorer_birth_certificate.setIconSize(QtCore.QSize(20, 20))
        self.open_explorer_birth_certificate.setObjectName("open_explorer_birth_certificate")
        self.open_explorer_oms = QtWidgets.QPushButton(self.documents_tab)
        self.open_explorer_oms.setGeometry(QtCore.QRect(890, 310, 40, 40))
        self.open_explorer_oms.setMinimumSize(QtCore.QSize(40, 40))
        self.open_explorer_oms.setStyleSheet("QPushButton{\n"
                                             "                                                        background-color: rgb(255, 255, 255);\n"
                                             "                                                        border-radius: 15px;\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        QPushButton:hover{\n"
                                             "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                             "                                                        }\n"
                                             "\n"
                                             "                                                        QPushButton:pressed{\n"
                                             "                                                        background-color: rgb(87, 227, 137);\n"
                                             "                                                        }\n"
                                             "                                                    ")
        self.open_explorer_oms.setText("")
        self.open_explorer_oms.setIcon(icon3)
        self.open_explorer_oms.setIconSize(QtCore.QSize(20, 20))
        self.open_explorer_oms.setObjectName("open_explorer_oms")
        self.open_explorer_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.open_explorer_certificate.setGeometry(QtCore.QRect(1390, 630, 40, 40))
        self.open_explorer_certificate.setMinimumSize(QtCore.QSize(40, 40))
        self.open_explorer_certificate.setStyleSheet("QPushButton{\n"
                                                     "                                                        background-color: rgb(255, 255, 255);\n"
                                                     "                                                        border-radius: 15px;\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QPushButton:hover{\n"
                                                     "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                     "                                                        }\n"
                                                     "\n"
                                                     "                                                        QPushButton:pressed{\n"
                                                     "                                                        background-color: rgb(87, 227, 137);\n"
                                                     "                                                        }\n"
                                                     "                                                    ")
        self.open_explorer_certificate.setText("")
        self.open_explorer_certificate.setIcon(icon3)
        self.open_explorer_certificate.setIconSize(QtCore.QSize(20, 20))
        self.open_explorer_certificate.setObjectName("open_explorer_certificate")
        self.open_explorer_snils = QtWidgets.QPushButton(self.documents_tab)
        self.open_explorer_snils.setGeometry(QtCore.QRect(890, 40, 40, 40))
        self.open_explorer_snils.setMinimumSize(QtCore.QSize(40, 40))
        self.open_explorer_snils.setStyleSheet("QPushButton{\n"
                                               "                                                        background-color: rgb(255, 255, 255);\n"
                                               "                                                        border-radius: 15px;\n"
                                               "                                                        }\n"
                                               "\n"
                                               "                                                        QPushButton:hover{\n"
                                               "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                               "                                                        }\n"
                                               "\n"
                                               "                                                        QPushButton:pressed{\n"
                                               "                                                        background-color: rgb(87, 227, 137);\n"
                                               "                                                        }\n"
                                               "                                                    ")
        self.open_explorer_snils.setText("")
        self.open_explorer_snils.setIcon(icon3)
        self.open_explorer_snils.setIconSize(QtCore.QSize(20, 20))
        self.open_explorer_snils.setObjectName("open_explorer_snils")
        self.open_explorer_passport = QtWidgets.QPushButton(self.documents_tab)
        self.open_explorer_passport.setGeometry(QtCore.QRect(330, 70, 40, 40))
        self.open_explorer_passport.setMinimumSize(QtCore.QSize(40, 40))
        self.open_explorer_passport.setStyleSheet("QPushButton{\n"
                                                  "                                                        background-color: rgb(255, 255, 255);\n"
                                                  "                                                        border-radius: 15px;\n"
                                                  "                                                        }\n"
                                                  "\n"
                                                  "                                                        QPushButton:hover{\n"
                                                  "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                  "                                                        }\n"
                                                  "\n"
                                                  "                                                        QPushButton:pressed{\n"
                                                  "                                                        background-color: rgb(87, 227, 137);\n"
                                                  "                                                        }\n"
                                                  "                                                    ")
        self.open_explorer_passport.setText("")
        self.open_explorer_passport.setIcon(icon3)
        self.open_explorer_passport.setIconSize(QtCore.QSize(20, 20))
        self.open_explorer_passport.setObjectName("open_explorer_passport")
        self.certificate_image = QtWidgets.QLabel(self.documents_tab)
        self.certificate_image.setGeometry(QtCore.QRect(990, 710, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.certificate_image.setFont(font)
        self.certificate_image.setMouseTracking(True)
        self.certificate_image.setAcceptDrops(True)
        self.certificate_image.setStyleSheet("QLabel {\n"
                                             "                                                        border: 4px dashed #aaa;\n"
                                             "                                                        border-radius: 15px;\n"
                                             "                                                        }\n"
                                             "                                                    ")
        self.certificate_image.setScaledContents(True)
        self.certificate_image.setAlignment(QtCore.Qt.AlignCenter)
        self.certificate_image.setObjectName("certificate_image")
        self.snils_image = QtWidgets.QLabel(self.documents_tab)
        self.snils_image.setGeometry(QtCore.QRect(490, 120, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.snils_image.setFont(font)
        self.snils_image.setMouseTracking(True)
        self.snils_image.setAcceptDrops(True)
        self.snils_image.setStyleSheet("QLabel {\n"
                                       "                                                        border: 4px dashed #aaa;\n"
                                       "                                                        border-radius: 15px;\n"
                                       "                                                        }\n"
                                       "                                                    ")
        self.snils_image.setScaledContents(True)
        self.snils_image.setAlignment(QtCore.Qt.AlignCenter)
        self.snils_image.setObjectName("snils_image")
        self.label_20 = QtWidgets.QLabel(self.documents_tab)
        self.label_20.setGeometry(QtCore.QRect(990, 410, 651, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.achievements_image = QtWidgets.QLabel(self.documents_tab)
        self.achievements_image.setGeometry(QtCore.QRect(990, 440, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.achievements_image.setFont(font)
        self.achievements_image.setMouseTracking(True)
        self.achievements_image.setAcceptDrops(True)
        self.achievements_image.setStyleSheet("QLabel {\n"
                                              "                                                        border: 4px dashed #aaa;\n"
                                              "                                                        border-radius: 15px;\n"
                                              "                                                        }\n"
                                              "                                                    ")
        self.achievements_image.setScaledContents(True)
        self.achievements_image.setAlignment(QtCore.Qt.AlignCenter)
        self.achievements_image.setObjectName("achievements_image")
        self.oms_policy_number_error = QtWidgets.QLabel(self.documents_tab)
        self.oms_policy_number_error.setGeometry(QtCore.QRect(490, 360, 481, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.oms_policy_number_error.setFont(font)
        self.oms_policy_number_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.oms_policy_number_error.setText("")
        self.oms_policy_number_error.setObjectName("oms_policy_number_error")
        self.birth_certificate_number_error = QtWidgets.QLabel(self.documents_tab)
        self.birth_certificate_number_error.setGeometry(QtCore.QRect(490, 630, 481, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.birth_certificate_number_error.setFont(font)
        self.birth_certificate_number_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.birth_certificate_number_error.setText("")
        self.birth_certificate_number_error.setObjectName("birth_certificate_number_error")
        self.certificate_number_error = QtWidgets.QLabel(self.documents_tab)
        self.certificate_number_error.setGeometry(QtCore.QRect(990, 680, 641, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.certificate_number_error.setFont(font)
        self.certificate_number_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.certificate_number_error.setText("")
        self.certificate_number_error.setObjectName("certificate_number_error")
        self.date_of_issue_error = QtWidgets.QLabel(self.documents_tab)
        self.date_of_issue_error.setGeometry(QtCore.QRect(10, 760, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.date_of_issue_error.setFont(font)
        self.date_of_issue_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.date_of_issue_error.setText("")
        self.date_of_issue_error.setObjectName("date_of_issue_error")
        self.division_code_error = QtWidgets.QLabel(self.documents_tab)
        self.division_code_error.setGeometry(QtCore.QRect(10, 870, 461, 31))
        self.division_code_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.division_code_error.setText("")
        self.division_code_error.setObjectName("division_code_error")
        self.issue_error = QtWidgets.QLabel(self.documents_tab)
        self.issue_error.setGeometry(QtCore.QRect(10, 400, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.issue_error.setFont(font)
        self.issue_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.issue_error.setText("")
        self.issue_error.setObjectName("issue_error")
        self.left_button_passport = QtWidgets.QPushButton(self.documents_tab)
        self.left_button_passport.setGeometry(QtCore.QRect(20, 220, 40, 40))
        self.left_button_passport.setStyleSheet("QPushButton {\n"
                                                "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                "                                                        border-radius: 20px;\n"
                                                "                                                        height: 30px;\n"
                                                "                                                        transition: background 2.5s ease;\n"
                                                "                                                        }\n"
                                                "                                                        QPushButton:hover {\n"
                                                "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                "                                                        border-radius: 20px;\n"
                                                "\n"
                                                "                                                        }\n"
                                                "                                                    ")
        self.left_button_passport.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/less.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_button_passport.setIcon(icon6)
        self.left_button_passport.setObjectName("left_button_passport")
        self.right_button_passport = QtWidgets.QPushButton(self.documents_tab)
        self.right_button_passport.setGeometry(QtCore.QRect(260, 220, 40, 40))
        self.right_button_passport.setStyleSheet("QPushButton {\n"
                                                 "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                 "                                                        border-radius: 20px;\n"
                                                 "\n"
                                                 "                                                        }\n"
                                                 "                                                        QPushButton:hover {\n"
                                                 "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                 "                                                        border-radius: 20px;\n"
                                                 "                                                        transition: 2.5s;\n"
                                                 "                                                        }\n"
                                                 "                                                    ")
        self.right_button_passport.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/more.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_button_passport.setIcon(icon7)
        self.right_button_passport.setObjectName("right_button_passport")
        self.left_button_snils = QtWidgets.QPushButton(self.documents_tab)
        self.left_button_snils.setGeometry(QtCore.QRect(500, 175, 40, 40))
        self.left_button_snils.setStyleSheet("QPushButton {\n"
                                             "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                             "                                                        border-radius: 20px;\n"
                                             "                                                        height: 30px;\n"
                                             "                                                        transition: background 2.5s ease;\n"
                                             "                                                        }\n"
                                             "                                                        QPushButton:hover {\n"
                                             "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                             "                                                        border-radius: 20px;\n"
                                             "\n"
                                             "                                                        }\n"
                                             "                                                    ")
        self.left_button_snils.setText("")
        self.left_button_snils.setIcon(icon6)
        self.left_button_snils.setObjectName("left_button_snils")
        self.left_button_oms = QtWidgets.QPushButton(self.documents_tab)
        self.left_button_oms.setGeometry(QtCore.QRect(500, 450, 40, 40))
        self.left_button_oms.setStyleSheet("QPushButton {\n"
                                           "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                           "                                                        border-radius: 20px;\n"
                                           "                                                        height: 30px;\n"
                                           "                                                        transition: background 2.5s ease;\n"
                                           "                                                        }\n"
                                           "                                                        QPushButton:hover {\n"
                                           "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                           "                                                        border-radius: 20px;\n"
                                           "\n"
                                           "                                                        }\n"
                                           "                                                    ")
        self.left_button_oms.setText("")
        self.left_button_oms.setIcon(icon6)
        self.left_button_oms.setObjectName("left_button_oms")
        self.left_button_birth_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.left_button_birth_certificate.setGeometry(QtCore.QRect(500, 720, 40, 40))
        self.left_button_birth_certificate.setStyleSheet("QPushButton {\n"
                                                         "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                         "                                                        border-radius: 20px;\n"
                                                         "                                                        height: 30px;\n"
                                                         "                                                        transition: background 2.5s ease;\n"
                                                         "                                                        }\n"
                                                         "                                                        QPushButton:hover {\n"
                                                         "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                         "                                                        border-radius: 20px;\n"
                                                         "\n"
                                                         "                                                        }\n"
                                                         "                                                    ")
        self.left_button_birth_certificate.setText("")
        self.left_button_birth_certificate.setIcon(icon6)
        self.left_button_birth_certificate.setObjectName("left_button_birth_certificate")
        self.left_button_achievements = QtWidgets.QPushButton(self.documents_tab)
        self.left_button_achievements.setGeometry(QtCore.QRect(1000, 500, 40, 40))
        self.left_button_achievements.setStyleSheet("QPushButton {\n"
                                                    "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                    "                                                        border-radius: 20px;\n"
                                                    "                                                        height: 30px;\n"
                                                    "                                                        transition: background 2.5s ease;\n"
                                                    "                                                        }\n"
                                                    "                                                        QPushButton:hover {\n"
                                                    "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                    "                                                        border-radius: 20px;\n"
                                                    "\n"
                                                    "                                                        }\n"
                                                    "                                                    ")
        self.left_button_achievements.setText("")
        self.left_button_achievements.setIcon(icon6)
        self.left_button_achievements.setObjectName("left_button_achievements")
        self.left_button_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.left_button_certificate.setGeometry(QtCore.QRect(1000, 765, 40, 40))
        self.left_button_certificate.setStyleSheet("QPushButton {\n"
                                                   "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                   "                                                        border-radius: 20px;\n"
                                                   "                                                        height: 30px;\n"
                                                   "                                                        transition: background 2.5s ease;\n"
                                                   "                                                        }\n"
                                                   "                                                        QPushButton:hover {\n"
                                                   "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                   "                                                        border-radius: 20px;\n"
                                                   "\n"
                                                   "                                                        }\n"
                                                   "                                                    ")
        self.left_button_certificate.setText("")
        self.left_button_certificate.setIcon(icon6)
        self.left_button_certificate.setObjectName("left_button_certificate")
        self.right_button_snils = QtWidgets.QPushButton(self.documents_tab)
        self.right_button_snils.setGeometry(QtCore.QRect(740, 175, 40, 40))
        self.right_button_snils.setStyleSheet("QPushButton {\n"
                                              "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                              "                                                        border-radius: 20px;\n"
                                              "\n"
                                              "                                                        }\n"
                                              "                                                        QPushButton:hover {\n"
                                              "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                              "                                                        border-radius: 20px;\n"
                                              "                                                        transition: 2.5s;\n"
                                              "                                                        }\n"
                                              "                                                    ")
        self.right_button_snils.setText("")
        self.right_button_snils.setIcon(icon7)
        self.right_button_snils.setObjectName("right_button_snils")
        self.right_button_oms = QtWidgets.QPushButton(self.documents_tab)
        self.right_button_oms.setGeometry(QtCore.QRect(740, 450, 40, 40))
        self.right_button_oms.setStyleSheet("QPushButton {\n"
                                            "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                            "                                                        border-radius: 20px;\n"
                                            "\n"
                                            "                                                        }\n"
                                            "                                                        QPushButton:hover {\n"
                                            "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                            "                                                        border-radius: 20px;\n"
                                            "                                                        transition: 2.5s;\n"
                                            "                                                        }\n"
                                            "                                                    ")
        self.right_button_oms.setText("")
        self.right_button_oms.setIcon(icon7)
        self.right_button_oms.setObjectName("right_button_oms")
        self.right_button_birth_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.right_button_birth_certificate.setGeometry(QtCore.QRect(740, 720, 40, 40))
        self.right_button_birth_certificate.setStyleSheet("QPushButton {\n"
                                                          "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                          "                                                        border-radius: 20px;\n"
                                                          "\n"
                                                          "                                                        }\n"
                                                          "                                                        QPushButton:hover {\n"
                                                          "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                          "                                                        border-radius: 20px;\n"
                                                          "                                                        transition: 2.5s;\n"
                                                          "                                                        }\n"
                                                          "                                                    ")
        self.right_button_birth_certificate.setText("")
        self.right_button_birth_certificate.setIcon(icon7)
        self.right_button_birth_certificate.setObjectName("right_button_birth_certificate")
        self.right_button_achievements = QtWidgets.QPushButton(self.documents_tab)
        self.right_button_achievements.setGeometry(QtCore.QRect(1240, 500, 40, 40))
        self.right_button_achievements.setStyleSheet("QPushButton {\n"
                                                     "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                     "                                                        border-radius: 20px;\n"
                                                     "\n"
                                                     "                                                        }\n"
                                                     "                                                        QPushButton:hover {\n"
                                                     "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                     "                                                        border-radius: 20px;\n"
                                                     "                                                        transition: 2.5s;\n"
                                                     "                                                        }\n"
                                                     "                                                    ")
        self.right_button_achievements.setText("")
        self.right_button_achievements.setIcon(icon7)
        self.right_button_achievements.setObjectName("right_button_achievements")
        self.right_button_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.right_button_certificate.setGeometry(QtCore.QRect(1240, 765, 40, 40))
        self.right_button_certificate.setStyleSheet("QPushButton {\n"
                                                    "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                    "                                                        border-radius: 20px;\n"
                                                    "\n"
                                                    "                                                        }\n"
                                                    "                                                        QPushButton:hover {\n"
                                                    "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                    "                                                        border-radius: 20px;\n"
                                                    "                                                        transition: 2.5s;\n"
                                                    "                                                        }\n"
                                                    "                                                    ")
        self.right_button_certificate.setText("")
        self.right_button_certificate.setIcon(icon7)
        self.right_button_certificate.setObjectName("right_button_certificate")
        self.delete_image_achievements = QtWidgets.QPushButton(self.documents_tab)
        self.delete_image_achievements.setGeometry(QtCore.QRect(1250, 450, 31, 31))
        self.delete_image_achievements.setStyleSheet("QPushButton {\n"
                                                     "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                     "                                                        border-radius: 15px;\n"
                                                     "\n"
                                                     "                                                        }\n"
                                                     "                                                        QPushButton:hover {\n"
                                                     "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                     "                                                        border-radius: 15px;\n"
                                                     "                                                        transition: 2.5s;\n"
                                                     "                                                        }\n"
                                                     "                                                    ")
        self.delete_image_achievements.setText("")
        self.delete_image_achievements.setIcon(icon2)
        self.delete_image_achievements.setObjectName("delete_image_achievements")
        self.delete_image_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.delete_image_certificate.setGeometry(QtCore.QRect(1250, 710, 31, 29))
        self.delete_image_certificate.setStyleSheet("QPushButton {\n"
                                                    "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                    "                                                        border-radius: 15px;\n"
                                                    "\n"
                                                    "                                                        }\n"
                                                    "                                                        QPushButton:hover {\n"
                                                    "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                    "                                                        border-radius: 15px;\n"
                                                    "                                                        transition: 2.5s;\n"
                                                    "                                                        }\n"
                                                    "                                                    ")
        self.delete_image_certificate.setText("")
        self.delete_image_certificate.setIcon(icon2)
        self.delete_image_certificate.setObjectName("delete_image_certificate")
        self.delete_image_birth_certificate = QtWidgets.QPushButton(self.documents_tab)
        self.delete_image_birth_certificate.setGeometry(QtCore.QRect(750, 670, 31, 31))
        self.delete_image_birth_certificate.setStyleSheet("QPushButton {\n"
                                                          "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                          "                                                        border-radius: 15px;\n"
                                                          "\n"
                                                          "                                                        }\n"
                                                          "                                                        QPushButton:hover {\n"
                                                          "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                          "                                                        border-radius: 15px;\n"
                                                          "                                                        transition: 2.5s;\n"
                                                          "                                                        }\n"
                                                          "                                                    ")
        self.delete_image_birth_certificate.setText("")
        self.delete_image_birth_certificate.setIcon(icon2)
        self.delete_image_birth_certificate.setObjectName("delete_image_birth_certificate")
        self.delete_image_oms = QtWidgets.QPushButton(self.documents_tab)
        self.delete_image_oms.setGeometry(QtCore.QRect(750, 400, 31, 31))
        self.delete_image_oms.setStyleSheet("QPushButton {\n"
                                            "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                            "                                                        border-radius: 15px;\n"
                                            "\n"
                                            "                                                        }\n"
                                            "                                                        QPushButton:hover {\n"
                                            "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                            "                                                        border-radius: 15px;\n"
                                            "                                                        transition: 2.5s;\n"
                                            "                                                        }\n"
                                            "                                                    ")
        self.delete_image_oms.setText("")
        self.delete_image_oms.setIcon(icon2)
        self.delete_image_oms.setObjectName("delete_image_oms")
        self.delete_image_snils = QtWidgets.QPushButton(self.documents_tab)
        self.delete_image_snils.setGeometry(QtCore.QRect(750, 130, 31, 31))
        self.delete_image_snils.setStyleSheet("QPushButton {\n"
                                              "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                              "                                                        border-radius: 15px;\n"
                                              "\n"
                                              "                                                        }\n"
                                              "                                                        QPushButton:hover {\n"
                                              "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                              "                                                        border-radius: 15px;\n"
                                              "                                                        transition: 2.5s;\n"
                                              "                                                        }\n"
                                              "                                                    ")
        self.delete_image_snils.setText("")
        self.delete_image_snils.setIcon(icon2)
        self.delete_image_snils.setObjectName("delete_image_snils")
        self.delete_image_passport = QtWidgets.QPushButton(self.documents_tab)
        self.delete_image_passport.setGeometry(QtCore.QRect(270, 170, 31, 31))
        self.delete_image_passport.setStyleSheet("QPushButton {\n"
                                                 "                                                        background-color: rgba(255, 255, 255, 170);\n"
                                                 "                                                        border-radius: 15px;\n"
                                                 "\n"
                                                 "                                                        }\n"
                                                 "                                                        QPushButton:hover {\n"
                                                 "                                                        background-color: rgba(255, 255, 255, 255);\n"
                                                 "                                                        border-radius: 15px;\n"
                                                 "                                                        transition: 2.5s;\n"
                                                 "                                                        }\n"
                                                 "                                                    ")
        self.delete_image_passport.setText("")
        self.delete_image_passport.setIcon(icon2)
        self.delete_image_passport.setObjectName("delete_image_passport")
        self.length_textedit = QtWidgets.QLabel(self.documents_tab)
        self.length_textedit.setGeometry(QtCore.QRect(1550, 365, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.length_textedit.setFont(font)
        self.length_textedit.setObjectName("length_textedit")
        self.open_explorer_achievements = QtWidgets.QPushButton(self.documents_tab)
        self.open_explorer_achievements.setGeometry(QtCore.QRect(1300, 440, 40, 40))
        self.open_explorer_achievements.setMinimumSize(QtCore.QSize(40, 40))
        self.open_explorer_achievements.setStyleSheet("QPushButton{\n"
                                                      "                                                        background-color: rgb(255, 255, 255);\n"
                                                      "                                                        border-radius: 15px;\n"
                                                      "                                                        }\n"
                                                      "\n"
                                                      "                                                        QPushButton:hover{\n"
                                                      "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                                      "                                                        }\n"
                                                      "\n"
                                                      "                                                        QPushButton:pressed{\n"
                                                      "                                                        background-color: rgb(87, 227, 137);\n"
                                                      "                                                        }\n"
                                                      "                                                    ")
        self.open_explorer_achievements.setText("")
        self.open_explorer_achievements.setIcon(icon3)
        self.open_explorer_achievements.setIconSize(QtCore.QSize(20, 20))
        self.open_explorer_achievements.setObjectName("open_explorer_achievements")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/documents.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.education_tab.addTab(self.documents_tab, icon8, "")
        self.verticalLayout_4.addWidget(self.education_tab)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setMinimumSize(QtCore.QSize(600, 0))
        self.frame2.setObjectName("frame2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.path = QtWidgets.QLineEdit(self.frame2)
        self.path.setMinimumSize(QtCore.QSize(650, 40))
        self.path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.path.setFont(font)
        self.path.setStyleSheet("border-radius: 15px;")
        self.path.setObjectName("path")
        self.horizontalLayout_9.addWidget(self.path)
        self.open_path = QtWidgets.QPushButton(self.frame2)
        self.open_path.setMinimumSize(QtCore.QSize(40, 40))
        self.open_path.setStyleSheet("QPushButton{\n"
                                     "                                                    background-color: rgb(255, 255, 255);\n"
                                     "                                                    border-radius: 15px;\n"
                                     "                                                    }\n"
                                     "\n"
                                     "                                                    QPushButton:hover{\n"
                                     "                                                    background-color: rgba(255, 255, 255, 70);\n"
                                     "                                                    }\n"
                                     "\n"
                                     "                                                    QPushButton:pressed{\n"
                                     "                                                    background-color: rgb(87, 227, 137);\n"
                                     "                                                    }\n"
                                     "                                                ")
        self.open_path.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/search.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_path.setIcon(icon9)
        self.open_path.setIconSize(QtCore.QSize(20, 20))
        self.open_path.setObjectName("open_path")
        self.horizontalLayout_9.addWidget(self.open_path)
        self.horizontalLayout_8.addWidget(self.frame2, 0, QtCore.Qt.AlignLeft)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setMinimumSize(QtCore.QSize(103, 40))
        self.cancel.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QPushButton{\n"
                                  "                                        background-color: rgb(255, 255, 255);\n"
                                  "                                        border-radius: 15px;\n"
                                  "                                        }\n"
                                  "\n"
                                  "                                        QPushButton:hover{\n"
                                  "                                        background-color: rgba(255, 255, 255, 70);\n"
                                  "                                        }\n"
                                  "\n"
                                  "                                        QPushButton:pressed{\n"
                                  "                                        background-color: rgb(87, 227, 137);\n"
                                  "                                        }\n"
                                  "                                    ")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_8.addWidget(self.cancel)
        self.clear_current_tab = QtWidgets.QPushButton(self.centralwidget)
        self.clear_current_tab.setMinimumSize(QtCore.QSize(245, 40))
        self.clear_current_tab.setMaximumSize(QtCore.QSize(1, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_current_tab.setFont(font)
        self.clear_current_tab.setStyleSheet("QPushButton{\n"
                                             "                                        background-color: rgb(255, 255, 255);\n"
                                             "                                        border-radius: 15px;\n"
                                             "                                        }\n"
                                             "\n"
                                             "                                        QPushButton:hover{\n"
                                             "                                        background-color: rgba(255, 255, 255, 70);\n"
                                             "                                        }\n"
                                             "\n"
                                             "                                        QPushButton:pressed{\n"
                                             "                                        background-color: rgb(87, 227, 137);\n"
                                             "                                        }\n"
                                             "                                    ")
        self.clear_current_tab.setObjectName("clear_current_tab")
        self.horizontalLayout_8.addWidget(self.clear_current_tab)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setMinimumSize(QtCore.QSize(115, 40))
        self.save.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton{\n"
                                "                                        background-color: rgb(255, 255, 255);\n"
                                "                                        border-radius: 15px;\n"
                                "                                        }\n"
                                "\n"
                                "                                        QPushButton:hover{\n"
                                "                                        background-color: rgba(255, 255, 255, 70);\n"
                                "                                        }\n"
                                "\n"
                                "                                        QPushButton:pressed{\n"
                                "                                        background-color: rgb(87, 227, 137);\n"
                                "                                        }\n"
                                "                                    ")
        self.save.setObjectName("save")
        self.horizontalLayout_8.addWidget(self.save)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.education_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление абитуриента"))
        self.label_37.setText(_translate("MainWindow", "Выбор формы"))
        self.label_34.setText(_translate("MainWindow", "Для СПО"))
        self.spo_11th_grade.setText(_translate("MainWindow", "11-й класс (ЕГЭ)"))
        self.spo_9th_grade.setText(_translate("MainWindow", "9-й класс (ОГЭ)"))
        self.label_36.setText(_translate("MainWindow", "Для ВУЗов"))
        self.hei_11th_grade.setText(_translate("MainWindow", "11-й класс (ЕГЭ)"))
        self.hei_spo.setText(_translate("MainWindow", "СПО"))
        self.label_2.setText(_translate("MainWindow", "Дата рождения"))
        self.label_38.setText(_translate("MainWindow", "Пол"))
        self.label_5.setText(_translate("MainWindow", "ФИО"))
        self.fio.setPlaceholderText(_translate("MainWindow", "Например, Магомедов Ислам Абакарович"))
        self.sex.setItemText(0, _translate("MainWindow", "Мужской"))
        self.sex.setItemText(1, _translate("MainWindow", "Женский"))
        self.label_10.setText(_translate("MainWindow", "Адрес"))
        self.label_7.setText(_translate("MainWindow", "Где он проживает?"))
        self.address.setPlaceholderText(_translate("MainWindow", "Например, Стальского 10В"))
        self.label_8.setText(_translate("MainWindow", "Регион"))
        self.label_9.setText(_translate("MainWindow", "Город"))
        self.label_60.setText(_translate("MainWindow", "Номер телефона абитуриента"))
        self.applicants_number.setPlaceholderText(_translate("MainWindow", "Например, +7886484383883"))
        self.label_61.setText(_translate("MainWindow", "Номер телефона родителей или законных представитилей\n"
                                                       "                                                    "))
        self.parents1_number.setPlaceholderText(_translate("MainWindow", "Например, +7999999999999"))
        self.label_62.setText(_translate("MainWindow", "Об абитуриенте"))
        self.label_63.setText(_translate("MainWindow", "О представителях"))
        self.parents1_fio.setPlaceholderText(_translate("MainWindow", "Например, Курбанов Расул Алибекович"))
        self.label_64.setText(_translate("MainWindow", "ФИО законного представителя (если нет \"-\")\n"
                                                       "                                                    "))
        self.label_65.setText(_translate("MainWindow", "ФИО законного представителя (если нет \"-\")\n"
                                                       "                                                    "))
        self.parents2_fio.setPlaceholderText(_translate("MainWindow", "Например, Магомедов Ислам Абакарович"))
        self.label_66.setText(_translate("MainWindow", "Номер телефона родителей или законных представитилей\n"
                                                       "                                                    "))
        self.parents2_number.setPlaceholderText(_translate("MainWindow", "Например, +7999999999999"))
        self.education_tab.setTabText(self.education_tab.indexOf(self.personal_data),
                                      _translate("MainWindow", "Личные данные"))
        self.label_13.setText(_translate("MainWindow", "Серия и номер паспорта (через пробел):"))
        self.series_and_number_passport.setPlaceholderText(_translate("MainWindow", "nnnn nnnnnn"))
        self.label_17.setText(_translate("MainWindow", "Паспорт"))
        self.label_14.setText(_translate("MainWindow", "Кем он был выдан?"))
        self.issued_by_whom.setPlaceholderText(_translate("MainWindow", "Например, МВД по Республике Дагестан"))
        self.label_15.setText(_translate("MainWindow", "Дата выдачи"))
        self.snils.setPlaceholderText(_translate("MainWindow", "nnn-nnn-nn nn"))
        self.label_16.setText(_translate("MainWindow", "СНИЛС"))
        self.label_11.setText(_translate("MainWindow", "Аттестат"))
        self.certificate_number.setPlaceholderText(_translate("MainWindow", "Номер, состоящий из 14 цифр"))
        self.label_18.setText(_translate("MainWindow", "Код подразделения"))
        self.division_code.setPlaceholderText(_translate("MainWindow", "nnn-nnn"))
        self.label_58.setText(_translate("MainWindow", "Номер полиса ОМС"))
        self.oms_policy_number.setPlaceholderText(_translate("MainWindow", "Номер, состоящий из 16 цифр"))
        self.label_59.setText(_translate("MainWindow", "Свидетельство о рождении"))
        self.birth_certificate_number.setPlaceholderText(_translate("MainWindow", "Серия и номер"))
        self.label_67.setText(_translate("MainWindow", "Индивидуальные достижения"))
        self.about_applicant_textedit.setPlaceholderText(_translate("MainWindow", "Опишите абитуриента"))
        self.passport_image.setText(_translate("MainWindow", "Вставьте изображение сюда"))
        self.birth_certificate_image.setText(_translate("MainWindow", "Вставьте изображение сюда"))
        self.oms_image.setText(_translate("MainWindow", "Вставьте изображение сюда"))
        self.certificate_image.setText(_translate("MainWindow", "Вставьте изображение сюда"))
        self.snils_image.setText(_translate("MainWindow", "Вставьте изображение сюда"))
        self.label_20.setText(_translate("MainWindow", "Добавьте сканы грамот, дипломов и т.д., если они имеются\n"
                                                       "                                                    "))
        self.achievements_image.setText(_translate("MainWindow", "Вставьте изображение сюда"))
        self.length_textedit.setText(_translate("MainWindow", "0/600"))
        self.education_tab.setTabText(self.education_tab.indexOf(self.documents_tab),
                                      _translate("MainWindow", "Документы и образование"))
        self.path.setPlaceholderText(_translate("MainWindow", "Укажите путь для сохранения"))
        self.cancel.setText(_translate("MainWindow", "Отмена"))
        self.clear_current_tab.setText(_translate("MainWindow", "Очистить текущую вкладку"))
        self.save.setText(_translate("MainWindow", "Сохранить"))

        spisok = ["Республика Дагестан", "Чеченская Республика", "Республика Ингушетия", "Архангельская область",
                  "Белгородская область",
                  "Владимирская область", "Воронежская область", "Ростовская область"]
        self.region.addItems(spisok)

        self.date_of_birth.setDate(self.calendar_birthday.selectedDate())
        self.date_of_issue.setDate(self.calendar_issue.selectedDate())

        self.dagestan_cities_and_villages = ["Альбурикент", "Богатырёвка", "Буйнакск", "Дагестанские Огни", "Дербент",
                                             "Избербаш", "Каспийск", "Кизилюрт", "Кизляр",
                                             "Красноармейское", "Кяхулай",
                                             "Ленинкент",
                                             "Махачкала", "Новый Кяхулай", "Новый Хушет",
                                             "Остров Чечень", "Семендер", "Сулак", "Талги", "Тарки", "Хасавюрт",
                                             "Шамхал",
                                             "Шамхал-Термен",
                                             "Южно-Сухомск"]

        self.chechnya_cities_and_villages = ["Аргун", "Бердыкель", "Грозный", "Гудермес", "Чечен-Аул"]
        self.city.addItems(self.dagestan_cities_and_villages)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.save.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.cancel.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_path.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_calendar_issue.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_calendar_birthday.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.fio.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.date_of_birth.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.date_of_issue.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.path.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.snils.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.sex.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.city.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.region.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.issued_by_whom.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.series_and_number_passport.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.address.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.certificate_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.address.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.applicants_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.clear_current_tab.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.parents1_fio.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.parents2_fio.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.parents1_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.parents2_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.oms_policy_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.birth_certificate_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.division_code.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_attachments_oms.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_attachments_certificate_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_attachments_birth_certificate.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_attachments_passport.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_attachments_snils.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_explorer_achievements.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_explorer_oms.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_explorer_snils.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_explorer_passport.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_explorer_birth_certificate.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_explorer_certificate.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.delete_image3x4.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.open_explorer_passport_2.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.code_of_parents1_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.code_of_parents2_number.setGraphicsEffect(shadow)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.code_of_applicants_number.setGraphicsEffect(shadow)

        self.left_button_passport.hide()
        self.right_button_passport.hide()
        self.delete_image_passport.hide()

        self.left_button_snils.hide()
        self.right_button_snils.hide()
        self.delete_image_snils.hide()

        self.left_button_oms.hide()
        self.right_button_oms.hide()
        self.delete_image_oms.hide()

        self.left_button_birth_certificate.hide()
        self.right_button_birth_certificate.hide()
        self.delete_image_birth_certificate.hide()

        self.right_button_achievements.hide()
        self.left_button_achievements.hide()
        self.delete_image_achievements.hide()

        self.left_button_certificate.hide()
        self.right_button_certificate.hide()
        self.delete_image_certificate.hide()

        self.fio_error.setStyleSheet("QLabel { color: red}")
        self.age_student_error.setStyleSheet("QLabel { color: red}")
        self.address_error.setStyleSheet("QLabel { color: red}")
        self.passport_error.setStyleSheet("QLabel { color: red}")
        self.issue_error.setStyleSheet("QLabel { color: red}")
        self.date_of_issue_error.setStyleSheet("QLabel { color: red}")
        self.snils_error.setStyleSheet("QLabel { color: red}")
        self.certificate_number_error.setStyleSheet("QLabel { color: red}")
        self.applicants_number_error.setStyleSheet("QLabel { color: red}")
        self.fio_parent1_error.setStyleSheet("QLabel { color: red}")
        self.fio_parent2_error.setStyleSheet("QLabel { color: red}")
        self.parent1_number_error.setStyleSheet("QLabel { color: red}")
        self.parent2_number_error.setStyleSheet("QLabel { color: red}")
        self.parent1_number_error.setStyleSheet("QLabel { color: red}")
        self.division_code_error.setStyleSheet("QLabel { color: red}")
        self.oms_policy_number_error.setStyleSheet("QLabel { color: red}")
        self.birth_certificate_number_error.setStyleSheet("QLabel { color: red}")
        self.parent1_number_error.setStyleSheet("QLabel { color: red}")

        self.calendar_birthday.hide()
