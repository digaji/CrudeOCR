from tkinter import messagebox
import cv2 as cv
from PIL import ImageGrab
from gtts import gTTS
from playsound import playsound
from os import remove
from components import frames, widgets
from components.image import Image

# * -- webcamFrame -- * #
def confirmWebcam(root):
    """confirmWebcamButton function |
    Takes photo and stops the webcam. Appends the photo to imageList as an Image class object with chosen textOption.
    Passes on to resultFrame
    """
    frames.webcam.takePhoto()
    frames.webcam.stopCam()
    frames.webcam.destroy()

    webcamImage = frames.fileList[-1]
    frames.imageList.append(Image(webcamImage, widgets.clicked.get()))

    frames.resultFrame(root)


def switchCamNumber():
    """Temporary function for switching which webcam is open (currently used in switchWebcamButton) |
    Switches video capture between webcam 0 and 1
    """
    if frames.webcam.camNumber == 0:
        frames.webcam.setCamNumber(1)
    else:
        frames.webcam.setCamNumber(0)


def backWebcam(root):
    """backWebcamButton function |
    Stops webcam frame and returns back to mainFrame
    """
    frames.webcam.stopCam()
    frames.webcam.destroy()
    frames.mainFrame(root)


# * -- fileFrame -- * #
def addFile(root):
    """addFileButton function |
    Gets the latest image and creates an Image class object from imageList and appends it to the predictionList along with the chosen textOption
    """
    latestImage = frames.fileList[-1]
    frames.imageList.append(Image(latestImage, widgets.clicked.get()))

    frames.fileFrame(root)


def confirmFile(root):
    """confirmFileButton function |
    Gets the latest image and creates an Image class object from imageList and appends it to the predictionList along with the chosen textOption.
    Passes on to resultFrame
    """
    latestImage = frames.fileList[-1]
    frames.imageList.append(Image(latestImage, widgets.clicked.get()))

    frames.resultFrame(root)


def deleteFile(root):
    """delFileButton function |
    Removes last image in fileList and imageList (if empty, returns to mainFrame)
    """
    if len(frames.fileList) > 1:
        frames.fileList.pop(-2)  # -2 to remove image before the current one
        frames.imageList.pop()
        messagebox.showinfo(title="Deleted", message="Previous image deleted!")
    else:
        frames.mainFrame(root)


# * -- testFrame -- * #
def confirmAI(root):
    """confirmAIButton function |
    Takes a screenshot of the AI canvas and creats an Image class object for prediction.
    Also triggers messageBox for prediction result
    """
    finalPath = "images/Canvas.png"

    # Grab the location of the canvas within the frame
    x = root.winfo_rootx() + frames.canvas.winfo_x()
    y = root.winfo_rooty() + frames.canvas.winfo_y()
    width = x + frames.canvas.winfo_width()
    height = y + frames.canvas.winfo_height()
    # Take a screenshot of the canvas and save it to the file path
    ImageGrab.grab((x, y, width, height)).save(finalPath)

    # Get the prediction for the canvas
    canvasImage = Image(finalPath, "Single Word")
    prediction = canvasImage.getPrediction()[0]

    # Show prediction in messageBox and ask user if they want to draw again or not
    messageBox = messagebox.askquestion(title="Prediction", message=f"This could be a: {prediction}\nDraw again?")
    if messageBox == "yes":
        frames.testFrame(root)
    else:
        frames.mainFrame(root)


# * -- resultFrame -- * #
def speechResult(text):
    """speechButton function |
    Reads text and plays its audio
    """
    audio = gTTS(text=text, lang="en")
    audio.save("audio.mp3")
    playsound("audio.mp3")
    remove("audio.mp3")


# * -- Misc. Functions -- * #
def checkFrame():
    """Every Frame function |
    Deletes all widgets from the frame
    """
    for widget in frames.frame.winfo_children():
        widget.destroy()


def rescaleDimensions(image, maxWidth, maxHeight):
    """Image resizing function |
    Returns rescaled image that's below max width and height (aspect ratio kept)
    """
    factor = maxHeight / float(image.shape[0])
    if maxWidth / float(image.shape[1]) < factor:
        factor = maxWidth / float(image.shape[1])

    return cv.resize(image, None, fx=factor, fy=factor, interpolation=cv.INTER_LINEAR)
