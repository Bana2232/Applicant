from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1095, 600)
        MainWindow.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.current_time_of_day = QtWidgets.QLabel(self.centralwidget)
        self.current_time_of_day.setGeometry(QtCore.QRect(20, 90, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.current_time_of_day.setFont(font)
        self.current_time_of_day.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.current_time_of_day.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.current_time_of_day.setObjectName("current_time_of_day")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(-10, 0, 1131, 80))
        self.horizontalFrame.setStyleSheet("box-shadow: 15px 15px 15px grey;\n"
                                           "background-color: rgb(255, 255, 255);")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(10, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(60, 50))
        self.pushButton.setStyleSheet("border: none;\n"
                                      "margin:  0px;\n"
                                      "padding: 0px;\n"
                                      "")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(200, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 150, 521, 411))
        self.frame.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                 "border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.open_file_from_main = QtWidgets.QPushButton(self.frame)
        self.open_file_from_main.setGeometry(QtCore.QRect(90, 40, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.open_file_from_main.setFont(font)
        self.open_file_from_main.setStyleSheet("QPushButton{\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "border-radius: 15px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgba(255, 255, 255, 70);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed{\n"
                                               "background-color: rgb(87, 227, 137);\n"
                                               "}")
        self.open_file_from_main.setObjectName("open_file_from_main")
        self.add_student = QtWidgets.QPushButton(self.frame)
        self.add_student.setGeometry(QtCore.QRect(90, 130, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.add_student.setFont(font)
        self.add_student.setStyleSheet("QPushButton{\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 15px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgba(255, 255, 255, 70);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "background-color:rgb(87, 227, 137);\n"
                                       "}")
        self.add_student.setObjectName("add_student")
        self.parameters = QtWidgets.QPushButton(self.frame)
        self.parameters.setGeometry(QtCore.QRect(90, 265, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.parameters.setFont(font)
        self.parameters.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 70);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "background-color:rgb(87, 227, 137);\n"
                                      "}")
        self.parameters.setObjectName("parameters")
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(90, 310, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton{\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "border-radius: 15px;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover{\n"
                                "background-color: rgba(255, 255, 255, 70);\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed{\n"
                                "background-color:rgb(87, 227, 137);\n"
                                "}")
        self.exit.setObjectName("exit")
        self.open_table = QtWidgets.QPushButton(self.frame)
        self.open_table.setGeometry(QtCore.QRect(90, 85, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.open_table.setFont(font)
        self.open_table.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 70);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "background-color:rgb(87, 227, 137);\n"
                                      "}")
        self.open_table.setObjectName("open_table")
        self.open_list_of_applicants = QtWidgets.QPushButton(self.frame)
        self.open_list_of_applicants.setGeometry(QtCore.QRect(90, 175, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.open_list_of_applicants.setFont(font)
        self.open_list_of_applicants.setStyleSheet("QPushButton{\n"
                                                   "background-color: rgb(255, 255, 255);\n"
                                                   "border-radius: 15px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover{\n"
                                                   "background-color: rgba(255, 255, 255, 70);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:pressed{\n"
                                                   "background-color:rgb(87, 227, 137);\n"
                                                   "}")
        self.open_list_of_applicants.setObjectName("open_list_of_applicants")
        self.print_documents = QtWidgets.QPushButton(self.frame)
        self.print_documents.setGeometry(QtCore.QRect(90, 220, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.print_documents.setFont(font)
        self.print_documents.setStyleSheet("QPushButton{\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "border-radius: 15px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgba(255, 255, 255, 70);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "background-color:rgb(87, 227, 137);\n"
                                           "}")
        self.print_documents.setObjectName("print_documents")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(740, 100, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(650, 150, 431, 411))
        self.frame_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                   "border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.recent_file_1 = QtWidgets.QPushButton(self.frame_2)
        self.recent_file_1.setGeometry(QtCore.QRect(60, 30, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.recent_file_1.setFont(font)
        self.recent_file_1.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 70);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(87, 227, 137);\n"
                                         "}")
        self.recent_file_1.setText("")
        self.recent_file_1.setObjectName("recent_file_1")
        self.recent_file_2 = QtWidgets.QPushButton(self.frame_2)
        self.recent_file_2.setGeometry(QtCore.QRect(60, 75, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.recent_file_2.setFont(font)
        self.recent_file_2.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 70);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(87, 227, 137);\n"
                                         "}")
        self.recent_file_2.setText("")
        self.recent_file_2.setObjectName("recent_file_2")
        self.recent_file_3 = QtWidgets.QPushButton(self.frame_2)
        self.recent_file_3.setGeometry(QtCore.QRect(60, 120, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.recent_file_3.setFont(font)
        self.recent_file_3.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 70);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(87, 227, 137);\n"
                                         "}")
        self.recent_file_3.setText("")
        self.recent_file_3.setObjectName("recent_file_3")
        self.recent_file_4 = QtWidgets.QPushButton(self.frame_2)
        self.recent_file_4.setGeometry(QtCore.QRect(60, 165, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.recent_file_4.setFont(font)
        self.recent_file_4.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 70);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(87, 227, 137);\n"
                                         "}")
        self.recent_file_4.setText("")
        self.recent_file_4.setObjectName("recent_file_4")
        self.recent_file_5 = QtWidgets.QPushButton(self.frame_2)
        self.recent_file_5.setGeometry(QtCore.QRect(60, 210, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.recent_file_5.setFont(font)
        self.recent_file_5.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 70);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(87, 227, 137);\n"
                                         "}")
        self.recent_file_5.setText("")
        self.recent_file_5.setObjectName("recent_file_5")
        self.recent_file_6 = QtWidgets.QPushButton(self.frame_2)
        self.recent_file_6.setGeometry(QtCore.QRect(60, 255, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.recent_file_6.setFont(font)
        self.recent_file_6.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 70);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(87, 227, 137);\n"
                                         "}")
        self.recent_file_6.setText("")
        self.recent_file_6.setObjectName("recent_file_6")
        self.recent_file_7 = QtWidgets.QPushButton(self.frame_2)
        self.recent_file_7.setGeometry(QtCore.QRect(60, 300, 321, 38))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        self.recent_file_7.setFont(font)
        self.recent_file_7.setStyleSheet("QPushButton{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 70);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(87, 227, 137);\n"
                                         "}")
        self.recent_file_7.setText("")
        self.recent_file_7.setObjectName("recent_file_7")
        self.empty_file_label = QtWidgets.QLabel(self.frame_2)
        self.empty_file_label.setGeometry(QtCore.QRect(10, 10, 411, 391))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(13)
        self.empty_file_label.setFont(font)
        self.empty_file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.empty_file_label.setObjectName("empty_file_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.current_time_of_day.setText(_translate("MainWindow", "Добрый день!"))
        self.label.setText(_translate("MainWindow", "Абитуриент"))
        self.open_file_from_main.setText(_translate("MainWindow", "Открыть файл"))
        self.add_student.setText(_translate("MainWindow", "Добавить абитуриента"))
        self.parameters.setText(_translate("MainWindow", "Параметры"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.open_table.setText(_translate("MainWindow", "Открыть таблицу"))
        self.open_list_of_applicants.setText(_translate("MainWindow", "Просмотр списка абитуриентов"))
        self.print_documents.setText(_translate("MainWindow", "Печать документов"))
        self.label_3.setText(_translate("MainWindow", "Недавние файлы"))
        self.empty_file_label.setText(_translate("MainWindow", "На данный момент здесь пусто"))

        self.recent_file_2.hide()
        self.recent_file_3.hide()
        self.recent_file_4.hide()
        self.recent_file_5.hide()
        self.recent_file_6.hide()
        self.recent_file_7.hide()

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        self.horizontalFrame.setGraphicsEffect(shadow)

        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(5)
        shadow2.setXOffset(3)
        shadow2.setYOffset(3)
        self.open_file_from_main.setGraphicsEffect(shadow2)

        shadow3 = QGraphicsDropShadowEffect()
        shadow3.setBlurRadius(5)
        shadow3.setXOffset(3)
        shadow3.setYOffset(3)
        self.open_table.setGraphicsEffect(shadow3)

        shadow4 = QGraphicsDropShadowEffect()
        shadow4.setBlurRadius(5)
        shadow4.setXOffset(3)
        shadow4.setYOffset(3)
        self.add_student.setGraphicsEffect(shadow4)

        shadow5 = QGraphicsDropShadowEffect()
        shadow5.setBlurRadius(5)
        shadow5.setXOffset(3)
        shadow5.setYOffset(3)
        self.parameters.setGraphicsEffect(shadow5)

        shadow6 = QGraphicsDropShadowEffect()
        shadow6.setBlurRadius(5)
        shadow6.setXOffset(3)
        shadow6.setYOffset(3)
        self.exit.setGraphicsEffect(shadow6)

        shadow7 = QGraphicsDropShadowEffect()
        shadow7.setBlurRadius(5)
        shadow7.setXOffset(3)
        shadow7.setYOffset(3)
        self.recent_file_1.setGraphicsEffect(shadow7)

        shadow8 = QGraphicsDropShadowEffect()
        shadow8.setBlurRadius(5)
        shadow8.setXOffset(3)
        shadow8.setYOffset(3)
        self.recent_file_2.setGraphicsEffect(shadow8)

        shadow9 = QGraphicsDropShadowEffect()
        shadow9.setBlurRadius(5)
        shadow9.setXOffset(3)
        shadow9.setYOffset(3)
        self.recent_file_3.setGraphicsEffect(shadow9)

        shadow10 = QGraphicsDropShadowEffect()
        shadow10.setBlurRadius(5)
        shadow10.setXOffset(3)
        shadow10.setYOffset(3)
        self.recent_file_4.setGraphicsEffect(shadow10)

        shadow11 = QGraphicsDropShadowEffect()
        shadow11.setBlurRadius(5)
        shadow11.setXOffset(3)
        shadow11.setYOffset(3)
        self.recent_file_5.setGraphicsEffect(shadow11)

        shadow12 = QGraphicsDropShadowEffect()
        shadow12.setBlurRadius(5)
        shadow12.setXOffset(3)
        shadow12.setYOffset(3)
        self.recent_file_6.setGraphicsEffect(shadow12)

        shadow13 = QGraphicsDropShadowEffect()
        shadow13.setBlurRadius(5)
        shadow13.setXOffset(3)
        shadow13.setYOffset(3)
        self.recent_file_7.setGraphicsEffect(shadow13)

        shadow14 = QGraphicsDropShadowEffect()
        shadow14.setBlurRadius(5)
        shadow14.setXOffset(3)
        shadow14.setYOffset(3)
        self.print_documents.setGraphicsEffect(shadow14)

        shadow15 = QGraphicsDropShadowEffect()
        shadow15.setBlurRadius(5)
        shadow15.setXOffset(3)
        shadow15.setYOffset(3)
        self.open_list_of_applicants.setGraphicsEffect(shadow15)
