# 🎉 Funky File Hashing Tool 🎉

Welcome to the **Funky File Hashing Tool**! This is a colorful, user-friendly desktop application built to generate, compare, and export file hashes securely and in style. 

## ✨ Features
* **Multiple Algorithms:** Supports standard, secure cryptographic hashing algorithms, specifically SHA-256 and SHA-512.
* **Hash Generation:** Browse and select any file from your system to instantly generate its hash.
* **Hash Comparison:** Easily verify file integrity by pasting a known hash into the comparison tool to check for a match.
* **Export & Copy:** Quickly copy the generated hash to your clipboard or export it directly to a `.txt` file.
* **Funky UI:** Features a custom UI built with `customtkinter`, utilizing fun canvas shapes, "Comic Sans MS" fonts, and emoji-themed buttons.

## 🚀 Getting Started

### Running the Executable
You don't need to install Python or any dependencies to use this tool!
1. Download the `GUI.exe` file directly from this repository.
2. Double-click `GUI.exe` to launch the application.

### 🎨 Important Note: The Background Image
To get the full visual experience, the application is programmed to recursively search your entire `C:\` drive for the background image named `funky_background.png`. 
* For the custom background to load, make sure you download `funky_background.png` from this repository and save it *anywhere* on your `C:\` drive. 
* If the image is not found, the app won't crash; it will gracefully fall back to a clean, solid-colored background (`#FFF8DC`) and render its own funky shapes on the canvas.

## 🛠️ Running from Source
If you prefer to run the raw Python script (`GUI.py`) instead of the executable, ensure you have the required dependencies installed:

```bash
pip install customtkinter Pillow
```

Then, run the script from your terminal:
```bash
python GUI.py
```

## 💻 Technologies Used
* **Python 3**
* **CustomTkinter & Tkinter:** For the modern, custom-styled graphical user interface.
* **Pillow (PIL):** For loading and resizing the custom background image.
* **Hashlib:** Native Python library used to generate the secure SHA-256 and SHA-512 hashes.
