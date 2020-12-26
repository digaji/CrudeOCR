import tkinter as tk
from commands import *

def title(window, x, y):
    title = tk.Label(window, text="Crude OCR", font="Helvetica 100", bg="white")
    title.place(relx=x, rely=y, anchor="center")

def webcamButton(window, x, y, width, height):
    buttonWebcam = tk.Button(window, text="Start Webcam", bg="#a8cbff", command=pass)
    buttonWebcam.place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def fileButton(window, x, y, width, height):
    buttonFile = tk.Button(window, text="Open File", bg="#ff7272", command=pass)
    buttonFile.place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def testButton(window, x, y, width, height):
    buttonTest = tk.Button(window, text="Test the AI!", command=pass)
    buttonTest.place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def backButton(window, x, y, width, height):
    buttonBack = tk.Button(window, text="Back", bg="#ff7272", command=pass)
    buttonBack.place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def confirmButton(window, x, y, width, height):
    buttonConfirm = tk.Button(window, text="Confirm?", command=pass)
    buttonConfirm.place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def webcamFrame(window, x, y, width, height):
    pass

def textField(window, x, y, width, height):
    pass

def scrollText():
    pass

# TODO: Implement commands in commands.py
# TODO: Change commands to clear main window instead of creating new top levels