# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:/Users/HP/AppData/Local/Programs/Python/Python39/Lib/site-packages/PyQt5/Qt/plugins/platforms'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_Generatekeys = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Generatekeys.setGeometry(QtCore.QRect(480, 70, 101, 23))
        self.pushButton_Generatekeys.setObjectName("pushButton_Generatekeys")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 140, 61, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton_Sign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sign.setGeometry(QtCore.QRect(210, 360, 75, 23))
        self.pushButton_Sign.setObjectName("pushButton_Sign")
        self.pushButton_Verify = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Verify.setGeometry(QtCore.QRect(420, 360, 75, 23))
        self.pushButton_Verify.setObjectName("pushButton_Verify")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 250, 61, 20))
        self.label_5.setObjectName("label_5")
        self.textEdit_Information = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Information.setGeometry(QtCore.QRect(200, 130, 391, 71))
        self.textEdit_Information.setObjectName("textEdit_Information")
        self.textEdit_Signature = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Signature.setGeometry(QtCore.QRect(200, 230, 391, 71))
        self.textEdit_Signature.setObjectName("textEdit_Signature")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ECC CIPHER"))
        self.pushButton_Generatekeys.setText(_translate("MainWindow", "Generate Keys"))
        self.label_4.setText(_translate("MainWindow", "Information:"))
        self.pushButton_Sign.setText(_translate("MainWindow", "Sign"))
        self.pushButton_Verify.setText(_translate("MainWindow", "Verify"))
        self.label_5.setText(_translate("MainWindow", "Signature:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
