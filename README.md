# Funky File Hashing Tool 🔍🎨

A lightweight, colorful desktop application built to generate, compare, and export file hashes. 

## 💡 Why I Built This
As I dive deeper into computer science and system security, I wanted to get hands-on with cryptographic hashing. Verifying file integrity is a core concept in everything from basic software downloads to malware analysis. I built this tool to take a backend concept (generating SHA-256/SHA-512 hashes via Python's `hashlib`) and wrap it in a custom, user-friendly graphical interface. 

It was a great exercise in bridging core Python logic with GUI development and OS-level file handling.

## ✨ Features
* **Core Cryptography:** Generates secure SHA-256 and SHA-512 hashes for any file on your system.
* **Integrity Checking:** Includes a quick-compare feature to match a generated hash against a known hash (useful for verifying downloads).
* **Export & Clipboard Integration:** One-click copy to clipboard or export the results directly to a `.txt` file.
* **Custom UI:** Built entirely with `customtkinter` to step away from standard, boring system windows. It features dynamic canvas shapes and a personalized color palette.

## 💻 Tech Stack & Concepts Learned
* **Python 3**
* **CustomTkinter & Tkinter:** Learned how to build and structure event-driven desktop applications.
* **Hashlib:** Implemented chunked file reading to efficiently hash large files without overloading system memory.
* **OS & File System Interaction:** Wrote recursive directory search algorithms to locate specific assets (like the background image) and used `filedialog` for user inputs.
* **Pillow (PIL):** Handled image processing and dynamic resizing for the application window.

## 🚀 Getting Started

### The Quick Way (Executable)
You don't need Python installed to test this out!
1. Download `GUI.exe` from this repository.
2. Double-click to run.

### 🎨 A Fun File-Handling Quirk: The Background
To practice OS-level file searching, I programmed the app to dynamically hunt for its own background. 
* If you want the full visual experience, download `funky_background.png` from this repo and save it *anywhere* on your `C:\` drive. The script will recursively search your drive, find it, and load it.
* **Fallback:** If it doesn't find the image, the app handles the exception gracefully, falling back to a clean `#FFF8DC` background and rendering its own geometric shapes on the canvas.

### Running from Source
If you want to check out the code and run it directly:

```bash
# Install the required libraries
pip install customtkinter Pillow

# Run the application
python GUI.py
