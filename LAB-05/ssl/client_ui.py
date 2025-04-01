# client_ui.py
import socket
import ssl
import threading
import tkinter as tk
from tkinter import ttk, messagebox

class SSLChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("SSL Chat Client")
        self.root.geometry("500x500")
        
        # Xử lý khi đóng cửa sổ
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        
        # Tạo frame chính
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tiêu đề
        ttk.Label(self.main_frame, text="SSL Chat Client", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Khu vực hiển thị tin nhắn
        ttk.Label(self.main_frame, text="Tin nhắn nhận được:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.chat_area = tk.Text(self.main_frame, height=15, width=50, state='disabled')
        self.chat_area.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Khu vực nhập tin nhắn
        ttk.Label(self.main_frame, text="Nhập tin nhắn:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.message_entry = tk.Text(self.main_frame, height=3, width=50)
        self.message_entry.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Nút gửi và thoát
        ttk.Button(self.main_frame, text="Gửi", command=self.send_message).grid(row=5, column=0, padx=5, pady=10)
        ttk.Button(self.main_frame, text="Thoát", command=self.quit).grid(row=5, column=1, padx=5, pady=10)
        
        # Thông tin server
        self.server_address = ('localhost', 12345)
        self.ssl_socket = None
        self.running = True
        
        # Kết nối đến server khi khởi động
        self.connect_to_server()

    def connect_to_server(self):
        try:
            # Tạo socket client
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Tạo SSL context
            context = ssl.SSLContext(ssl.PROTOCOL_TLS)
            context.verify_mode = ssl.CERT_NONE  # Không yêu cầu chứng chỉ từ server
            context.check_hostname = False       # Không kiểm tra hostname
            
            # Thiết lập kết nối SSL
            self.ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
            self.ssl_socket.connect(self.server_address)
            
            self.append_message("Đã kết nối đến server!")
            
            # Bắt đầu luồng nhận dữ liệu
            receive_thread = threading.Thread(target=self.receive_data)
            receive_thread.daemon = True
            receive_thread.start()
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể kết nối đến server: {e}")
            self.root.quit()

    def receive_data(self):
        try:
            while self.running:
                data = self.ssl_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                self.append_message(f"Nhận: {message}")
        except Exception as e:
            if self.running:
                self.append_message(f"Lỗi: {e}")
        finally:
            if self.running:
                self.append_message("Kết nối đã đóng.")
            self.ssl_socket.close()

    def send_message(self):
        try:
            message = self.message_entry.get("1.0", tk.END).strip()
            if not message:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập tin nhắn!")
                return
                
            self.ssl_socket.send(message.encode('utf-8'))
            self.append_message(f"Gửi: {message}")
            self.message_entry.delete("1.0", tk.END)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể gửi tin nhắn: {e}")

    def append_message(self, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.see(tk.END)

    def quit(self):
        self.running = False
        if self.ssl_socket:
            self.ssl_socket.close()
        self.root.quit()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = SSLChatClient(root)
    root.mainloop()

if __name__ == "__main__":
    main()