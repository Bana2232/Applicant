from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewing_applicants(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1169, 690)
        MainWindow.setMinimumSize(QtCore.QSize(1169, 690))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
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
        font.setFamily("Montserrat")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.horizontalFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame1.setAutoFillBackground(False)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(80)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_and_hide_filters = QtWidgets.QPushButton(self.horizontalFrame1)
        self.show_and_hide_filters.setMinimumSize(QtCore.QSize(41, 41))
        self.show_and_hide_filters.setMaximumSize(QtCore.QSize(41, 41))
        self.show_and_hide_filters.setStyleSheet("QPushButton{\n"
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
        self.show_and_hide_filters.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/filter-off-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_and_hide_filters.setIcon(icon1)
        self.show_and_hide_filters.setIconSize(QtCore.QSize(25, 25))
        self.show_and_hide_filters.setObjectName("show_and_hide_filters")
        self.horizontalLayout_2.addWidget(self.show_and_hide_filters)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.search_line = QtWidgets.QLineEdit(self.horizontalFrame1)
        self.search_line.setMinimumSize(QtCore.QSize(600, 41))
        self.search_line.setMaximumSize(QtCore.QSize(16777215, 41))
        self.search_line.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "text-color: rgb(222, 221, 218);\n"
                                       "border-radius: 15px;\n"
                                       "padding-left:10px;\n"
                                       "\n"
                                       "")
        self.search_line.setText("")
        self.search_line.setClearButtonEnabled(False)
        self.search_line.setObjectName("search_line")
        self.horizontalLayout_4.addWidget(self.search_line, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.horizontalFrame1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(291, 0))
        self.frame.setStyleSheet("QFrame {\n"
                                 "    border: none;\n"
                                 "    background-color: rgb(217, 217, 217);\n"
                                 "    border-radius: 15px;\n"
                                 "    margin-left: 5px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.sort_by_name = QtWidgets.QPushButton(self.frame)
        self.sort_by_name.setGeometry(QtCore.QRect(230, 20, 41, 41))
        self.sort_by_name.setMinimumSize(QtCore.QSize(41, 41))
        self.sort_by_name.setStyleSheet("QPushButton{\n"
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
        self.sort_by_name.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/sort-desc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sort_by_name.setIcon(icon2)
        self.sort_by_name.setIconSize(QtCore.QSize(25, 25))
        self.sort_by_name.setObjectName("sort_by_name")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.number_of_elements = QtWidgets.QLabel(self.frame)
        self.number_of_elements.setGeometry(QtCore.QRect(10, 220, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.number_of_elements.setFont(font)
        self.number_of_elements.setObjectName("number_of_elements")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.is_accepted_button = QtWidgets.QRadioButton(self.frame)
        self.is_accepted_button.setGeometry(QtCore.QRect(10, 120, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.is_accepted_button.setFont(font)
        self.is_accepted_button.setObjectName("is_accepted_button")
        self.is_not_accepted_button = QtWidgets.QRadioButton(self.frame)
        self.is_not_accepted_button.setGeometry(QtCore.QRect(80, 120, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.is_not_accepted_button.setFont(font)
        self.is_not_accepted_button.setObjectName("is_not_accepted_button")
        self.show_all_button = QtWidgets.QRadioButton(self.frame)
        self.show_all_button.setGeometry(QtCore.QRect(150, 120, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.show_all_button.setFont(font)
        self.show_all_button.setChecked(True)
        self.show_all_button.setObjectName("show_all_button")
        self.faculty_combobox = QtWidgets.QComboBox(self.frame)
        self.faculty_combobox.setGeometry(QtCore.QRect(10, 170, 171, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.faculty_combobox.setFont(font)
        self.faculty_combobox.setStyleSheet("QComboBox {\n"
                                            "border: 1px solid #ced4da;\n"
                                            "border-radius: 15px;\n"
                                            "padding-left: 10px;\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::drop-down {\n"
                                            "border:0px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::down-arrow {\n"
                                            "image: url(images/arrow-down.png);\n"
                                            "width: 24px;\n"
                                            "height: 24px;\n"
                                            "margin-right: 15px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox:on{\n"
                                            "    border: 2px solid rgb(87, 227, 137);\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox QListView {\n"
                                            "border-radius: 15px;\n"
                                            "    font-size: 24px;\n"
                                            "    padding: 5px;\n"
                                            "    background-color: #fff;\n"
                                            "    outline: 0px;\n"
                                            "    \n"
                                            "    color: rgb(0, 0, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox QListView::item {\n"
                                            "padding-left: 10px;\n"
                                            "    background-color: #00ff00;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox QListView:item:hover {\n"
                                            "    background-color: rgb(87, 227, 137);\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox QListView:item:selected {\n"
                                            "    background-color: rgb(87, 227, 137);\n"
                                            "}\n"
                                            "")
        self.faculty_combobox.setObjectName("faculty_combobox")
        self.faculty_combobox.addItem("")
        self.horizontalLayout_3.addWidget(self.frame)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setStyleSheet("QListWidget {\n"
                                      "border-radius: 15px;\n"
                                      "background-color: rgb(217, 217, 217);\n"
                                      "margin-right: 5px;\n"
                                      "padding-top: 5px;\n"
                                      "padding-right: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QListWidget:item{\n"
                                      "    color: rgb(0, 0, 0);\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 15px;\n"
                                      "    margin-bottom: 5px;\n"
                                      "    padding-top: 15px;\n"
                                      "    padding-bottom: 15px;\n"
                                      "    padding-left: 6px;\n"
                                      "}\n"
                                      "\n"
                                      "QListWidget:item:selected {\n"
                                      "    background-color: rgb(192, 191, 188);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "    background-color: #BFBFBF;\n"
                                      "    border-radius: 3px;\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical:hover {\n"
                                      "    background-color: #43464D;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical:pressed {\n"
                                      "    background-color: rgb(51, 209, 122);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar{\n"
                                      "    border: none;\n"
                                      "    max-width: 10px;\n"
                                      "    margin: 0px 0 0px 0;\n"
                                      "    background-color: rgb(247, 247, 247);\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:handle{\n"
                                      "    background-color: rgb(163, 163, 163);\n"
                                      "    border-radius: 5px;\n"
                                      "    min-height: 30px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:handle::hover{\n"
                                      "    background-color: rgb(134, 134, 134);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:handle::pressed{\n"
                                      "    background-color: rgb(158, 227, 149);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::sub-line{\n"
                                      "    border: none;\n"
                                      "    height: 5px;\n"
                                      "    background-color: rgb(247, 247, 247);\n"
                                      "    border-top-left-radius: 5px;\n"
                                      "    border-top-right-radius: 5px;\n"
                                      "    subcontrol-position: top;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-line{\n"
                                      "    border: none;\n"
                                      "    height: 5px;\n"
                                      "    background-color: rgb(247, 247, 247);\n"
                                      "    border-bottom-left-radius: 5px;\n"
                                      "    border-bottom-right-radius: 5px;\n"
                                      "    subcontrol-position: bottom;\n"
                                      "}\n"
                                      "")
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотр абитуриентов"))
        self.label.setText(_translate("MainWindow", "Абитуриент"))
        self.search_line.setPlaceholderText(_translate("MainWindow", "Поиск по ФИО"))
        self.label_3.setText(_translate("MainWindow", "Сортировка по ФИО:"))
        self.number_of_elements.setText(_translate("MainWindow", "Всего элементов: 0"))
        self.label_4.setText(_translate("MainWindow", "Приняты:"))
        self.is_accepted_button.setText(_translate("MainWindow", "Да"))
        self.is_not_accepted_button.setText(_translate("MainWindow", "Нет"))
        self.show_all_button.setText(_translate("MainWindow", "Показать всех"))
        self.faculty_combobox.setItemText(0, _translate("MainWindow", "Факультет"))
