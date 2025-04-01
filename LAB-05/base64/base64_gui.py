import tkinter as tk
from tkinter import ttk, messagebox
import base64

class Base64EncoderDecoder:
    def __init__(self, root):
        self.root = root
        self.root.title("Base64 Encoder/Decoder")
        self.root.geometry("500x400")
        
        # Tạo frame chính
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tiêu đề
        ttk.Label(self.main_frame, text="Base64 Encoder/Decoder", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Khu vực nhập văn bản gốc
        ttk.Label(self.main_frame, text="Nhập văn bản gốc:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.input_text = tk.Text(self.main_frame, height=5, width=50)
        self.input_text.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Nút mã hóa và giải mã
        ttk.Button(self.main_frame, text="Mã hóa", command=self.encode_text).grid(row=3, column=0, padx=5, pady=10)
        ttk.Button(self.main_frame, text="Giải mã", command=self.decode_text).grid(row=3, column=1, padx=5, pady=10)
        
        # Khu vực hiển thị kết quả
        ttk.Label(self.main_frame, text="Kết quả:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.output_text = tk.Text(self.main_frame, height=5, width=50)
        self.output_text.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Nút lưu file và xóa
        ttk.Button(self.main_frame, text="Lưu vào file", command=self.save_to_file).grid(row=6, column=0, padx=5, pady=10)
        ttk.Button(self.main_frame, text="Xóa tất cả", command=self.clear_all).grid(row=6, column=1, padx=5, pady=10)

    def encode_text(self):
        try:
            input_string = self.input_text.get("1.0", tk.END).strip()
            if not input_string:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản cần mã hóa!")
                return
                
            encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
            encoded_string = encoded_bytes.decode("utf-8")
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", encoded_string)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi mã hóa: {e}")

    def decode_text(self):
        try:
            encoded_string = self.input_text.get("1.0", tk.END).strip()
            if not encoded_string:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản cần giải mã!")
                return
                
            decoded_bytes = base64.b64decode(encoded_string)
            decoded_string = decoded_bytes.decode("utf-8")
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", decoded_string)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi giải mã: {e}")

    def save_to_file(self):
        try:
            content = self.output_text.get("1.0", tk.END).strip()
            if not content:
                messagebox.showwarning("Cảnh báo", "Không có nội dung để lưu!")
                return
                
            with open("data.txt", "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Thành công", "Đã lưu vào file data.txt")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu file: {e}")

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = Base64EncoderDecoder(root)
    root.mainloop()

if __name__ == "__main__":
    main()