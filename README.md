Shuffl3d – Image Encryption Tool

Shuffl3d is a simple Python GUI tool that encrypts and decrypts images by **scrambling pixel positions** and **shifting RGB values**. It ensures that the image becomes completely unreadable without the correct key.

## 🧠 How It Works

1. **Scrambles** all pixels using a key-based random shuffle
2. **Shifts** each pixel’s RGB values using the same key
3. **Decrypts** by reversing both operations with the correct key

## ⚙️ Tech Stack

* Python 3.x
* `Tkinter` – GUI
* `Pillow` – Image processing
* `random` – For pixel shuffling

## 🚀 How to Use

1. Clone repo and install Pillow:

   ```bash
   pip install pillow
   ```

2. Run the app:

   ```bash
   python shuffl3d.py
   ```

3. In the GUI:

   * Choose an image
   * Enter an integer key
   * Click **Encrypt** or **Decrypt**

Output image is saved in the same folder with `_encrypted` or `_decrypted` suffix.

## ✅ Example

Input: `photo.jpg` + key `123`
→ Output: `photo_encrypted.jpg`
→ Decrypt with same key → `photo_decrypted.jpg`

Built during my internship at **Prodigy Infotech**.
