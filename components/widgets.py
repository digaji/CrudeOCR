import tkinter as tk
from tkinter import ttk
from components import commands, windows

def title(window, x, y):
    tk.Label(window, text="Crude OCR", font="Helvetica 100", bg="white").place(relx=x, rely=y, anchor="center")

def webcamButton(window, root, x, y, width, height):
    tk.Button(window, text="Start Webcam", bg="#a8cbff", command=lambda: windows.webcamWindow(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def fileButton(window, root, x, y, width, height):
    tk.Button(window, text="Open File", bg="#ff7272", command=lambda: windows.fileWindow(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def testButton(window, root, x, y, width, height):
    tk.Button(window, text="Test the AI!").place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def backButton(window, root, x, y, width, height):
    tk.Button(window, text="Back", bg="#ff7272", command=lambda: windows.mainWindow(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def confirmButton(window, root, x, y, width, height):
    tk.Button(window, text="Confirm?", command=lambda: windows.mainWindow(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def webcamFrame(window, x, y, width, height):
    pass

def textField(window, x, y, width, height):
    pass

def scrollText(window):
    pass

# TODO: Implement commands from commands.py