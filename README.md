# Roblox-Shortcut-Creator
Makes an app or shortcut on your desktop that opens a roblox game instantly.
# 🎮 Roblox Shortcut Generator

A simple desktop app that lets you generate Roblox game shortcuts directly from a game link.

No more digging through folders or losing your screenshots — just paste, click, done.

---

## ✨ Features

* 🔗 Paste any Roblox game link
* ⚡ Instantly generate a desktop shortcut
* 🖥️ Clean and simple UI (Tkinter-based)
* 🚫 No command prompt window (built as a GUI app)
* 💾 Saves time finding your games again

---

## 📦 Installation

### Option 1: Download EXE (Recommended)

1. Go to the **Releases** tab
2. Download the latest `.exe`
3. Run it — no setup needed

### Option 2: Run from Source

Make sure you have Python installed (3.9+ recommended)

```bash
pip install pywin32 winshell
python main.py
```

---

## 🛠️ Build from Source

To convert the app into an `.exe`:

```bash
pyinstaller --onefile --noconsole main.py
```

The executable will be in the `/dist` folder.

---

## 📋 Requirements

* Python 3.9+
* Windows OS
* Modules:

  * `winshell`
  * `pywin32`
  * `tkinter` (comes with Python)

---

## 🚀 How to Use

1. Open the app
2. Paste a Roblox game link (example):

   ```
   https://www.roblox.com/games/123456789/Example-Game
   ```
3. Click **Generate Shortcut**
4. Done! Your shortcut will appear on your desktop

---

## ⚠️ Notes

* Only works on Windows (uses Windows shortcut system)
* Make sure your Roblox link is valid
* If antivirus complains, it’s usually because of PyInstaller packaging

---

## 🧠 Why This Exists

Roblox screenshots and links can get messy fast.
This tool helps you quickly create shortcuts so you can jump back into games instantly.

---

## 📜 License

MIT License — feel free to use, modify, and share.

---

## 💬 Contributing

Pull requests are welcome!
If you have ideas or improvements, feel free to open an issue.

---

## ⭐ Support

If you like this project, consider giving it a star on GitHub!

---
