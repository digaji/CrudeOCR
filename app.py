import tkinter as tk
from windows import *

# Initialize main window
root = tk.Tk()
root.title("Crude OCR")
root.geometry("1280x800")
root.config(bg="white")

mainWindow(root)

# Starts the window
root.mainloop()
