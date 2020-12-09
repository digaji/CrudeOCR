import tkinter as tk

# Starting resolution
HEIGHT = 800
WIDTH = 1280

# Initialize main window
main = tk.Tk()
main.title("Crude OCR")

window = tk.Canvas(main, height=HEIGHT, width=WIDTH, bg="white")
window.pack()

# Title
title = tk.Label(main, text="Crude OCR", font="Helvetica 100", bg="white")
title.place(relx=0.5, rely=0.2, anchor="center")

# Buttons
buttonWebcam = tk.Button(main, text="Start Webcam", bg="#a8cbff")
buttonWebcam.place(relx=0.3, rely=0.7, anchor="center", relwidth=0.15, relheight=0.05)

buttonFile = tk.Button(main, text="Open File", bg="#ff7272")
buttonFile.place(relx=0.7, rely=0.7, anchor="center", relwidth=0.15, relheight=0.05)

buttonTest = tk.Button(main, text="Test the AI!")
buttonTest.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.15, relheight=0.05)

# Starts the window
main.mainloop()