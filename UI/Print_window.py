from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_print(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1095, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(-10, 0, 1131, 80))
        self.horizontalFrame.setStyleSheet("box-shadow: 15px 15px 15px grey;\n"
                                           "background-color: rgb(255, 255, 255);")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setMinimumSize(QtCore.QSize(10, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(60, 50))
        self.pushButton_4.setStyleSheet("border: none;\n"
                                        "margin:  0px;\n"
                                        "padding: 0px;\n"
                                        "")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(200, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Noto Looped Lao UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 90, 391, 501))
        self.frame.setStyleSheet("background-color: rgb(217, 217, 217);\n"
                                 "border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.open_file_from_main_2 = QtWidgets.QPushButton(self.frame)
        self.open_file_from_main_2.setGeometry(QtCore.QRect(30, 25, 321, 38))
        self.open_file_from_main_2.setStyleSheet("QPushButton{\n"
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
        self.open_file_from_main_2.setObjectName("open_file_from_main_2")
        self.add_student_2 = QtWidgets.QPushButton(self.frame)
        self.add_student_2.setEnabled(False)
        self.add_student_2.setGeometry(QtCore.QRect(30, 115, 321, 38))
        self.add_student_2.setStyleSheet("QPushButton{\n"
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
        self.add_student_2.setObjectName("add_student_2")
        self.about_the_author_2 = QtWidgets.QPushButton(self.frame)
        self.about_the_author_2.setGeometry(QtCore.QRect(30, 205, 321, 38))
        self.about_the_author_2.setStyleSheet("QPushButton{\n"
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
        self.about_the_author_2.setObjectName("about_the_author_2")
        self.open_table_2 = QtWidgets.QPushButton(self.frame)
        self.open_table_2.setEnabled(True)
        self.open_table_2.setGeometry(QtCore.QRect(30, 70, 321, 38))
        self.open_table_2.setStyleSheet("QPushButton{\n"
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
        self.open_table_2.setObjectName("open_table_2")
        self.print_documents_2 = QtWidgets.QPushButton(self.frame)
        self.print_documents_2.setEnabled(True)
        self.print_documents_2.setGeometry(QtCore.QRect(30, 160, 321, 38))
        self.print_documents_2.setStyleSheet("QPushButton{\n"
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
        self.print_documents_2.setObjectName("print_documents_2")
        self.open_file_from_main_3 = QtWidgets.QPushButton(self.frame)
        self.open_file_from_main_3.setGeometry(QtCore.QRect(30, 250, 321, 38))
        self.open_file_from_main_3.setStyleSheet("QPushButton{\n"
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
        self.open_file_from_main_3.setObjectName("open_file_from_main_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 90, 20, 501))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.open_file_from_main_4 = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_from_main_4.setGeometry(QtCore.QRect(950, 550, 131, 40))
        self.open_file_from_main_4.setStyleSheet("QPushButton{\n"
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
        self.open_file_from_main_4.setObjectName("open_file_from_main_4")
        self.open_file_from_main_5 = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_from_main_5.setGeometry(QtCore.QRect(810, 550, 131, 40))
        self.open_file_from_main_5.setStyleSheet("QPushButton{\n"
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
        self.open_file_from_main_5.setObjectName("open_file_from_main_5")
        self.frame_enrollment = QtWidgets.QFrame(self.centralwidget)
        self.frame_enrollment.setGeometry(QtCore.QRect(419, 89, 671, 451))
        self.frame_enrollment.setStyleSheet("border: none;")
        self.frame_enrollment.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_enrollment.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_enrollment.setObjectName("frame_enrollment")
        self.label_2 = QtWidgets.QLabel(self.frame_enrollment)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_enrollment)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 511, 36))
        self.lineEdit.setStyleSheet("border-radius: 15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.frame_rejected = QtWidgets.QFrame(self.centralwidget)
        self.frame_rejected.setGeometry(QtCore.QRect(419, 89, 671, 451))
        self.frame_rejected.setStyleSheet("border: none;")
        self.frame_rejected.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rejected.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rejected.setObjectName("frame_rejected")
        self.label_3 = QtWidgets.QLabel(self.frame_rejected)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_rejected)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 50, 511, 36))
        self.lineEdit_2.setStyleSheet("border-radius: 15px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_enrollment.raise_()
        self.horizontalFrame.raise_()
        self.frame.raise_()
        self.line.raise_()
        self.open_file_from_main_4.raise_()
        self.open_file_from_main_5.raise_()
        self.frame_rejected.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.frame_rejected.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Печать документов"))
        self.label.setText(_translate("MainWindow", "Абитуриент"))
        self.open_file_from_main_2.setText(_translate("MainWindow", "Приказ о зачислении"))
        self.add_student_2.setText(_translate("MainWindow", "Заявка на рассмотрении"))
        self.about_the_author_2.setText(_translate("MainWindow", "Что-то"))
        self.open_table_2.setText(_translate("MainWindow", "Приказ об отказе"))
        self.print_documents_2.setText(_translate("MainWindow", "Какой-то документ"))
        self.open_file_from_main_3.setText(_translate("MainWindow", "Зачем столько кнопок???"))
        self.open_file_from_main_4.setText(_translate("MainWindow", "Распечатать"))
        self.open_file_from_main_5.setText(_translate("MainWindow", "Сбросить"))
        self.label_2.setText(_translate("MainWindow", "ФИО абитуриента"))
        self.label_3.setText(_translate("MainWindow", "ФИО абитуриента(2)"))
