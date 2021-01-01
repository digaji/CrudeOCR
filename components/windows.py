import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from components import widgets

# TODO: Implement command after confirm button clicked
# TODO: Implement analyzing window

# Starting Resolution
HEIGHT = 800
WIDTH = 1280


def initialize(root):
    global canvas
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
    canvas.pack()

    mainWindow(root)


# Function for canvas checking
def checkCanvas(root):
    global canvas
    if canvas is not None:
        canvas.destroy()
        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
        canvas.pack()


def mainWindow(root):
    global canvas
    checkCanvas(root)

    # Title
    widgets.title(canvas, 0.5, 0.2)

    # Buttons
    widgets.webcamButton(canvas, root, 0.3, 0.7, 0.15, 0.05)
    widgets.fileButton(canvas, root, 0.7, 0.7, 0.15, 0.05)
    widgets.testButton(canvas, root, 0.5, 0.8, 0.15, 0.05)


def webcamWindow(root):
    global canvas
    checkCanvas(root)

    # Title
    widgets.title(canvas, 0.5, 0.1)

    # Buttons
    widgets.backButton(canvas, root, 0.85, 0.9, 0.15, 0.05)


def fileWindow(root):
    global theImage
    global canvas
    checkCanvas(root)

    filename = ""
    # Opens and converts image to tKinter readable format. Will revert to main window if cancelled
    try:
        filename = filedialog.askopenfilename(
            title="Select A File",
            filetypes=(("png files", ".png"), ("jpg files", ".jpg .jpeg")),
        )
        theImage = ImageTk.PhotoImage(Image.open(filename))

        # Checks if loaded image is greater than designated size or not
        if theImage.width() < WIDTH // 2 and theImage.height() < HEIGHT // 2:
            showImage = tk.Label(canvas, image=theImage).place(relx=0.5, rely=0.3, anchor="center")
        else:
            theImage = ImageTk.PhotoImage(Image.open(filename).resize((600, 600), Image.ANTIALIAS))
            showImage = tk.Label(canvas, image=theImage).place(relx=0.5, rely=0.4, anchor="center")

        # Buttons
        widgets.confirmButton(canvas, root, 0.5, 0.85, 0.15, 0.05)
    except:
        mainWindow(root)