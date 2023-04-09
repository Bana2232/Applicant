from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_table(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1685, 748)
        MainWindow.setWindowTitle("")
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "                background-color: rgb(255, 255, 255);\n"
                                 "                text: color: rgb(0, 0, 0);\n"
                                 "                }\n"
                                 "            ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setStyleSheet("QFrame{\n"
                                         "                                background-color: rgb(222, 221, 218);\n"
                                         "                                border-radius: 10px}\n"
                                         "                            ")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalFrame)
        self.frame.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, 550, -1)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, 280, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setMinimumSize(QtCore.QSize(40, 35))
        self.save_button.setMaximumSize(QtCore.QSize(40, 35))
        self.save_button.setStyleSheet("QPushButton {\n"
                                       "                                                                        border: none;\n"
                                       "                                                                        margin: 0px;\n"
                                       "                                                                        padding: 0px;\n"
                                       "                                                                        }\n"
                                       "                                                                    ")
        self.save_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/save.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon)
        self.save_button.setIconSize(QtCore.QSize(30, 30))
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setMinimumSize(QtCore.QSize(40, 35))
        self.back.setMaximumSize(QtCore.QSize(40, 35))
        self.back.setStyleSheet("QPushButton {\n"
                                "                                                                        border: none;\n"
                                "                                                                        margin: 0px;\n"
                                "                                                                        padding: 0px;\n"
                                "                                                                        }\n"
                                "                                                                    ")
        self.back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("\n"
                                      "images/left_arrow.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setIconSize(QtCore.QSize(20, 30))
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.forward = QtWidgets.QPushButton(self.frame)
        self.forward.setMinimumSize(QtCore.QSize(40, 35))
        self.forward.setMaximumSize(QtCore.QSize(40, 35))
        self.forward.setStyleSheet("QPushButton {\n"
                                   "                                                                        border: none;\n"
                                   "                                                                        margin: 0px;\n"
                                   "                                                                        padding: 0px;\n"
                                   "                                                                        }\n"
                                   "                                                                    ")
        self.forward.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("\n"
                                      "images/right_arrow.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward.setIcon(icon2)
        self.forward.setIconSize(QtCore.QSize(20, 30))
        self.forward.setObjectName("forward")
        self.horizontalLayout.addWidget(self.forward)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(200, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_line = QtWidgets.QLineEdit(self.frame)
        self.search_line.setMinimumSize(QtCore.QSize(0, 35))
        self.search_line.setMaximumSize(QtCore.QSize(800, 16777215))
        self.search_line.setStyleSheet("background-color:\n"
                                       "                                                                                rgb(255, 255, 255);\n"
                                       "                                                                                text-color: rgb(222, 221, 218);\n"
                                       "                                                                                border-radius: 15px;\n"
                                       "                                                                                padding-left:10px;\n"
                                       "\n"
                                       "                                                                            ")
        self.search_line.setObjectName("search_line")
        self.horizontalLayout_2.addWidget(self.search_line)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.verticalFrame)
        self.frame_2.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(-1, -1, 280, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.current_cell = QtWidgets.QLineEdit(self.frame_2)
        self.current_cell.setEnabled(False)
        self.current_cell.setMinimumSize(QtCore.QSize(90, 35))
        self.current_cell.setMaximumSize(QtCore.QSize(90, 35))
        self.current_cell.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "                                                        border-radius: 15px;\n"
                                        "                                                        padding-left:10px;\n"
                                        "color: rgb(0, 0, 0);")
        self.current_cell.setObjectName("current_cell")
        self.horizontalLayout_3.addWidget(self.current_cell)
        self.bold_text = QtWidgets.QPushButton(self.frame_2)
        self.bold_text.setMinimumSize(QtCore.QSize(40, 35))
        self.bold_text.setMaximumSize(QtCore.QSize(60, 16777215))
        self.bold_text.setToolTip("")
        self.bold_text.setToolTipDuration(1)
        self.bold_text.setWhatsThis("")
        self.bold_text.setStyleSheet("QPushButton {\n"
                                     "                                                        border: none;\n"
                                     "                                                        margin: 0px;\n"
                                     "                                                        padding: 0px;\n"
                                     "                                                        border-radius: 10px;\n"
                                     "                                                        }\n"
                                     "                                                    ")
        self.bold_text.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bold_text.setIcon(icon3)
        self.bold_text.setIconSize(QtCore.QSize(30, 25))
        self.bold_text.setObjectName("bold_text")
        self.horizontalLayout_3.addWidget(self.bold_text)
        self.italic_text = QtWidgets.QPushButton(self.frame_2)
        self.italic_text.setMinimumSize(QtCore.QSize(40, 35))
        self.italic_text.setMaximumSize(QtCore.QSize(60, 16777215))
        self.italic_text.setStyleSheet("QPushButton {\n"
                                       "                                                        border: none;\n"
                                       "                                                        margin: 0px;\n"
                                       "                                                        padding: 0px;\n"
                                       "                                                        border-radius: 10px;\n"
                                       "                                                        }\n"
                                       "                                                    ")
        self.italic_text.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italic_text.setIcon(icon4)
        self.italic_text.setIconSize(QtCore.QSize(30, 25))
        self.italic_text.setAutoDefault(False)
        self.italic_text.setObjectName("italic_text")
        self.horizontalLayout_3.addWidget(self.italic_text)
        self.underlined_text = QtWidgets.QPushButton(self.frame_2)
        self.underlined_text.setMinimumSize(QtCore.QSize(40, 35))
        self.underlined_text.setMaximumSize(QtCore.QSize(60, 16777215))
        self.underlined_text.setStyleSheet("QPushButton {\n"
                                           "                                                        border: none;\n"
                                           "                                                        margin: 0px;\n"
                                           "                                                        padding: 0px;\n"
                                           "                                                        border-radius: 10px;\n"
                                           "                                                        }\n"
                                           "                                                    ")
        self.underlined_text.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/underlined.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underlined_text.setIcon(icon5)
        self.underlined_text.setObjectName("underlined_text")
        self.horizontalLayout_3.addWidget(self.underlined_text)
        self.fontComboBox = QtWidgets.QFontComboBox(self.frame_2)
        self.fontComboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.fontComboBox.setStyleSheet("QComboBox {\n"
                                        "    border: 1px solid #ced4da;\n"
                                        "    border-radius: 15px;\n"
                                        "    padding-left: 10px;\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    }\n"
                                        "    \n"
                                        "    QComboBox::drop-down {\n"
                                        "    border:0px;\n"
                                        "    }\n"
                                        "    \n"
                                        "    QComboBox::down-arrow {\n"
                                        "    image: url(images/arrow-down.png);\n"
                                        "    width: 24px;\n"
                                        "    height: 24px;\n"
                                        "    margin-right: 15px;\n"
                                        "    }\n"
                                        "    \n"
                                        "    QComboBox:on{\n"
                                        "        border: 2px solid rgb(87, 227, 137);\n"
                                        "    }\n"
                                        "    \n"
                                        "    QComboBox QListView {\n"
                                        "    border-radius: 5px;\n"
                                        "        font-size: 24px;\n"
                                        "        padding: 5px;\n"
                                        "        background-color: #fff;\n"
                                        "        outline: 0px;\n"
                                        "        \n"
                                        "        color: rgb(0, 0, 0);\n"
                                        "    }\n"
                                        "    \n"
                                        "    QComboBox QListView::item {\n"
                                        "    padding-left: 10px;\n"
                                        "        background-color: #00ff00;\n"
                                        "    }\n"
                                        "    \n"
                                        "    QComboBox QListView:item:hover {\n"
                                        "        background-color: rgb(87, 227, 137);\n"
                                        "    }\n"
                                        "    \n"
                                        "    QComboBox QListView:item:selected {\n"
                                        "        background-color: rgb(87, 227, 137);\n"
                                        "    }\n"
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
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_3.addWidget(self.fontComboBox)
        self.text_size = QtWidgets.QComboBox(self.frame_2)
        self.text_size.setMinimumSize(QtCore.QSize(0, 35))
        self.text_size.setStyleSheet("QComboBox {\n"
                                     "    border: 1px solid #ced4da;\n"
                                     "    border-radius: 15px;\n"
                                     "    padding-left: 10px;\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "    }\n"
                                     "    \n"
                                     "    QComboBox::drop-down {\n"
                                     "    border:0px;\n"
                                     "    }\n"
                                     "    \n"
                                     "    QComboBox::down-arrow {\n"
                                     "    image: url(images/arrow-down.png);\n"
                                     "    width: 24px;\n"
                                     "    height: 24px;\n"
                                     "    margin-right: 15px;\n"
                                     "    }\n"
                                     "    \n"
                                     "    QComboBox:on{\n"
                                     "        border: 2px solid rgb(87, 227, 137);\n"
                                     "    }\n"
                                     "    \n"
                                     "    QComboBox QListView {\n"
                                     "         min-width: 120px;\n"
                                     "         border-radius: 5px;\n"
                                     "        font-size: 24px;\n"
                                     "        padding: 5px;\n"
                                     "        background-color: #fff;\n"
                                     "        outline: 0px;\n"
                                     "        \n"
                                     "        color: rgb(0, 0, 0);\n"
                                     "    }\n"
                                     "    \n"
                                     "    QComboBox QListView::item {\n"
                                     "    padding-left: 10px;\n"
                                     "        background-color: #00ff00;\n"
                                     "    }\n"
                                     "    \n"
                                     "    QComboBox QListView:item:hover {\n"
                                     "        background-color: rgb(87, 227, 137);\n"
                                     "    }\n"
                                     "    \n"
                                     "    QComboBox QListView:item:selected {\n"
                                     "        background-color: rgb(87, 227, 137);\n"
                                     "    }\n"
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
        self.text_size.setObjectName("text_size")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.text_size.addItem("")
        self.horizontalLayout_3.addWidget(self.text_size)
        self.text_color = QtWidgets.QComboBox(self.frame_2)
        self.text_color.setMinimumSize(QtCore.QSize(0, 35))
        self.text_color.setStyleSheet("QComboBox {\n"
                                      "    border: 1px solid #ced4da;\n"
                                      "    border-radius: 15px;\n"
                                      "    padding-left: 10px;\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    }\n"
                                      "    \n"
                                      "    QComboBox::drop-down {\n"
                                      "    border:0px;\n"
                                      "    }\n"
                                      "    \n"
                                      "    QComboBox::down-arrow {\n"
                                      "    image: url(/home/salih/Загрузки/arrow-down.png);\n"
                                      "    width: 24px;\n"
                                      "    height: 24px;\n"
                                      "    margin-right: 15px;\n"
                                      "    }\n"
                                      "    \n"
                                      "    QComboBox:on{\n"
                                      "        border: 2px solid rgb(87, 227, 137);\n"
                                      "    }\n"
                                      "    \n"
                                      "    QComboBox QListView {\n"
                                      "         min-width: 200px;\n"
                                      "        border-radius: 5px;\n"
                                      "        font-size: 24px;\n"
                                      "        padding: 5px;\n"
                                      "        background-color: #fff;\n"
                                      "        outline: 0px;\n"
                                      "        \n"
                                      "        color: rgb(0, 0, 0);\n"
                                      "    }\n"
                                      "    \n"
                                      "    QComboBox QListView::item {\n"
                                      "    padding-left: 10px;\n"
                                      "        background-color: #00ff00;\n"
                                      "    }\n"
                                      "    \n"
                                      "    QComboBox QListView:item:hover {\n"
                                      "        background-color: rgb(87, 227, 137);\n"
                                      "    }\n"
                                      "    \n"
                                      "    QComboBox QListView:item:selected {\n"
                                      "        background-color: rgb(87, 227, 137);\n"
                                      "    }\n"
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
                                      "\n"
                                      "")
        self.text_color.setObjectName("text_color")
        self.horizontalLayout_3.addWidget(self.text_color)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setMinimumSize(QtCore.QSize(1, 40))
        self.line_2.setMaximumSize(QtCore.QSize(1, 40))
        self.line_2.setStyleSheet("background-color: rgb(154, 153, 150);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.align_left = QtWidgets.QPushButton(self.frame_2)
        self.align_left.setMinimumSize(QtCore.QSize(40, 35))
        self.align_left.setMaximumSize(QtCore.QSize(43, 16777215))
        self.align_left.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "                                                        border-radius: 10px;\n"
                                      "                                                        }\n"
                                      "                                                        QPushButton:hover{\n"
                                      "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                      "                                                        }\n"
                                      "                                                    ")
        self.align_left.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/left_alignment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.align_left.setIcon(icon6)
        self.align_left.setObjectName("align_left")
        self.horizontalLayout_3.addWidget(self.align_left)
        self.align_center = QtWidgets.QPushButton(self.frame_2)
        self.align_center.setMinimumSize(QtCore.QSize(40, 35))
        self.align_center.setMaximumSize(QtCore.QSize(43, 16777215))
        self.align_center.setStyleSheet("QPushButton {\n"
                                        "                                                        background-color: rgb(255, 255, 255);\n"
                                        "                                                        border-radius: 10px;\n"
                                        "                                                        }\n"
                                        "                                                        QPushButton:hover{\n"
                                        "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                        "                                                        }\n"
                                        "                                                    ")
        self.align_center.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/center_alignment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.align_center.setIcon(icon7)
        self.align_center.setIconSize(QtCore.QSize(16, 20))
        self.align_center.setObjectName("align_center")
        self.horizontalLayout_3.addWidget(self.align_center)
        self.align_right = QtWidgets.QPushButton(self.frame_2)
        self.align_right.setMinimumSize(QtCore.QSize(40, 35))
        self.align_right.setMaximumSize(QtCore.QSize(43, 16777215))
        self.align_right.setStyleSheet("QPushButton {\n"
                                       "                                                        background-color: rgb(255, 255, 255);\n"
                                       "                                                        border-radius: 10px;\n"
                                       "                                                        }\n"
                                       "                                                        QPushButton:hover{\n"
                                       "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                       "                                                        }\n"
                                       "                                                    ")
        self.align_right.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/right_alignment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.align_right.setIcon(icon8)
        self.align_right.setObjectName("align_right")
        self.horizontalLayout_3.addWidget(self.align_right)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setMaximumSize(QtCore.QSize(1, 40))
        self.line.setStyleSheet("background-color: rgb(154, 153, 150);\n"
                                "                                                        border-radius: 15px;\n"
                                "                                                    ")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.white_color = QtWidgets.QPushButton(self.frame_2)
        self.white_color.setMinimumSize(QtCore.QSize(95, 35))
        self.white_color.setStyleSheet("QPushButton{\n"
                                       "                                                        border: none;\n"
                                       "                                                        margin: 0px;\n"
                                       "                                                        padding: 0px;\n"
                                       "                                                        background-color: rgb(255, 255, 255);\n"
                                       "                                                        border-radius: 15px;\n"
                                       "                                                        }\n"
                                       "                                                        QPushButton:hover{\n"
                                       "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                       "                                                        }\n"
                                       "                                                    ")
        self.white_color.setObjectName("white_color")
        self.horizontalLayout_3.addWidget(self.white_color)
        self.green_color = QtWidgets.QPushButton(self.frame_2)
        self.green_color.setMinimumSize(QtCore.QSize(95, 35))
        self.green_color.setStyleSheet("QPushButton{\n"
                                       "                                                        border: none;\n"
                                       "                                                        margin: 0px;\n"
                                       "                                                        padding: 0px;\n"
                                       "                                                        background-color: rgb(143, 240, 164);\n"
                                       "                                                        border-radius: 15px;\n"
                                       "                                                        }\n"
                                       "                                                        QPushButton:hover{\n"
                                       "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                       "                                                        }\n"
                                       "                                                    ")
        self.green_color.setObjectName("green_color")
        self.horizontalLayout_3.addWidget(self.green_color)
        self.red_color = QtWidgets.QPushButton(self.frame_2)
        self.red_color.setMinimumSize(QtCore.QSize(95, 35))
        self.red_color.setStyleSheet("QPushButton{\n"
                                     "                                                        border: none;\n"
                                     "                                                        margin: 0px;\n"
                                     "                                                        padding: 0px;\n"
                                     "                                                        background-color: rgb(246, 97, 81);\n"
                                     "                                                        border-radius: 15px;\n"
                                     "                                                        }\n"
                                     "                                                        QPushButton:hover{\n"
                                     "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                     "                                                        }\n"
                                     "                                                    ")
        self.red_color.setObjectName("red_color")
        self.horizontalLayout_3.addWidget(self.red_color)
        self.orange_color = QtWidgets.QPushButton(self.frame_2)
        self.orange_color.setMinimumSize(QtCore.QSize(95, 35))
        self.orange_color.setAutoFillBackground(False)
        self.orange_color.setStyleSheet("QPushButton{\n"
                                        "                                                        border: none;\n"
                                        "                                                        margin: 0px;\n"
                                        "                                                        padding: 0px;\n"
                                        "                                                        background-color: rgb(255, 190, 111);\n"
                                        "                                                        border-radius: 15px;\n"
                                        "                                                        }\n"
                                        "                                                        QPushButton:hover{\n"
                                        "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                        "                                                        }\n"
                                        "                                                    ")
        self.orange_color.setObjectName("orange_color")
        self.horizontalLayout_3.addWidget(self.orange_color)
        self.add_new_color = QtWidgets.QPushButton(self.frame_2)
        self.add_new_color.setMinimumSize(QtCore.QSize(42, 35))
        self.add_new_color.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_new_color.setStyleSheet("QPushButton{background-color: rgb(255, 255,\n"
                                         "                                                        255);\n"
                                         "                                                        border-radius: 15px;\n"
                                         "                                                        }\n"
                                         "                                                        QPushButton:hover{\n"
                                         "                                                        background-color: rgba(255, 255, 255, 70);\n"
                                         "                                                        }\n"
                                         "                                                    ")
        self.add_new_color.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/brush.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_new_color.setIcon(icon9)
        self.add_new_color.setObjectName("add_new_color")
        self.horizontalLayout_3.addWidget(self.add_new_color)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.verticalFrame)
        self.frame223 = QtWidgets.QFrame(self.centralwidget)
        self.frame223.setStyleSheet("border-radius:15px;")
        self.frame223.setObjectName("frame223")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame223)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame223)
        self.tabWidget.setStyleSheet("QTabWidget{\n"
                                     "                                            background-color: rgb(46, 194, 126);\n"
                                     "                                            }\n"
                                     "                                            QTabWidget::tab-bar {\n"
                                     "                                            alternate-background-color: rgb(224, 27, 36);\n"
                                     "                                            }\n"
                                     "                                            QTabBar::tab {\n"
                                     "                                            background-color: qlineargradient(x1:0.5, y1:1, x2:0.5, y2:0, stop:0\n"
                                     "                                            rgb(253,250,250), stop:0.2 rgb(253,250,250), stop:1 rgb(255,249,234));\n"
                                     "\n"
                                     "                                            border-bottom-left-radius: 7px;\n"
                                     "                                            border-bottom-right-radius: 7px;\n"
                                     "\n"
                                     "                                            min-width: 14ex;\n"
                                     "                                            padding: 5px;\n"
                                     "                                            }\n"
                                     "\n"
                                     "                                            QTabBar::tab:selected {\n"
                                     "                                            background-color: rgb(46, 194, 126);\n"
                                     "                                            color: rgb(255, 255, 255);\n"
                                     "                                            }\n"
                                     "\n"
                                     "                                            QTabBar::tab:!selected {\n"
                                     "                                            margin-top: 5px;\n"
                                     "                                            background: qlineargradient(x1:0.5, y1:1, x2:0.5, y2:0, stop:0\n"
                                     "                                            rgb(253,250,250), stop:0.2 rgb(253,250,250), stop:1 rgb(250,244,229));\n"
                                     "                                            color: rgb(93, 109, 109)\n"
                                     "                                            }\n"
                                     "                                        ")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.table_main = QtWidgets.QTableWidget(self.tab)
        self.table_main.setToolTipDuration(-1)
        self.table_main.setStatusTip("")
        self.table_main.setStyleSheet("QTableWidget{\n"
                                      "\n"
                                      "                                                            background-color: rgb(255, 255, 255);\n"
                                      "                                                            selection-background-color: rgb(227, 235, 231);\n"
                                      "                                                            }\n"
                                      "                                                        ")
        self.table_main.setGridStyle(QtCore.Qt.CustomDashLine)
        self.table_main.setObjectName("table_main")
        self.table_main.setColumnCount(0)
        self.table_main.setRowCount(0)
        self.table_main.horizontalHeader().setVisible(True)
        self.table_main.verticalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_6.addWidget(self.table_main)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.table_main_2 = QtWidgets.QTableWidget(self.tab_2)
        self.table_main_2.setToolTipDuration(-1)
        self.table_main_2.setStatusTip("")
        self.table_main_2.setStyleSheet("QTableWidget{\n"
                                        "                                                            background-color: rgb(255, 255, 255);\n"
                                        "                                                            border-color: rgb(255, 255, 255);\n"
                                        "                                                            selection-background-color: rgb(227, 235, 231);\n"
                                        "                                                            }\n"
                                        "                                                        ")
        self.table_main_2.setObjectName("table_main_2")
        self.table_main_2.setColumnCount(0)
        self.table_main_2.setRowCount(0)
        self.horizontalLayout_7.addWidget(self.table_main_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_4.addWidget(self.frame223)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1685, 30))
        self.menuBar.setMinimumSize(QtCore.QSize(0, 30))
        self.menuBar.setStyleSheet("QMenuBar::item:pressed {\n"
                                   "                    background-color: rgba(32, 114, 69, 60);\n"
                                   "                    }\n"
                                   "                    QMenuBar{\n"
                                   "                    background-color: rgb(64, 134, 92);\n"
                                   "                    color: rgb(255, 255, 255);\n"
                                   "                    }\n"
                                   "                ")
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.parametrs = QtWidgets.QMenu(self.menuBar)
        self.parametrs.setObjectName("parametrs")
        MainWindow.setMenuBar(self.menuBar)
        self.open_file = QtWidgets.QAction(MainWindow)
        self.open_file.setObjectName("open_file")
        self.save_file = QtWidgets.QAction(MainWindow)
        self.save_file.setObjectName("save_file")
        self.print = QtWidgets.QAction(MainWindow)
        self.print.setObjectName("print")
        self.save_as = QtWidgets.QAction(MainWindow)
        self.save_as.setObjectName("save_as")
        self.parameters = QtWidgets.QAction(MainWindow)
        self.parameters.setObjectName("parameters")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.open_last_file = QtWidgets.QAction(MainWindow)
        self.open_last_file.setObjectName("open_last_file")
        self.menu.addAction(self.open_file)
        self.menu.addAction(self.open_last_file)
        self.menu.addAction(self.save_file)
        self.menu.addAction(self.save_as)
        self.parametrs.addAction(self.parameters)
        self.parametrs.addAction(self.action_2)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.parametrs.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        colors = ["Чёрный", "Красный", "Жёлтый", "Синий", "Голубой", "Зелёный", "Фиолетовый", "Оранжевый", "Серый",
                  "Белый", "Лаймовый", "Пользовательский"]

        colors.sort()
        colors[0] = "Чёрный"
        colors[-1] = "Пользовательский"
        colors[-5] = "Белый"
        self.text_color.addItems(colors)
        self.text_size.setCurrentIndex(4)

        self.table_main.setColumnCount(50)
        self.table_main.setRowCount(1000)

        self.back.hide()
        self.forward.hide()

        self.bold_text.setShortcut("Ctrl+B")
        self.italic_text.setShortcut("Ctrl+I")
        self.underlined_text.setShortcut("Ctrl+U")
        self.text_size.setEditable(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.text_size.setItemText(0, _translate("MainWindow", "8"))
        self.text_size.setItemText(1, _translate("MainWindow", "9"))
        self.text_size.setItemText(2, _translate("MainWindow", "10"))
        self.text_size.setItemText(3, _translate("MainWindow", "11"))
        self.text_size.setItemText(4, _translate("MainWindow", "12"))
        self.text_size.setItemText(5, _translate("MainWindow", "14"))
        self.text_size.setItemText(6, _translate("MainWindow", "16"))
        self.text_size.setItemText(7, _translate("MainWindow", "18"))
        self.text_size.setItemText(8, _translate("MainWindow", "20"))
        self.text_size.setItemText(9, _translate("MainWindow", "22"))
        self.text_size.setItemText(10, _translate("MainWindow", "24"))
        self.text_size.setItemText(11, _translate("MainWindow", "26"))
        self.text_size.setItemText(12, _translate("MainWindow", "28"))
        self.text_size.setItemText(13, _translate("MainWindow", "36"))
        self.text_size.setItemText(14, _translate("MainWindow", "48"))
        self.text_size.setItemText(15, _translate("MainWindow", "72"))
        self.text_size.setItemText(16, _translate("MainWindow", "96"))
        self.text_size.setItemText(17, _translate("MainWindow", "Выбрать свой"))
        self.white_color.setText(_translate("MainWindow", "Без цвета"))
        self.green_color.setText(_translate("MainWindow", "Зелёный"))
        self.red_color.setText(_translate("MainWindow", "Красный"))
        self.orange_color.setText(_translate("MainWindow", "Оранжевый"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Лист 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Лист 2"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.parametrs.setTitle(_translate("MainWindow", "Параметры и выход"))
        self.open_file.setText(_translate("MainWindow", "Открыть файл"))
        self.save_file.setText(_translate("MainWindow", "Сохранить файл"))
        self.print.setText(_translate("MainWindow", "Печать"))
        self.save_as.setText(_translate("MainWindow", "Сохранить как"))
        self.parameters.setText(_translate("MainWindow", "Параметры"))
        self.parameters.setToolTip(_translate("MainWindow", "Параметры"))
        self.action_2.setText(_translate("MainWindow", "Выход в главное меню"))
        self.open_last_file.setText(_translate("MainWindow", "Открыть последний файл"))
