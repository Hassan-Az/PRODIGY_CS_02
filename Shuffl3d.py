import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import random
import os

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shuffl3d")
        self.root.geometry("500x250")
        self.root.resizable(False, False)
        
        # Matte color scheme
        self.bg_color = "#f5f7fa"  # Soft blue-gray
        self.frame_color = "#e8ecef"  # Light gray
        self.accent_color = "#6c7a89"  # Matte blue-gray
        self.text_color = "#333333"  # Dark gray
        self.button_color = "#8d9aa9"  # Muted blue-gray
        self.button_hover = "#7a8897"  # Slightly darker on hover
        self.status_color = "#dde1e6"  # Light status bar
        
        # Configure root background
        self.root.configure(bg=self.bg_color)
        
        # Image file path
        self.image_path = None
        
        # Create GUI elements
        self.create_widgets()
        
        # Bind hover effects
        self.bind_hover_effects()
    
    def create_widgets(self):
        # Main container frame
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Title
        title = tk.Label(
            main_frame, 
            text="Shuffl3d - Image encryption tool",
            font=("Segoe UI", 14, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
            pady=5
        )
        title.pack(fill="x")
        
        # File selection frame
        file_frame = tk.Frame(main_frame, bg=self.bg_color, pady=10)
        file_frame.pack(fill="x")
        
        tk.Label(
            file_frame, 
            text="Image File:", 
            bg=self.bg_color, 
            fg=self.text_color,
            font=("Segoe UI", 9)
        ).pack(side="left", anchor="w")
        
        # File path display with subtle border
        self.file_label = tk.Label(
            file_frame, 
            text="No file selected",
            anchor="w",
            bg="white",
            fg="#666666",
            relief="flat",
            bd=1,
            padx=10,
            height=1,
            width=30,
            font=("Segoe UI", 9)
        )
        self.file_label.pack(side="left", padx=(5, 0), fill="x", expand=True)
        
        # Browse button with minimal styling
        self.btn_choose = tk.Button(
            file_frame, 
            text="Browse",
            command=self.choose_image,
            bg=self.button_color,
            fg="white",
            activebackground=self.button_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=2,
            font=("Segoe UI", 9)
        )
        self.btn_choose.pack(side="right")
        
        # Key input frame
        key_frame = tk.Frame(main_frame, bg=self.bg_color, pady=10)
        key_frame.pack(fill="x")
        
        tk.Label(
            key_frame, 
            text="Encryption Key:", 
            bg=self.bg_color, 
            fg=self.text_color,
            font=("Segoe UI", 9)
        ).pack(side="left", anchor="w")
        
        # Key entry with minimal styling
        self.key_entry = tk.Entry(
            key_frame, 
            width=30,
            relief="flat",
            bd=1,
            bg="white",
            fg=self.text_color,
            font=("Segoe UI", 9),
            highlightthickness=1,
            highlightbackground="#cccccc",
            highlightcolor=self.accent_color
        )
        self.key_entry.pack(side="left", padx=(5, 0), fill="x", expand=True)
        self.key_entry.bind("<Return>", lambda e: self.encrypt_image())
        
        # Button container
        btn_frame = tk.Frame(main_frame, bg=self.bg_color, pady=20)
        btn_frame.pack(fill="x")
        
        # Encrypt button
        self.btn_encrypt = tk.Button(
            btn_frame, 
            text="Encrypt Image",
            command=self.encrypt_image,
            bg=self.button_color,
            fg="white",
            activebackground=self.button_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=8,
            font=("Segoe UI", 10, "bold")
        )
        self.btn_encrypt.pack(side="left", padx=(0, 10), fill="x", expand=True)
        
        # Decrypt button
        self.btn_decrypt = tk.Button(
            btn_frame, 
            text="Decrypt Image",
            command=self.decrypt_image,
            bg=self.button_color,
            fg="white",
            activebackground=self.button_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=8,
            font=("Segoe UI", 10, "bold")
        )
        self.btn_decrypt.pack(side="right", padx=(10, 0), fill="x", expand=True)
        
        # Status bar with minimal styling
        self.status_bar = tk.Label(
            self.root, 
            text="Ready to encrypt or decrypt images",
            bd=0, 
            relief="flat", 
            anchor="w",
            bg=self.status_color,
            fg="#666666",
            padx=10,
            font=("Segoe UI", 8)
        )
        self.status_bar.pack(side="bottom", fill="x")
    
    def bind_hover_effects(self):
        # Add hover effects to buttons
        for btn in [self.btn_choose, self.btn_encrypt, self.btn_decrypt]:
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.button_hover))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.button_color))
    
    def choose_image(self):
        filetypes = [
            ("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.webp"),
            ("All files", "*.*")
        ]
        self.image_path = filedialog.askopenfilename(filetypes=filetypes)
        
        if self.image_path:
            filename = os.path.basename(self.image_path)
            self.file_label.config(text=filename)
            self.status_bar.config(text=f"Selected: {filename}")
        else:
            self.status_bar.config(text="No file selected")
    
    def validate_key(self):
        key_str = self.key_entry.get()
        if not key_str:
            messagebox.showerror("Error", "Please enter an encryption key")
            return None
        
        try:
            key = int(key_str)
            # Key can be any integer, but we'll recommend 0-2^31-1
            return key
        except ValueError:
            messagebox.showerror("Invalid Key", "Key must be an integer")
            return None
    
    def encrypt_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image file first!")
            return
        
        key = self.validate_key()
        if key is None:
            return
        
        try:
            self.status_bar.config(text="Encrypting image...")
            self.root.update()
            
            with Image.open(self.image_path) as img:
                # Convert to RGB if needed
                if img.mode != "RGB":
                    img = img.convert("RGB")
                
                width, height = img.size
                pixels = list(img.getdata())
                n = len(pixels)
                
                # Step 1: Pixel scrambling
                indices = list(range(n))
                random.seed(key)
                random.shuffle(indices)
                
                scrambled_pixels = [pixels[i] for i in indices]
                
                # Step 2: Value shifting
                shifted_pixels = []
                for pixel in scrambled_pixels:
                    r, g, b = pixel
                    shifted_pixels.append((
                        (r + key) % 256,
                        (g + key) % 256,
                        (b + key) % 256
                    ))
                
                # Create new image
                encrypted_img = Image.new("RGB", (width, height))
                encrypted_img.putdata(shifted_pixels)
                
                # Save output
                base, ext = os.path.splitext(self.image_path)
                output_path = f"{base}_encrypted{ext}"
                encrypted_img.save(output_path)
            
            self.status_bar.config(text="Encryption completed successfully")
            messagebox.showinfo(
                "Success", 
                f"Image encrypted successfully!\nSaved as: {os.path.basename(output_path)}"
            )
                
        except Exception as e:
            self.status_bar.config(text="Error during encryption")
            messagebox.showerror(
                "Encryption Error", 
                f"An error occurred during encryption:\n{str(e)}"
            )
    
    def decrypt_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image file first!")
            return
        
        key = self.validate_key()
        if key is None:
            return
        
        try:
            self.status_bar.config(text="Decrypting image...")
            self.root.update()
            
            with Image.open(self.image_path) as img:
                # Convert to RGB if needed
                if img.mode != "RGB":
                    img = img.convert("RGB")
                
                width, height = img.size
                pixels = list(img.getdata())
                n = len(pixels)
                
                # Step 1: Reverse value shifting
                unshifted_pixels = []
                for pixel in pixels:
                    r, g, b = pixel
                    unshifted_pixels.append((
                        (r - key) % 256,
                        (g - key) % 256,
                        (b - key) % 256
                    ))
                
                # Step 2: Reverse scrambling
                indices = list(range(n))
                random.seed(key)
                random.shuffle(indices)
                
                # Create an empty array for original pixels
                original_pixels = [0] * n
                for i in range(n):
                    # Place the pixel at its original position
                    original_pixels[indices[i]] = unshifted_pixels[i]
                
                # Create new image
                decrypted_img = Image.new("RGB", (width, height))
                decrypted_img.putdata(original_pixels)
                
                # Save output
                base, ext = os.path.splitext(self.image_path)
                output_path = f"{base}_decrypted{ext}"
                decrypted_img.save(output_path)
            
            self.status_bar.config(text="Decryption completed successfully")
            messagebox.showinfo(
                "Success", 
                f"Image decrypted successfully!\nSaved as: {os.path.basename(output_path)}"
            )
                
        except Exception as e:
            self.status_bar.config(text="Error during decryption")
            messagebox.showerror(
                "Decryption Error", 
                f"An error occurred during decryption:\n{str(e)}"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()