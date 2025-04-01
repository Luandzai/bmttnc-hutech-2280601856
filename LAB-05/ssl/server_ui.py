# server_ui.py
import socket
import ssl
import threading
import tkinter as tk
from tkinter import ttk, messagebox

class SSLChatServer:
    def __init__(self, root):
        self.root = root
        self.root.title("SSL Chat Server")
        self.root.geometry("500x500")
        
        # Xử lý khi đóng cửa sổ
        self.root.protocol("WM_DELETE_WINDOW", self.stop_server)
        
        # Tạo frame chính
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tiêu đề
        ttk.Label(self.main_frame, text="SSL Chat Server", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Khu vực hiển thị trạng thái
        ttk.Label(self.main_frame, text="Trạng thái server:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.status_area = tk.Text(self.main_frame, height=10, width=50, state='disabled')
        self.status_area.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Khu vực hiển thị danh sách client
        ttk.Label(self.main_frame, text="Client đang kết nối:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.client_list = tk.Text(self.main_frame, height=5, width=50, state='disabled')
        self.client_list.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Khu vực hiển thị tin nhắn
        ttk.Label(self.main_frame, text="Tin nhắn nhận được:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.message_area = tk.Text(self.main_frame, height=5, width=50, state='disabled')
        self.message_area.grid(row=6, column=0, columnspan=2, pady=5)
        
        # Nút dừng server
        ttk.Button(self.main_frame, text="Dừng Server", command=self.stop_server).grid(row=7, column=0, columnspan=2, pady=10)
        
        # Thông tin server
        self.server_address = ('localhost', 12345)
        self.clients = []  # Danh sách các client đã kết nối
        self.server_socket = None
        self.running = True
        
        # Khởi động server
        self.start_server()

    def start_server(self):
        try:
            # Tạo socket server
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Cho phép tái sử dụng địa chỉ
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(self.server_address)
            self.server_socket.listen(5)
            
            self.append_status("Server đang chờ kết nối...")
            
            # Bắt đầu luồng chấp nhận kết nối
            accept_thread = threading.Thread(target=self.accept_connections)
            accept_thread.daemon = True
            accept_thread.start()
            
        except Exception as e:
            self.append_status(f"Lỗi khi khởi động server: {e}")
            messagebox.showerror("Lỗi", f"Không thể khởi động server: {e}")

    def accept_connections(self):
        while self.running:
            try:
                client_socket, client_address = self.server_socket.accept()
                
                # Tạo SSL context
                context = ssl.SSLContext(ssl.PROTOCOL_TLS)
                context.load_cert_chain(certfile="./certificates/server-cert.crt", keyfile="./certificates/server-key.key")
                
                # Thiết lập kết nối SSL
                ssl_socket = context.wrap_socket(client_socket, server_side=True)
                
                # Thêm client vào danh sách
                self.clients.append(ssl_socket)
                self.append_status(f"Đã kết nối với: {ssl_socket.getpeername()}")
                self.update_client_list()
                
                # Bắt đầu luồng xử lý cho client
                client_thread = threading.Thread(target=self.handle_client, args=(ssl_socket,))
                client_thread.daemon = True
                client_thread.start()
                
            except Exception as e:
                if self.running:
                    self.append_status(f"Lỗi khi chấp nhận kết nối: {e}")

    def handle_client(self, client_socket):
        try:
            while self.running:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                self.append_message(f"Nhận từ {client_socket.getpeername()}: {message}")
                
                # Gửi dữ liệu đến tất cả các client khác
                for client in self.clients:
                    if client != client_socket:
                        try:
                            client.send(data)
                        except:
                            self.clients.remove(client)
                            self.append_status(f"Đã ngắt kết nối: {client.getpeername()}")
                            self.update_client_list()
                            client.close()
                            
        except Exception as e:
            if self.running:
                self.append_status(f"Lỗi với client {client_socket.getpeername()}: {e}")
        finally:
            if client_socket in self.clients:
                self.clients.remove(client_socket)
                self.append_status(f"Đã ngắt kết nối: {client_socket.getpeername()}")
                self.update_client_list()
                client_socket.close()

    def append_status(self, message):
        self.status_area.configure(state='normal')
        self.status_area.insert(tk.END, message + "\n")
        self.status_area.configure(state='disabled')
        self.status_area.see(tk.END)

    def append_message(self, message):
        self.message_area.configure(state='normal')
        self.message_area.insert(tk.END, message + "\n")
        self.message_area.configure(state='disabled')
        self.message_area.see(tk.END)

    def update_client_list(self):
        self.client_list.configure(state='normal')
        self.client_list.delete("1.0", tk.END)
        for client in self.clients:
            self.client_list.insert(tk.END, f"{client.getpeername()}\n")
        self.client_list.configure(state='disabled')

    def stop_server(self):
        self.running = False
        for client in self.clients:
            client.close()
        if self.server_socket:
            self.server_socket.close()
        self.append_status("Server đã dừng.")
        self.root.quit()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = SSLChatServer(root)
    root.mainloop()

if __name__ == "__main__":
    main()