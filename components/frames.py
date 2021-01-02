import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
from components import widgets, commands

# TODO: Implement command after confirm button clicked
# TODO: Implement analyzing window

# Starting Resolution
HEIGHT = 800
WIDTH = 1280


def initialize(root):
    global frame
    frame = tk.Frame(root, bg="white")
    frame.pack(side="top", expand=True, fill="both")

    mainFrame(root)


# Function for frame checking
def checkFrame():
    global frame
    for widget in frame.winfo_children():
        widget.destroy()


def mainFrame(root):
    global frame
    checkFrame()

    # Title
    widgets.title(frame, 0.5, 0.2)

    # Buttons
    widgets.webcamButton(frame, root, 0.3, 0.7, 0.15, 0.05)
    widgets.fileButton(frame, root, 0.7, 0.7, 0.15, 0.05)
    widgets.testButton(frame, root, 0.5, 0.8, 0.15, 0.05)


def webcamFrame(root):
    global frame
    checkFrame()

    # Buttons
    widgets.backButton(frame, root, 0.85, 0.9, 0.15, 0.05)


def fileFrame(root):
    global theImage
    global frame
    checkFrame()

    filename = ""
    # Opens and converts image to tKinter readable format. Will revert to main window if cancelled
    try:
        filename = filedialog.askopenfilename(
            title="Select A File",
            filetypes=(("png files", ".png"), ("jpg files", ".jpg .jpeg")),
        )
        theImage = ImageTk.PhotoImage(Image.open(filename))

        # Checks if loaded image is greater than designated size or not
        if theImage.width() < frame.winfo_width() // 2 and frame.winfo_height() < HEIGHT // 2:
            tk.Label(frame, image=theImage).place(relx=0.5, rely=0.3, anchor="center")
        else:
            theImage = ImageTk.PhotoImage(Image.open(filename).resize((600, 600), Image.ANTIALIAS))
            tk.Label(frame, image=theImage).place(relx=0.5, rely=0.4, anchor="center")

        # Buttons
        widgets.confirmButton(frame, root, 0.5, 0.85, 0.15, 0.05)
    except:
        mainFrame(root)


def testFrame(root):
    global frame
    checkFrame()

    canvas = widgets.TestAI(frame, width=500, height=500, background="black", highlightthickness=10, highlightbackground="gray")
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Label
    tk.Label(frame, text="Draw Here!", font="Helvetica 70", bg="white").place(relx=0.5, rely=0.1, anchor="center")

    # Buttons
    widgets.backButton(frame, root, 0.85, 0.9, 0.15, 0.05)