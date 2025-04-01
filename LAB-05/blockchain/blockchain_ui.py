# blockchain_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
from blockchain import Blockchain

class BlockchainUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blockchain Simulator")
        self.root.geometry("600x600")
        
        # Khởi tạo blockchain
        self.blockchain = Blockchain()
        
        # Tạo frame chính
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tiêu đề
        ttk.Label(self.main_frame, text="Blockchain Simulator", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Khu vực nhập giao dịch
        ttk.Label(self.main_frame, text="Thêm giao dịch:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Nhập Sender
        ttk.Label(self.main_frame, text="Sender:").grid(row=2, column=0, sticky=tk.W)
        self.sender_entry = ttk.Entry(self.main_frame, width=20)
        self.sender_entry.grid(row=2, column=1, pady=5)
        
        # Nhập Receiver
        ttk.Label(self.main_frame, text="Receiver:").grid(row=3, column=0, sticky=tk.W)
        self.receiver_entry = ttk.Entry(self.main_frame, width=20)
        self.receiver_entry.grid(row=3, column=1, pady=5)
        
        # Nhập Amount
        ttk.Label(self.main_frame, text="Amount:").grid(row=4, column=0, sticky=tk.W)
        self.amount_entry = ttk.Entry(self.main_frame, width=20)
        self.amount_entry.grid(row=4, column=1, pady=5)
        
        # Nút thêm giao dịch
        ttk.Button(self.main_frame, text="Thêm giao dịch", command=self.add_transaction).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Nút khai thác khối
        ttk.Button(self.main_frame, text="Khai thác khối mới", command=self.mine_block).grid(row=6, column=0, columnspan=2, pady=10)
        
        # Khu vực hiển thị blockchain
        ttk.Label(self.main_frame, text="Chuỗi Blockchain:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.chain_area = tk.Text(self.main_frame, height=15, width=70, state='disabled')
        self.chain_area.grid(row=8, column=0, columnspan=2, pady=5)
        
        # Nút kiểm tra tính hợp lệ
        ttk.Button(self.main_frame, text="Kiểm tra tính hợp lệ", command=self.check_validity).grid(row=9, column=0, columnspan=2, pady=10)
        
        # Hiển thị blockchain ban đầu
        self.display_chain()

    def add_transaction(self):
        sender = self.sender_entry.get().strip()
        receiver = self.receiver_entry.get().strip()
        amount = self.amount_entry.get().strip()
        
        # Kiểm tra input
        if not sender or not receiver or not amount:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin giao dịch!")
            return
        
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Số tiền phải lớn hơn 0!")
        except ValueError:
            messagebox.showerror("Lỗi", "Số tiền phải là một số hợp lệ và lớn hơn 0!")
            return
        
        # Thêm giao dịch vào blockchain
        self.blockchain.add_transaction(sender, receiver, amount)
        messagebox.showinfo("Thành công", f"Đã thêm giao dịch: {sender} -> {receiver}: {amount}")
        
        # Xóa các ô nhập
        self.sender_entry.delete(0, tk.END)
        self.receiver_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def mine_block(self):
        # Thêm giao dịch thưởng cho miner
        self.blockchain.add_transaction('Genesis', 'Miner', 1)
        
        # Lấy thông tin khối trước đó
        previous_block = self.blockchain.get_previous_block()
        previous_proof = previous_block.proof
        previous_hash = previous_block.hash
        
        # Thực hiện proof of work
        new_proof = self.blockchain.proof_of_work(previous_proof)
        
        # Tạo khối mới
        self.blockchain.create_block(new_proof, previous_hash)
        
        messagebox.showinfo("Thành công", "Đã khai thác khối mới!")
        
        # Cập nhật hiển thị blockchain
        self.display_chain()

    def display_chain(self):
        self.chain_area.configure(state='normal')
        self.chain_area.delete("1.0", tk.END)
        
        for block in self.blockchain.chain:
            self.chain_area.insert(tk.END, f"Block #{block.index}\n")
            self.chain_area.insert(tk.END, f"Timestamp: {block.timestamp}\n")
            self.chain_area.insert(tk.END, f"Transactions: {block.transactions}\n")
            self.chain_area.insert(tk.END, f"Proof: {block.proof}\n")
            self.chain_area.insert(tk.END, f"Previous Hash: {block.previous_hash}\n")
            self.chain_area.insert(tk.END, f"Hash: {block.hash}\n")
            self.chain_area.insert(tk.END, "-------------------\n")
        
        self.chain_area.configure(state='disabled')
        self.chain_area.see(tk.END)

    def check_validity(self):
        is_valid = self.blockchain.is_chain_valid(self.blockchain.chain)
        messagebox.showinfo("Kết quả", f"Chuỗi Blockchain hợp lệ: {is_valid}")
        
        # Cập nhật hiển thị blockchain
        self.display_chain()

def main():
    root = tk.Tk()
    app = BlockchainUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()