import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Cập nhật tên button
        self.ui.pushButton_Encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_Decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.textEdit_Plaintext.toPlainText(),  # Cập nhật tên textEdit
            "key": self.ui.textEdit_Key.toPlainText()  # Cập nhật tên textEdit cho key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_Ciphertext.setText(data["encrypted_message"])  # Cập nhật textEdit cho ciphertext
                self.show_message("Encrypted Successfully")
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.textEdit_Ciphertext.toPlainText(),  # Cập nhật textEdit cho ciphertext
            "key": self.ui.textEdit_Key.toPlainText()  # Cập nhật textEdit cho key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_Plaintext.setText(data["decrypted_message"])  # Cập nhật textEdit cho plaintext
                self.show_message("Decrypted Successfully")
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def show_message(self, text):
        """Hiển thị thông báo."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
