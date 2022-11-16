# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Parabola Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize


class Ui_QDialog(object):
    def setupUi(self, QDialog):
        QDialog.setObjectName("QDialog")
        QDialog.setWindowModality(QtCore.Qt.WindowModal)
        QDialog.resize(712, 521)
        QDialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/myICO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QDialog.setWindowIcon(icon)
        QDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        QDialog.setStyleSheet("QMainWindow{\n"
"background-color: rgb(37, 37, 56);\n"
"}\n"
"QDialog{\n"
"background-color: rgb(37,37,56)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(56, 0, 84)\n"
"}")
        self.Main_String = QtWidgets.QLineEdit(QDialog)
        self.Main_String.setGeometry(QtCore.QRect(30, 30, 481, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Main_String.setFont(font)
        self.Main_String.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Main_String.setStyleSheet("\n"
"background-color:rgb(191, 180, 255);")
        self.Main_String.setInputMask("")
        self.Main_String.setText("")
        self.Main_String.setMaxLength(30)
        self.Main_String.setObjectName("Main_String")
        self.Button_3 = QtWidgets.QPushButton(QDialog)
        self.Button_3.setEnabled(True)
        self.Button_3.setGeometry(QtCore.QRect(320, 120, 100, 71))
        self.Button_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_3.setObjectName("Button_3")
        self.Button_6 = QtWidgets.QPushButton(QDialog)
        self.Button_6.setGeometry(QtCore.QRect(320, 210, 101, 71))
        self.Button_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_6.setObjectName("Button_6")
        self.Button_9 = QtWidgets.QPushButton(QDialog)
        self.Button_9.setGeometry(QtCore.QRect(320, 300, 100, 71))
        self.Button_9.setAutoFillBackground(False)
        self.Button_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_9.setObjectName("Button_9")
        self.Button_5 = QtWidgets.QPushButton(QDialog)
        self.Button_5.setGeometry(QtCore.QRect(180, 210, 100, 71))
        self.Button_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_5.setObjectName("Button_5")
        self.Button_2 = QtWidgets.QPushButton(QDialog)
        self.Button_2.setGeometry(QtCore.QRect(180, 119, 100, 71))
        self.Button_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_2.setObjectName("Button_2")
        self.Button_8 = QtWidgets.QPushButton(QDialog)
        self.Button_8.setGeometry(QtCore.QRect(180, 300, 100, 71))
        self.Button_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_8.setObjectName("Button_8")
        self.Button_0 = QtWidgets.QPushButton(QDialog)
        self.Button_0.setGeometry(QtCore.QRect(180, 390, 100, 71))
        self.Button_0.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_0.setObjectName("Button_0")
        self.Button_1 = QtWidgets.QPushButton(QDialog)
        self.Button_1.setGeometry(QtCore.QRect(40, 120, 100, 71))
        self.Button_1.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_1.setObjectName("Button_1")
        self.Button_4 = QtWidgets.QPushButton(QDialog)
        self.Button_4.setGeometry(QtCore.QRect(40, 210, 100, 71))
        self.Button_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_4.setObjectName("Button_4")
        self.Button_7 = QtWidgets.QPushButton(QDialog)
        self.Button_7.setGeometry(QtCore.QRect(40, 300, 100, 71))
        self.Button_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Button_7.setObjectName("Button_7")
        self.Dot_Button = QtWidgets.QPushButton(QDialog)
        self.Dot_Button.setGeometry(QtCore.QRect(40, 390, 100, 71))
        self.Dot_Button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(108, 26, 164);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Dot_Button.setObjectName("Dot_Button")
        self.button_right = QtWidgets.QPushButton(QDialog)
        self.button_right.setGeometry(QtCore.QRect(380, 390, 61, 71))
        self.button_right.setAutoFillBackground(False)
        self.button_right.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(108, 26, 164);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.button_right.setObjectName("button_right")
        self.plus_button = QtWidgets.QPushButton(QDialog)
        self.plus_button.setGeometry(QtCore.QRect(480, 250, 81, 51))
        self.plus_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(183,66,139);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.plus_button.setObjectName("plus_button")
        self.minus_button = QtWidgets.QPushButton(QDialog)
        self.minus_button.setGeometry(QtCore.QRect(580, 250, 81, 51))
        self.minus_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(183,66,139);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.minus_button.setObjectName("minus_button")
        self.mult_button = QtWidgets.QPushButton(QDialog)
        self.mult_button.setGeometry(QtCore.QRect(480, 320, 81, 51))
        self.mult_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(183,66,139);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.mult_button.setObjectName("mult_button")
        self.division_button = QtWidgets.QPushButton(QDialog)
        self.division_button.setGeometry(QtCore.QRect(580, 320, 81, 51))
        self.division_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(183,66,139);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.division_button.setObjectName("division_button")
        self.factorial_button = QtWidgets.QPushButton(QDialog)
        self.factorial_button.setGeometry(QtCore.QRect(480, 390, 81, 51))
        self.factorial_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(183,66,139);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.factorial_button.setObjectName("factorial_button")
        self.exp_button = QtWidgets.QPushButton(QDialog)
        self.exp_button.setGeometry(QtCore.QRect(580, 390, 81, 51))
        self.exp_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(183,66,139);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.exp_button.setObjectName("exp_button")
        self.history = QtWidgets.QPushButton(QDialog)
        self.history.setGeometry(QtCore.QRect(480, 180, 81, 51))
        self.history.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(108, 26, 164);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.history.setObjectName("history")
        self.instructions = QtWidgets.QPushButton(QDialog)
        self.instructions.setGeometry(QtCore.QRect(580, 180, 81, 51))
        self.instructions.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(108, 26, 164);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.instructions.setObjectName("instructions")
        self.Enter = QtWidgets.QPushButton(QDialog)
        self.Enter.setGeometry(QtCore.QRect(540, 20, 151, 61))
        self.Enter.setStyleSheet("\n"
"\n"
"\n"
"border-radius: 10px;font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(73,89,255);\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"")
        self.Enter.setText("Enter")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Desktop/Icons/BackspaceIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Enter.setIcon(icon1)
        self.Enter.setIconSize(QtCore.QSize(32, 32))
        self.Enter.setObjectName("Enter")
        self.Backspace = QtWidgets.QPushButton(QDialog)
        self.Backspace.setGeometry(QtCore.QRect(480, 100, 81, 61))
        self.Backspace.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(41, 14, 135);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.Backspace.setText("Backspace")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Desktop/Icons/BackspaceIcon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Backspace.setIcon(icon2)
        self.Backspace.setIconSize(QtCore.QSize(32, 32))
        self.Backspace.setObjectName("Backspace")
        self.button_left = QtWidgets.QPushButton(QDialog)
        self.button_left.setGeometry(QtCore.QRect(300, 390, 61, 71))
        self.button_left.setAutoFillBackground(False)
        self.button_left.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(108, 26, 164);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.button_left.setObjectName("button_left")
        self.erase_button = QtWidgets.QPushButton(QDialog)
        self.erase_button.setGeometry(QtCore.QRect(580, 100, 81, 61))
        self.erase_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(41,14,135);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.erase_button.setText("Erase")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Desktop/Coding/GUI/icons8-erase-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.erase_button.setIcon(icon3)
        self.erase_button.setIconSize(QtCore.QSize(32, 32))
        self.erase_button.setObjectName("erase_button")
        self.mult_button_2 = QtWidgets.QPushButton(QDialog)
        self.mult_button_2.setGeometry(QtCore.QRect(480, 450, 181, 41))
        self.mult_button_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\"; \n"
"background-color:rgb(183,66,139);\n"
"border-style: outset;\n"
"border-radius: 10px;")
        self.mult_button_2.setObjectName("mult_button_2")

        self.retranslateUi(QDialog)
        QtCore.QMetaObject.connectSlotsByName(QDialog)

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("QDialog", "L-D Calculator"))
        self.Main_String.setPlaceholderText(_translate("QDialog", "Calculate here: "))
        self.Button_3.setText(_translate("QDialog", "3"))
        self.Button_6.setText(_translate("QDialog", "6"))
        self.Button_9.setText(_translate("QDialog", "9"))
        self.Button_5.setText(_translate("QDialog", "5"))
        self.Button_2.setText(_translate("QDialog", "2"))
        self.Button_8.setText(_translate("QDialog", "8"))
        self.Button_0.setText(_translate("QDialog", "0"))
        self.Button_1.setText(_translate("QDialog", "1"))
        self.Button_4.setText(_translate("QDialog", "4"))
        self.Button_7.setText(_translate("QDialog", "7"))
        self.Dot_Button.setText(_translate("QDialog", "•"))
        self.button_right.setText(_translate("QDialog", ")"))
        self.plus_button.setText(_translate("QDialog", "+"))
        self.minus_button.setText(_translate("QDialog", "-"))
        self.mult_button.setText(_translate("QDialog", "*"))
        self.division_button.setText(_translate("QDialog", ":"))
        self.factorial_button.setText(_translate("QDialog", "!"))
        self.exp_button.setText(_translate("QDialog", "^"))
        self.history.setText(_translate("QDialog", "𝓗"))
        self.instructions.setText(_translate("QDialog", "𝐼"))
        self.button_left.setText(_translate("QDialog", "( "))
        self.mult_button_2.setText(_translate("QDialog", "√"))

