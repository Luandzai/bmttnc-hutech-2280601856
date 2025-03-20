import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối các nút với phương thức tương ứng
        self.ui.pushButton_Generatekeys.clicked.connect(self.call_api_gen_keys)  # Generate Keys
        self.ui.pushButton_Sign.clicked.connect(self.call_api_sign)  # Sign
        self.ui.pushButton_Verify.clicked.connect(self.call_api_verify)  # Verify

    def call_api_gen_keys(self):
        print("Generate Keys button clicked!")  # Debug
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            print(f"API Response Status Code: {response.status_code}")  # Debug
            if response.status_code == 200:
                data = response.json()
                print(f"API Response: {data}")  # Debug
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print(f"Error: {response.status_code}, {response.text}")  # Debug
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")  # Debug

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        payload = {
            "message": self.ui.textEdit_Information.toPlainText(),  # Information textEdit
        }
        try:
            response = requests.post(url, json=payload)
            print(f"Sign API Response Status Code: {response.status_code}")  # Debug
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_Signature.setText(data["signature"])  # Signature textEdit
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print(f"Error: {response.status_code}, {response.text}")  # Debug
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        payload = {
            "message": self.ui.textEdit_Information.toPlainText(),  # Information textEdit
            "signature": self.ui.textEdit_Signature.toPlainText()  # Signature textEdit
        }
        try:
            response = requests.post(url, json=payload)
            print(f"Verify API Response Status Code: {response.status_code}")  # Debug
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                if data["is_verified"]:
                    msg.setText("Verified Successfully")
                else:
                    msg.setText("Verified Failed")
                msg.exec_()
            else:
                print(f"Error: {response.status_code}, {response.text}")  # Debug
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
