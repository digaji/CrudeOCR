import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2 as cv
from model import Model
from components import widgets, commands

# TODO: Implement command after confirm button clicked
# TODO: Implement analyzing window

# Starting Resolution
HEIGHT = 800
WIDTH = 1280

# Desired model
model = Model("CrudeV8")

def initialize(root):
    global frame
    frame = tk.Frame(root, bg="white")
    frame.pack(side="top", expand=True, fill="both")

    # Loads in prediction model
    model.load()

    mainFrame(root)


# Function for frame checking
def checkFrame():
    for widget in frame.winfo_children():
        widget.destroy()


def mainFrame(root):
    checkFrame()
    imageList.clear()

    # Title
    widgets.title(frame, 0.5, 0.2)

    # Buttons
    widgets.webcamButton(frame, root, x=0.3, y=0.7, width=0.15, height=0.05)
    widgets.fileButton(frame, root, x=0.7, y=0.7, width=0.15, height=0.05)
    widgets.testButton(frame, root, x=0.5, y=0.8, width=0.15, height=0.05)


def webcamFrame(root):
    checkFrame()

    # Buttons
    widgets.backButton(frame, root, x=0.5, y=0.9, width=0.15, height=0.05)


imageList = []
def fileFrame(root):
    global tkImage
    checkFrame()

    # Opens and converts image to TkInter readable format
    try:
        # Asks the user to pick a jpeg or png file
        filepath = filedialog.askopenfilename(
            title="Select A File",
            filetypes=(("jpg files", ".jpg .jpeg"), ("png files", ".png")),
        )
        rawImage = cv.imread(filepath)

        # Converts from default OpenCV color space of BGR to RGB
        rawImage = cv.cvtColor(rawImage, cv.COLOR_BGR2RGB)

        # Checks if loaded image is greater than designated size or not
        if rawImage.shape[1] < frame.winfo_width() // 2 and rawImage.shape[0] < frame.winfo_height():
            pass
        else:
            rawImage = commands.rescaleDimensions(rawImage)

        # Converting from normal image array to TkInter readable format
        tkImage = Image.fromarray(rawImage)
        tkImage = ImageTk.PhotoImage(tkImage)

        # Appends grayscaled image to list for predictions
        imageList.append(rawImage)
        
        # Image
        tk.Label(frame, image=tkImage, highlightthickness=10, highlightbackground="gray").place(relx=0.5, rely=0.4, anchor="center")

        # Buttons
        widgets.addButton(frame, root, x=0.85, y=0.85, width=0.15, height=0.05)
        widgets.confirmButton(frame, root, x=0.5, y=0.85, width=0.15, height=0.05)
        widgets.delButton(frame, root, x=0.15, y=0.85, width=0.15, height=0.05)
        widgets.backButton(frame, root, x=0.5, y=0.95, width=0.15, height=0.05)
    except:
        # If user clicked cancel on file dialog
        mainFrame(root)


def testFrame(root):
    checkFrame()

    # Image
    canvas = widgets.TestAI(frame, width=500, height=500, background="black", highlightthickness=10, highlightbackground="gray")
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Label
    tk.Label(frame, text="Draw Here!", font="Helvetica 70", bg="white").place(relx=0.5, rely=0.1, anchor="center")

    # Buttons
    widgets.backButton(frame, root, x=0.85, y=0.9, width=0.15, height=0.05)