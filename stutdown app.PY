
import os
from tkinter import *
from tkinter import messagebox

# ------------------------ System Control Functions ------------------------

# Shutdown the system after user confirms
def shutdown():
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to shut down?")
    if confirm:
        os.system("shutdown /s /t 1")

# Restart the system immediately after confirmation
def restart():
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to restart now?")
    if confirm:
        os.system("shutdown /r /t 1")

# Restart the system after 20 seconds
def restart_time():
    confirm = messagebox.askyesno("Confirmation", "Restart in 20 seconds?")
    if confirm:
        os.system("shutdown /r /t 20")

# Log out the current user session
def logout():
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to log out?")
    if confirm:
        os.system("shutdown -l")

# Abort a scheduled shutdown/restart
def abort():
    os.system("shutdown /a")
    messagebox.showinfo("Cancelled", "Scheduled shutdown/restart has been cancelled.")

# Exit the application
def exit_app():
    root.destroy()

# Minimize the application window
def minimize_window():
    root.iconify()

# Toggle fullscreen mode on/off using F11
def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

# Exit fullscreen mode using Esc key
def exit_fullscreen(event=None):
    global fullscreen
    fullscreen = False
    root.attributes("-fullscreen", False)

# ------------------------ GUI Setup Using Tkinter ------------------------

# Create main window
root = Tk()  # Initialize the main application window
root.title("Shutdown App - System Control Panel")  # Set window title
root.geometry("400x550")         # Set window size
root.resizable(False, False)     # Disable window resizing
root.configure(bg="#2c3e50")     # Set background color
fullscreen = False               # Initialize fullscreen state

# Keyboard shortcuts
root.bind("<F11>", toggle_fullscreen)  # Press F11 to toggle fullscreen
root.bind("<Escape>", exit_fullscreen)  # Press Esc to exit fullscreen

# ------------------------ Style for Buttons ------------------------

style = {
    "font": ("Segoe UI", 14, "bold"),
    "bg": "#3498db",
    "fg": "white",
    "activebackground": "#2980b9",
    "activeforeground": "white",
    "relief": RAISED,
    "bd": 2,
    "cursor": "hand2",
    "width": 25,
    "height": 2
}

# ------------------------ Heading Label ------------------------

heading = Label(root, text="System Control Panel", font=("Segoe UI", 20, "bold"), 
                fg="white", bg="#2c3e50")
heading.pack(pady=20)

# ------------------------ Button Section ------------------------

btn_frame = Frame(root, bg="#2c3e50")
btn_frame.pack(pady=10)

# Create control buttons
Button(btn_frame, text="🔁 Restart Now", command=restart, **style).pack(pady=5)
Button(btn_frame, text="🕒 Restart in 20 sec", command=restart_time, **style).pack(pady=5)
Button(btn_frame, text="🚪 Log Out", command=logout, **style).pack(pady=5)
Button(btn_frame, text="⏻ Shut Down", command=shutdown, **style).pack(pady=5)
Button(btn_frame, text="❌ Cancel Shutdown", command=abort, **style).pack(pady=5)
Button(btn_frame, text="🗕 Minimize", command=minimize_window, **style).pack(pady=5)
Button(btn_frame, text="🖵 Toggle Fullscreen (F11)", command=toggle_fullscreen, **style).pack(pady=5)
Button(btn_frame, text="🔙 Exit App", command=exit_app, **style).pack(pady=5)

# ------------------------ Start Application ------------------------

root.mainloop()  # Start the GUI event loop
