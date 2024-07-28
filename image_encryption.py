from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def encrypt_image(image_path, key):
    try:
        image = Image.open(image_path)
        pixels = np.array(image, dtype=np.uint8)
        
        key_int = int.from_bytes(key.encode(), 'little') % 256
        encrypted_pixels = (pixels.astype(np.int16) + key_int) % 256
        encrypted_pixels = encrypted_pixels.astype(np.uint8)
        
        encrypted_image = Image.fromarray(encrypted_pixels)
        return encrypted_image
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")
        return None

def decrypt_image(image_path, key):
    try:
        image = Image.open(image_path)
        pixels = np.array(image, dtype=np.uint8)
        
        key_int = int.from_bytes(key.encode(), 'little') % 256
        decrypted_pixels = (pixels.astype(np.int16) - key_int) % 256
        decrypted_pixels = decrypted_pixels.astype(np.uint8)
        
        decrypted_image = Image.fromarray(decrypted_pixels)
        return decrypted_image
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")
        return None

def select_file():
    return filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

def save_file(image):
    if image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        if file_path:
            image.save(file_path)

def encrypt_action():
    image_path = select_file()
    if image_path:
        key = simpledialog.askstring("Encryption Key", "Enter the encryption key:")
        if key:
            encrypted_image = encrypt_image(image_path, key)
            if encrypted_image:
                save_file(encrypted_image)
                messagebox.showinfo("Success", "Image encrypted successfully!")

def decrypt_action():
    image_path = select_file()
    if image_path:
        key = simpledialog.askstring("Decryption Key", "Enter the decryption key:")
        if key:
            decrypted_image = decrypt_image(image_path, key)
            if decrypted_image:
                save_file(decrypted_image)
                messagebox.showinfo("Success", "Image decrypted successfully!")

# GUI setup
root = tk.Tk()
root.title("Image Encryption Tool")

tk.Button(root, text="Encrypt Image", command=encrypt_action).pack(pady=10)
tk.Button(root, text="Decrypt Image", command=decrypt_action).pack(pady=10)

root.mainloop()
