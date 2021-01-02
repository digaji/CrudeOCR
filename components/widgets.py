import tkinter as tk
from tkinter import ttk
from components import frames, commands

def title(frame, x, y):
    tk.Label(frame, text="Crude OCR", font="Helvetica 100", bg="white").place(relx=x, rely=y, anchor="center")

def webcamButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Start Webcam", bg="#a8cbff", command=lambda: frames.webcamFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def fileButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Open File", bg="#ff7272", command=lambda: frames.fileFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def testButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Test the AI!", command=lambda: frames.testFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def backButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Back", bg="#ff7272", command=lambda: frames.mainFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def confirmButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Confirm?", command=lambda: frames.mainFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)

def webcamFrame(frame, x, y, width, height):
    pass

def textField(frame, x, y, width, height):
    pass

def scrollbarText(frame):
    pass

# Test AI Canvas Class
class TestAI(tk.Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Mouse bindings for painting
        self.bind("<Button-1>", self.lastPos)
        self.bind("<B1-Motion>", self.addLine)

    def lastPos(self, event):
        # Remembers the last position of the mouse click
        self.lastX, self.lastY = event.x, event.y

    def addLine(self, event):
        # Creates lines for painting
        self.create_line(self.lastX, self.lastY, event.x, event.y, fill="white", width=5)
        self.lastPos(event)

# TODO: Implement commands from commands.py