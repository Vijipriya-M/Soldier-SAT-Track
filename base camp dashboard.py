import tkinter as tk
from tkinter import scrolledtext
import time
import os

log_file_path = "patrol_log.txt"

# Create the file with a default message if it doesn't exist
if not os.path.exists(log_file_path):
    with open(log_file_path, "w") as f:
        f.write("📍 Base camp log initialized...\n")

# GUI setup
root = tk.Tk()
root.title("🛰️ SAT-Track Base Camp")
root.configure(bg="black")

# Text area setup
text_box = scrolledtext.ScrolledText(root, width=100, height=30, bg="black", fg="lime", font=("Courier", 11))
text_box.pack(padx=20, pady=20)

# Function to update logs
def update_logs():
    try:
        with open(log_file_path, "r") as f:
            content = f.read()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, content)
        root.after(2000, update_logs)  # Refresh every 2 sec
    except Exception as e:
        text_box.insert(tk.END, f"Error reading log: {e}\n")

# Start log updates
update_logs()

root.mainloop()
