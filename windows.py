import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

## TODO: Implement command after confirm button clicked
## TODO: Implement analyzing window

# Starting Resolution
HEIGHT = 800
WIDTH = 1280

def mainWindow(frame):
    main = tk.Canvas(frame, height=HEIGHT, width=WIDTH, bg="white").pack()

    # Title
    title = tk.Label(main, text="Crude OCR", font="Helvetica 100", bg="white")
    title.place(relx=0.5, rely=0.2, anchor="center")

    # Buttons
    buttonWebcam = tk.Button(main, text="Start Webcam", bg="#a8cbff", command=lambda: webcamWindow(frame))
    buttonWebcam.place(relx=0.3, rely=0.7, anchor="center", relwidth=0.15, relheight=0.05)

    buttonFile = tk.Button(main, text="Open File", bg="#ff7272", command=lambda: fileWindow(frame))
    buttonFile.place(relx=0.7, rely=0.7, anchor="center", relwidth=0.15, relheight=0.05)

    buttonTest = tk.Button(main, text="Test the AI!")
    buttonTest.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.15, relheight=0.05)

def webcamWindow(frame):
    webcamFrame = tk.Toplevel(frame, height=HEIGHT, width=WIDTH, bg="white")
    webcamFrame.title("Webcam")

    # Title
    title = tk.Label(webcamFrame, text="Crude OCR", font="Helvetica 100", bg="white")
    title.place(relx=0.5, rely=0.1, anchor="center")

    # Buttons
    backButton = tk.Button(webcamFrame, text="Back", bg="#ff7272", command=webcamFrame.destroy)
    backButton.place(relx=0.85, rely=0.9, anchor="center", relwidth=0.15, relheight=0.05)

def fileWindow(frame):
    global theImage

    filename = filedialog.askopenfilename(title="Select A File", filetypes=(("png files", ".png"), ("jpg files", ".jpg .jpeg")))
    theImage = ImageTk.PhotoImage(Image.open(filename))

    fileFrame = tk.Toplevel(frame, height=HEIGHT, width=WIDTH, bg="white")
    if theImage.width() < 800 and theImage.height() < 600:
        showImage = tk.Label(fileFrame, image=theImage).place(relx=0.5, rely=0.3, anchor="center")
    else:
        theImage = ImageTk.PhotoImage(Image.open(filename).resize((600, 600), Image.ANTIALIAS))
        showImage = tk.Label(fileFrame, image=theImage).place(relx=0.5, rely=0.4, anchor="center")

    confirmButton = tk.Button(fileFrame, text="Confirm?", command=fileFrame.destroy)
    confirmButton.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.15, relheight=0.05)
