import tkinter as tk
import customtkinter as ctk 
from tkinter import filedialog, messagebox
from PIL import Image 
import hashlib
import os

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("dark-blue")

ALGORITHMS = {
    'SHA-256': hashlib.sha256,
    'SHA-512': hashlib.sha512,
}
ALGO_DESCRIPTIONS = {
    'SHA-256': "SHA-256: Secure, recommended for most uses. 🔒",
    'SHA-512': "SHA-512: Extra strong, for high-security needs. 🛡️",
}

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

class FunkyHashApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🎉 Funky File Hashing Tool 🎉")
        self.geometry("800x600")
        self.resizable(False, False)

        bg_img_path = find_file("funky_background.png", "C:\\")
        if bg_img_path:
            bg_img = Image.open(bg_img_path).resize((800, 600))
            print(f"Image loaded from: {bg_img_path}")
        else:
            bg_img = Image.new("RGB", (800, 600), "#FFF8DC")
            print("funky_background.png not found on C:\\ drive.")

        self.bg_image = ctk.CTkImage(bg_img, size=(800, 600))
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.funky_canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0, bg="#FFF8DC", bd=0)
        self.funky_canvas.place(x=0, y=0)
        self.draw_funky_shapes()

        self.main_frame = ctk.CTkFrame(self, fg_color="#FFF8DC", corner_radius=30, width=550, height=500)
        self.main_frame.place(relx=0.5, rely=0.52, anchor="center")

        ctk.CTkLabel(self.main_frame, text="Funky File Hashing Tool", font=("Comic Sans MS", 28, "bold"), text_color="#ff6f61").pack(pady=(18, 8))
        ctk.CTkLabel(self.main_frame, text="Generate, compare, and export file hashes in style!", font=("Comic Sans MS", 14, "italic"), text_color="#6B5B95").pack(pady=(0, 18))

        self.file_var = ctk.StringVar()
        file_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        file_frame.pack(pady=(0, 10))
        self.file_entry = ctk.CTkEntry(file_frame, textvariable=self.file_var, width=300, height=38,
                                       placeholder_text="Select a file...", fg_color="#fff8dc", border_color="#ff6f61",
                                       corner_radius=15, font=("Comic Sans MS", 13))
        self.file_entry.pack(side="left", padx=(0, 8))
        ctk.CTkButton(file_frame, text="Browse 🎵", fg_color="#ff6f61", hover_color="#ff8a75",
                      corner_radius=15, font=("Comic Sans MS", 13, "bold"), command=self.select_file).pack(side="left")

        algo_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        algo_frame.pack(pady=(0, 10))
        ctk.CTkLabel(algo_frame, text="Algorithm:", font=("Comic Sans MS", 14, "bold"), text_color="#6B5B95").pack(side="left", padx=(0, 6))
        self.algo_var = ctk.StringVar(value="SHA-256")
        self.algo_menu = ctk.CTkOptionMenu(algo_frame, variable=self.algo_var, values=list(ALGORITHMS.keys()),
                                           width=120, fg_color="#f7cac9", button_color="#6B5B95", font=("Comic Sans MS", 13, "bold"),
                                           dropdown_font=("Comic Sans MS", 12), corner_radius=12, command=self.update_algo_info)
        self.algo_menu.pack(side="left")
        self.algo_info = ctk.CTkLabel(self.main_frame, text=ALGO_DESCRIPTIONS[self.algo_var.get()], font=("Comic Sans MS", 12, "italic"), text_color="#4F8A8B")
        self.algo_info.pack(pady=(2, 8))

        ctk.CTkButton(self.main_frame, text="Generate Hash 🔥", fg_color="#6B5B95", hover_color="#483d8b",
                      corner_radius=18, font=("Comic Sans MS", 14, "bold"), command=self.generate_hash).pack(pady=(6, 6))
        self.hash_var = ctk.StringVar()
        self.hash_entry = ctk.CTkEntry(self.main_frame, textvariable=self.hash_var, width=440, height=38,
                                       placeholder_text="Hash will appear here...", fg_color="#f5f5f5", border_color="#6B5B95",
                                       corner_radius=15, font=("Consolas", 12))
        self.hash_entry.pack(pady=(0, 6))

        btn_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame.pack(pady=(0, 8))
        ctk.CTkButton(btn_frame, text="Export 💾", fg_color="#ff6f61", hover_color="#ff8a75", corner_radius=12,
                      font=("Comic Sans MS", 12, "bold"), width=110, command=self.export_hash).pack(side="left", padx=8)
        ctk.CTkButton(btn_frame, text="Copy 📋", fg_color="#88B04B", hover_color="#a6d608", corner_radius=12,
                      font=("Comic Sans MS", 12, "bold"), width=110, command=self.copy_hash).pack(side="left", padx=8)

        ctk.CTkLabel(self.main_frame, text="Compare With:", font=("Comic Sans MS", 13, "bold"), text_color="#ff6f61").pack(pady=(8, 2))
        self.compare_var = ctk.StringVar()
        self.compare_entry = ctk.CTkEntry(self.main_frame, textvariable=self.compare_var, width=440, height=38,
                                          placeholder_text="Paste or load a hash to compare...", fg_color="#fff8dc", border_color="#ff6f61",
                                          corner_radius=15, font=("Consolas", 12))
        self.compare_entry.pack(pady=(0, 5))
        ctk.CTkButton(self.main_frame, text="Compare Hashes ⚡", fg_color="#88B04B", hover_color="#a6d608",
                      corner_radius=18, font=("Comic Sans MS", 13, "bold"), command=self.compare_hash).pack(pady=(2, 8))

        self.result_label = ctk.CTkLabel(self.main_frame, text="", font=("Comic Sans MS", 15, "bold"))
        self.result_label.pack(pady=(0, 2))

    def draw_funky_shapes(self):
        # Funky overlapping circles and polygons
        self.funky_canvas.create_oval(30, 30, 150, 150, fill="#ff6f61", outline="")
        self.funky_canvas.create_oval(200, 80, 370, 220, fill="#6B5B95", outline="")
        self.funky_canvas.create_polygon(500, 60, 700, 180, 600, 320, fill="#88B04B", outline="")
        self.funky_canvas.create_oval(600, 380, 780, 560, fill="#f7cac9", outline="")
        self.funky_canvas.create_polygon(120, 400, 280, 540, 80, 580, fill="#fbd46d", outline="")

    def select_file(self):
        path = filedialog.askopenfilename(title="Select a file")
        if path:
            self.file_var.set(path)

    def update_algo_info(self, event=None):
        algo = self.algo_var.get()
        self.algo_info.configure(text=ALGO_DESCRIPTIONS.get(algo, ""))

    def generate_hash(self):
        path = self.file_var.get()
        algo = self.algo_var.get()
        if not path or not algo:
            messagebox.showwarning("Missing info", "Please select a file and algorithm.")
            return
        try:
            hash_func = ALGORITHMS[algo]()
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_func.update(chunk)
            self.hash_var.set(hash_func.hexdigest())
            self.result_label.configure(text="Hash generated! 🎉", text_color="#10b981")
        except Exception as e:
            self.result_label.configure(text=f"Error: {e}", text_color="#ef4444")

    def copy_hash(self):
        self.clipboard_clear()
        self.clipboard_append(self.hash_var.get())
        self.result_label.configure(text="Hash copied to clipboard! 📋", text_color="#6B5B95")

    def export_hash(self):
        hash_val = self.hash_var.get()
        if not hash_val:
            messagebox.showwarning("No hash", "Generate a hash first!")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt", title="Export hash as...")
        if path:
            with open(path, "w") as f:
                f.write(hash_val)
            messagebox.showinfo("Exported", f"Hash exported to {os.path.basename(path)}")

    def compare_hash(self):
        if not self.hash_var.get() or not self.compare_var.get():
            messagebox.showwarning("Missing info", "Generate and paste/load a hash to compare.")
            return
        if self.hash_var.get().strip() == self.compare_var.get().strip():
            self.result_label.configure(text="Hashes Match! ✅", text_color="#10b981")
        else:
            self.result_label.configure(text="Hashes DON'T Match! ❌", text_color="#ef4444")

if __name__ == "__main__":
    app = FunkyHashApp()
    app.mainloop()
