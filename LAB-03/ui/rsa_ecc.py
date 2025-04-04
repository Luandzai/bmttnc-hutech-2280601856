# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa_ecc.ui'
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
        MainWindow.resize(1037, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_rsa_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rsa_gen_keys.setGeometry(QtCore.QRect(500, 20, 93, 28))
        self.pushButton_rsa_gen_keys.setObjectName("pushButton_rsa_gen_keys")
        self.pushButton_ecc_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ecc_gen_keys.setGeometry(QtCore.QRect(670, 20, 93, 28))
        self.pushButton_ecc_gen_keys.setObjectName("pushButton_ecc_gen_keys")
        self.pushButton_rsa_sign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rsa_sign.setGeometry(QtCore.QRect(170, 280, 93, 28))
        self.pushButton_rsa_sign.setObjectName("pushButton_rsa_sign")
        self.pushButton_rsa_verify = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rsa_verify.setGeometry(QtCore.QRect(350, 280, 93, 28))
        self.pushButton_rsa_verify.setObjectName("pushButton_rsa_verify")
        self.pushButton_ecc_sign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ecc_sign.setGeometry(QtCore.QRect(670, 280, 93, 28))
        self.pushButton_ecc_sign.setObjectName("pushButton_ecc_sign")
        self.pushButton_ecc_verify = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ecc_verify.setGeometry(QtCore.QRect(850, 280, 93, 28))
        self.pushButton_ecc_verify.setObjectName("pushButton_ecc_verify")
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
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(610, 170, 371, 87))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(110, 170, 371, 87))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(110, 60, 371, 87))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA_ECC Cipher"))
        self.pushButton_rsa_gen_keys.setText(_translate("MainWindow", "Generate RSA Keys"))
        self.pushButton_ecc_gen_keys.setText(_translate("MainWindow", "Generate ECC Keys"))
        self.pushButton_rsa_sign.setText(_translate("MainWindow", "Sign RSA"))
        self.pushButton_rsa_verify.setText(_translate("MainWindow", "Verify RSA"))
        self.pushButton_ecc_sign.setText(_translate("MainWindow", "Sign ECC"))
        self.pushButton_ecc_verify.setText(_translate("MainWindow", "Verify ECC"))
        self.label_3.setText(_translate("MainWindow", "Information:"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_5.setText(_translate("MainWindow", "Signature:"))
        self.label_6.setText(_translate("MainWindow", "Signature:"))
        self.label_4.setText(_translate("MainWindow", "Information:"))
        self.label_2.setText(_translate("MainWindow", "ECC CIPHER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
