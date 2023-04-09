from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(564, 262)
        self.ok_and_cancel = QtWidgets.QDialogButtonBox(Dialog)
        self.ok_and_cancel.setGeometry(QtCore.QRect(200, 220, 341, 32))
        self.ok_and_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_and_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_and_cancel.setObjectName("ok_and_cancel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.label.setObjectName("label")
        self.encoding = QtWidgets.QComboBox(Dialog)
        self.encoding.setGeometry(QtCore.QRect(20, 50, 321, 31))
        self.encoding.setObjectName("encoding")
        self.encoding.addItem("")
        self.encoding.addItem("")
        self.encoding.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 141, 31))
        self.label_2.setObjectName("label_2")
        self.separator = QtWidgets.QComboBox(Dialog)
        self.separator.setGeometry(QtCore.QRect(20, 140, 321, 31))
        self.separator.setObjectName("separator")
        self.separator.addItem("")
        self.separator.addItem("")
        self.separator.addItem("")
        self.separator.addItem("")
        self.separator.addItem("")

        self.retranslateUi(Dialog)
        self.ok_and_cancel.accepted.connect(Dialog.accept)  # type: ignore
        self.ok_and_cancel.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Выберите параметры csv"))
        self.label.setText(_translate("Dialog", "Кодировка"))
        self.encoding.setItemText(0, _translate("Dialog", "UTF-8 (по умолчанию)"))
        self.encoding.setItemText(1, _translate("Dialog", "ASCII"))
        self.encoding.setItemText(2, _translate("Dialog", "Windows-1251 (для кириллических алфавитов)"))
        self.label_2.setText(_translate("Dialog", "Разделитель"))
        self.separator.setItemText(0, _translate("Dialog", "Точка с запятой"))
        self.separator.setItemText(1, _translate("Dialog", "Двоеточие"))
        self.separator.setItemText(2, _translate("Dialog", "Запятая"))
        self.separator.setItemText(3, _translate("Dialog", "Табуляция"))
        self.separator.setItemText(4, _translate("Dialog", "Пробел"))
