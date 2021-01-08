import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2 as cv
from model import Model
from components import widgets, commands
from components.widgets import Camera, TestAI

# TODO: Implement command after confirm button clicked
# TODO: Implement resultFrame

# * -- Variables -- * #
model = Model("CrudeV8")
imageList = []

# * -- Initialization Function -- * #
def initialize(root):
    global frame
    frame = tk.Frame(root, bg="white")
    frame.pack(side="top", expand=True, fill="both")

    # Loads in prediction model
    model.load()

    # Loads in mainFrame
    mainFrame(root)


# * -- Frames -- * #
def mainFrame(root):
    commands.checkFrame()
    imageList.clear()

    # Label
    tk.Label(frame, text="Crude OCR", font="Helvetica 100", bg="white").place(relx=0.5, rely=0.2, anchor="center")

    # Buttons
    widgets.webcamButton(frame, root, x=0.3, y=0.7, width=0.15, height=0.05)
    widgets.fileButton(frame, root, x=0.7, y=0.7, width=0.15, height=0.05)
    widgets.testButton(frame, root, x=0.5, y=0.8, width=0.15, height=0.05)


def webcamFrame(root):
    global webcam
    commands.checkFrame()

    # Webcam
    webcam = Camera(root, relx=0.5, rely=0.4, camNumber=0, resolution=(640, 480))

    # Buttons
    widgets.backWebcamButton(frame, root, x=0.5, y=0.9, width=0.15, height=0.05)


def fileFrame(root):
    global tkImage
    commands.checkFrame()

    # Opens and converts image to TkInter readable format
    try:
        # Asks the user to pick a jpeg or png file
        filepath = filedialog.askopenfilename(
            title="Select A File",
            filetypes=(("jpg files", ".jpg .jpeg"), ("png files", ".png")),
        )
        rawImage = cv.imread(filepath)

        # Converts from default OpenCV color space of BGR to RGB
        tkImage = cv.cvtColor(rawImage, cv.COLOR_BGR2RGB)

        # Rescales image to just below half of frame dimensions while keeping aspect ratio
        tkImage = commands.rescaleDimensions(tkImage, frame.winfo_width() // 2, frame.winfo_height() // 2)
        
        # Converting from normal image array to TkInter readable format
        tkImage = Image.fromarray(tkImage)
        tkImage = ImageTk.PhotoImage(tkImage)

        # Appends original image filepath to list for predictions
        imageList.append(filepath)
        
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
    global canvas
    commands.checkFrame()

    # Image
    canvas = TestAI(frame, relx=0.5, rely=0.5, width=500, height=500, background="black", highlightthickness=10, highlightbackground="gray")

    # Label
    tk.Label(frame, text="Draw Here!", font="Helvetica 70", bg="white").place(relx=0.5, rely=0.1, anchor="center")

    # Buttons
    widgets.backButton(frame, root, x=0.85, y=0.9, width=0.15, height=0.05)
