import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.transposition import Ui_transposition  # Corrected import
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_transposition()  # Corrected class name
        self.ui.setupUi(self)
        self.ui.pushButton_encrypt.clicked.connect(self.call_api_encrypt)  # Updated button name
        self.ui.pushButton_decrypt.clicked.connect(self.call_api_decrypt)  # Updated button name

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/transposition/encrypt"
        payload = {
            "plain_text": self.ui.textEdit_plain.toPlainText(),  # Updated text edit name
            "key": self.ui.lineEdit_key.text()  # Updated line edit name
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_cipher.setText(data["encrypted_text"])  # Updated text edit name
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/transposition/decrypt"
        payload = {
            "cipher_text": self.ui.textEdit_cipher.toPlainText(),  # Updated text edit name
            "key": self.ui.lineEdit_key.text()  # Updated line edit name
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_plain.setText(data["decrypted_text"])  # Updated text edit name
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
