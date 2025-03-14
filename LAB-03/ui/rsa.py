# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\Users\\TRUONG HUU\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\PyQt5\\Qt5\\plugins\\platforms'

class Ui_rsa(object):
    def setupUi(self, rsa):
        rsa.setObjectName("rsa")
        rsa.resize(1036, 385)
        self.centralwidget = QtWidgets.QWidget(rsa)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 60, 371, 87))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 170, 371, 87))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 280, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 20, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(610, 170, 371, 87))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 70, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(610, 60, 371, 87))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(850, 280, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 280, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        rsa.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(rsa)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 26))
        self.menubar.setObjectName("menubar")
        rsa.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(rsa)
        self.statusbar.setObjectName("statusbar")
        rsa.setStatusBar(self.statusbar)

        self.retranslateUi(rsa)
        QtCore.QMetaObject.connectSlotsByName(rsa)

    def retranslateUi(self, rsa):
        _translate = QtCore.QCoreApplication.translate
        rsa.setWindowTitle(_translate("rsa", "RSA Cipher"))
        self.label_4.setText(_translate("rsa", "Cipher Text:"))
        self.label.setText(_translate("rsa", "RSA CIPHER"))
        self.label_2.setText(_translate("rsa", "Plain Text:"))
        self.pushButton.setText(_translate("rsa", "Encrypt"))
        self.pushButton_2.setText(_translate("rsa", "Decrypt"))
        self.pushButton_3.setText(_translate("rsa", "Generate Keys"))
        self.label_3.setText(_translate("rsa", "Information:"))
        self.label_5.setText(_translate("rsa", "Signature:"))
        self.pushButton_4.setText(_translate("rsa", "Verify"))
        self.pushButton_5.setText(_translate("rsa", "Sign"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rsa = QtWidgets.QMainWindow()
    ui = Ui_rsa()
    ui.setupUi(rsa)
    rsa.show()
    sys.exit(app.exec_())
