import tkinter as tk
from tkinter import messagebox
from client import main as client_main
from server import main as server_main

class DHKeyExchangeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diffie-Hellman Key Exchange")

        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame)
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.server_button = tk.Button(self.scrollable_frame, text="Run Server", command=self.run_server)
        self.server_button.pack(pady=10)

        self.client_button = tk.Button(self.scrollable_frame, text="Run Client", command=self.run_client)
        self.client_button.pack(pady=10)

        self.shared_secret_label = tk.Label(self.scrollable_frame, text="")
        self.shared_secret_label.pack(pady=10)

    def run_server(self):
        try:
            server_main()
            messagebox.showinfo("Success", "Server is running.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run server: {e}")

    def run_client(self):
        try:
            shared_secret = client_main()
            self.shared_secret_label.config(text=f"Shared Secret: {shared_secret}")
            messagebox.showinfo("Success", "Client has derived the shared secret.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run client: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DHKeyExchangeApp(root)
    root.mainloop()
