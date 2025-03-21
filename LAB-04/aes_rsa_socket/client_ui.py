import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
import threading
import socket
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad

class ChatClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initSocket()

    def initUI(self):
        self.setWindowTitle('Chat Client')
        self.setGeometry(100, 100, 600, 400)

        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def initSocket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12348))

        self.client_key = RSA.generate(2048)
        self.server_public_key = RSA.import_key(self.client_socket.recv(2048))
        self.client_socket.send(self.client_key.publickey().export_key(format='PEM'))
        encrypted_aes_key = self.client_socket.recv(2048)
        cipher_rsa = PKCS1_OAEP.new(self.client_key)
        self.aes_key = cipher_rsa.decrypt(encrypted_aes_key)

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def encrypt_message(self, key, message):
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
        return cipher.iv + ciphertext

    def decrypt_message(self, key, encrypted_message):
        iv = encrypted_message[:AES.block_size]
        ciphertext = encrypted_message[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_message.decode()

    def receive_messages(self):
        while True:
            encrypted_message = self.client_socket.recv(1024)
            decrypted_message = self.decrypt_message(self.aes_key, encrypted_message)
            self.text_area.append(f"Received: {decrypted_message}")

    def send_message(self):
        message = self.input_field.text()
        encrypted_message = self.encrypt_message(self.aes_key, message)
        self.client_socket.send(encrypted_message)
        self.text_area.append(f"Sent: {message}")
        self.input_field.clear()
        if message == "exit":
            self.client_socket.close()
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = ChatClient()
    client.show()
    sys.exit(app.exec_())
