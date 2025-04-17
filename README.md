# BMPtoHEX

A lightweight Windows GUI program to convert grayscale BMP images into HEX-formatted `.txt` files.

---

## 📝 Release Notes

**v1.0** (2025-04-17)  
- Initial release  
- Convert grayscale BMP image to HEX-formatted `.txt` file  
- Supports Dark Mode  
- Shortcut key support  

---

## 🚀 How to Use

1. Download the `.exe` file from the release page  
2. Run the application  
3. Upload the grayscale BMP image you want to convert (**320x80 resolution only**)  
4. Click the **Transform** button  
5. Choose a folder and filename to save  
6. HEX-formatted `.txt` file will be generated from the image  

---

## ✨ Features

- 🌓 **Dark Mode** toggle support  
- ⌨️ **Keyboard Shortcuts**:
  - `Ctrl + O` : Open BMP image  
  - `Ctrl + S` : Save as HEX  
  - `Esc` : Exit the program

---

## 🛠 How to Build (`.exe`)

1. Install required modules:
   ```bash
   pip install pyinstaller Pillow
   ```

2. Run build command:
   ```bash
   pyinstaller --onefile --noconsole --icon=test.ico test.py
   ```

> 💡 Make sure your icon file (`test.ico`) and Python script are in the same folder when building.

---

## 📌 Notes

- Input image must be grayscale `.bmp` with resolution `320x80`  
- Output is a `.txt` file with HEX values like `0x00 0x1F 0xA3 ...` for each pixel row  
- This tool is optimized for grayscale conversion, so colored images should be preprocessed if necessary  

---

## 🧭 Planned Features (Coming Soon)

- ✅ Save converted image as `.bmp` file (resized to 320x80)
- ✅ Automatically scale any BMP image while maintaining aspect ratio
- ✅ Drag & Drop image upload
- ✅ HEX preview before saving
- ✅ Language toggle (Korean / English)

---

## 💻 Environment

- Windows 10 / 11  
- Python 3.10 or later (for building)  
- Pillow  
- PyInstaller  

---

## 👤 Author

- **Cho Jeonghun (조정훈)**   

