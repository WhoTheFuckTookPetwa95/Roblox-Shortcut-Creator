import os
import re
import winshell
from win32com.client import Dispatch
import tkinter as tk
from tkinter import messagebox

# ---------- COLORS ----------
BG = "#0f172a"          # dark background
CARD = "#1e293b"        # card color
ACCENT = "#38bdf8"      # blue accent
TEXT = "#e2e8f0"        # text color
INPUT_BG = "#0b1220"

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Roblox Shortcut Generator")
root.geometry("420x300")
root.configure(bg=BG)
root.resizable(False, False)

# ---------- FRAME (CARD STYLE) ----------
frame = tk.Frame(root, bg=CARD)
frame.pack(padx=15, pady=15, fill="both", expand=True)

# ---------- TITLE ----------
title = tk.Label(
    frame,
    text="Roblox Shortcut Generator",
    bg=CARD,
    fg=TEXT,
    font=("Segoe UI", 16, "bold")
)
title.pack(pady=(10, 15))

# ---------- GAME LINK ----------
label = tk.Label(frame, text="Game Link", bg=CARD, fg=TEXT, font=("Segoe UI", 10))
label.pack(anchor="w", padx=15)

entry = tk.Entry(
    frame,
    width=40,
    bg=INPUT_BG,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    font=("Segoe UI", 10)
)
entry.pack(padx=15, pady=(0, 10), ipady=5)

# ---------- NAME ----------
name_label = tk.Label(frame, text="Shortcut Name", bg=CARD, fg=TEXT, font=("Segoe UI", 10))
name_label.pack(anchor="w", padx=15)

name_entry = tk.Entry(
    frame,
    width=30,
    bg=INPUT_BG,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    font=("Segoe UI", 10)
)
name_entry.pack(padx=15, pady=(0, 15), ipady=5)

# ---------- FUNCTION ----------
def generate():
    url = entry.get()
    name = name_entry.get()

    match = re.search(r'games/(\d+)', url)

    if not match:
        messagebox.showerror("Error", "Invalid Roblox link")
        return

    place_id = match.group(1)

    if name.strip() == "":
        name = f"Roblox Game {place_id}"

    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, name + ".lnk")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = f"roblox://placeId={place_id}"
    shortcut.IconLocation = "C:\\Windows\\System32\\shell32.dll, 220"
    shortcut.save()

    messagebox.showinfo("Success", f"Shortcut created:\n{name}")

# ---------- BUTTON ----------
def on_enter(e):
    btn["bg"] = "#0ea5e9"

def on_leave(e):
    btn["bg"] = ACCENT

btn = tk.Button(
    frame,
    text="Generate Shortcut",
    command=generate,
    bg=ACCENT,
    fg="black",
    activebackground="#0ea5e9",
    relief="flat",
    font=("Segoe UI", 11, "bold"),
    cursor="hand2"
)
btn.pack(pady=10, ipadx=10, ipady=6)

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# ---------- FOOTER ----------
footer = tk.Label(
    frame,
    text="Made for Roblox players",
    bg=CARD,
    fg="#94a3b8",
    font=("Segoe UI", 8)
)
footer.pack(pady=(5, 10))

root.mainloop()