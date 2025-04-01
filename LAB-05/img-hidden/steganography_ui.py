# steganography_ui.py
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image

class SteganographyUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("500x500")
        
        # Tạo frame chính
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tiêu đề
        ttk.Label(self.main_frame, text="Steganography Tool", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Khu vực mã hóa
        ttk.Label(self.main_frame, text="Mã hóa thông điệp:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Chọn file ảnh gốc
        ttk.Label(self.main_frame, text="Chọn ảnh gốc:").grid(row=2, column=0, sticky=tk.W)
        self.image_path_entry = ttk.Entry(self.main_frame, width=40)
        self.image_path_entry.grid(row=2, column=1, pady=5)
        ttk.Button(self.main_frame, text="Chọn file", command=self.select_image).grid(row=2, column=2, padx=5)
        
        # Nhập thông điệp
        ttk.Label(self.main_frame, text="Thông điệp:").grid(row=3, column=0, sticky=tk.W)
        self.message_entry = tk.Text(self.main_frame, height=3, width=40)
        self.message_entry.grid(row=3, column=1, columnspan=2, pady=5)
        
        # Nút mã hóa
        ttk.Button(self.main_frame, text="Mã hóa", command=self.encode_message).grid(row=4, column=0, columnspan=3, pady=10)
        
        # Khu vực giải mã
        ttk.Label(self.main_frame, text="Giải mã thông điệp:").grid(row=5, column=0, sticky=tk.W, pady=5)
        
        # Chọn file ảnh đã mã hóa
        ttk.Label(self.main_frame, text="Chọn ảnh mã hóa:").grid(row=6, column=0, sticky=tk.W)
        self.encoded_image_path_entry = ttk.Entry(self.main_frame, width=40)
        self.encoded_image_path_entry.grid(row=6, column=1, pady=5)
        ttk.Button(self.main_frame, text="Chọn file", command=self.select_encoded_image).grid(row=6, column=2, padx=5)
        
        # Nút giải mã
        ttk.Button(self.main_frame, text="Giải mã", command=self.decode_message).grid(row=7, column=0, columnspan=3, pady=10)
        
        # Khu vực hiển thị thông điệp giải mã
        ttk.Label(self.main_frame, text="Thông điệp giải mã:").grid(row=8, column=0, sticky=tk.W, pady=5)
        self.decoded_message_area = tk.Text(self.main_frame, height=5, width=50, state='disabled')
        self.decoded_message_area.grid(row=9, column=0, columnspan=3, pady=5)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.image_path_entry.delete(0, tk.END)
            self.image_path_entry.insert(0, file_path)

    def select_encoded_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.encoded_image_path_entry.delete(0, tk.END)
            self.encoded_image_path_entry.insert(0, file_path)

    def encode_message(self):
        image_path = self.image_path_entry.get().strip()
        message = self.message_entry.get("1.0", tk.END).strip()
        
        # Kiểm tra input
        if not image_path:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn file ảnh gốc!")
            return
        if not message:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập thông điệp cần mã hóa!")
            return
        
        try:
            # Mã hóa thông điệp vào ảnh
            img = Image.open(image_path)
            width, height = img.size
            pixel_index = 0
            binary_message = ''.join(format(ord(char), '08b') for char in message)
            binary_message += '1111111111111110'  # Dấu đầu kết thúc thông điệp

            data_index = 0
            for row in range(height):
                for col in range(width):
                    pixel = list(img.getpixel((col, row)))
                    
                    for color_channel in range(3):
                        if data_index < len(binary_message):
                            pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                            data_index += 1

                    img.putpixel((col, row), tuple(pixel))

                    if data_index >= len(binary_message):
                        break

            encoded_image_path = 'encoded_image.png'
            img.save(encoded_image_path)
            messagebox.showinfo("Thành công", f"Mã hóa hoàn tất! Ảnh đã mã hóa được lưu tại: {encoded_image_path}")
            
            # Xóa ô nhập
            self.message_entry.delete("1.0", tk.END)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể mã hóa: {e}")

    def decode_message(self):
        encoded_image_path = self.encoded_image_path_entry.get().strip()
        
        # Kiểm tra input
        if not encoded_image_path:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn file ảnh đã mã hóa!")
            return
        
        try:
            # Giải mã thông điệp từ ảnh
            img = Image.open(encoded_image_path)
            width, height = img.size
            binary_message = ""

            for row in range(height):
                for col in range(width):
                    pixel = img.getpixel((col, row))
                    for color_channel in range(3):
                        binary_message += format(pixel[color_channel], '08b')[-1]

            message = ""
            for i in range(0, len(binary_message), 8):
                byte = binary_message[i:i+8]
                if byte == '11111111':  # Kiểm tra dấu kết thúc thông điệp
                    break
                char = chr(int(byte, 2))
                message += char

            # Hiển thị thông điệp giải mã
            self.decoded_message_area.configure(state='normal')
            self.decoded_message_area.delete("1.0", tk.END)
            self.decoded_message_area.insert(tk.END, message)
            self.decoded_message_area.configure(state='disabled')
            
            messagebox.showinfo("Thành công", "Giải mã hoàn tất! Thông điệp đã được hiển thị.")
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể giải mã: {e}")

def main():
    root = tk.Tk()
    app = SteganographyUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()