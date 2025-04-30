
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageCompressor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Compressor")
        self.geometry("600x300")
        self.image_path = None

        # Button to select an image file
        tk.Button(self, text="Select Image", command=self.select_image).pack(pady=10)
        self.file_label = tk.Label(self, text="No file selected")
        self.file_label.pack()

        # Slider to choose compression quality
        tk.Label(self, text="Quality (1-50):").pack(pady=5)
        self.quality_scale = tk.Scale(self, from_=1, to=50, orient=tk.HORIZONTAL)
        self.quality_scale.pack()

        # Button to compress and save
        tk.Button(self, text="Compress and Save", command=self.compress_image).pack(pady=10)

    def select_image(self):
        filetypes = [("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")]
        path = filedialog.askopenfilename(title="Select Image", filetypes=filetypes)
        if path:
            self.image_path = path
            self.file_label.config(text=os.path.basename(path))

    def compress_image(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please select an image first.")
            return

        quality = self.quality_scale.get()
        img = Image.open(self.image_path)

        # Suggest save location and filename
        dir_path, filename = os.path.split(self.image_path)
        name, _ = os.path.splitext(filename)
        default_name = f"{name}_compressed.jpg"
        output_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            initialfile=default_name,
            filetypes=[("JPEG files", "*.jpg *.jpeg")]
        )
        if not output_path:
            return

        # Convert PNG with alpha to RGB before saving
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Save with chosen quality and optimization
        img.save(output_path, "JPEG", optimize=True, quality=quality)
        messagebox.showinfo("Success", f"Image saved at {output_path}")

if __name__ == "__main__":
    app = ImageCompressor()
    app.mainloop()
