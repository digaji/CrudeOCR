import tkinter as tk
from tkinter import messagebox
import cv2 as cv
import numpy as np
from components import frames

# * -- Image Functions -- * #
def convertSingleToPredict(image):
    """
    Converts a single image to model readable format (ndarray (1, 28, 28, 1))
    """
    image = image.reshape(1, 28, 28, 1) 
    return image


def rescaleDimensions(image, maxWidth, maxHeight):
    """
    Returns rescaled image that's below max width and height (aspect ratio kept)
    """
    factor = maxHeight / float(image.shape[0])
    if maxWidth / float(image.shape[1]) < factor:
        factor = maxWidth / float(image.shape[1])

    return cv.resize(image, None, fx=factor, fy=factor, interpolation=cv.INTER_LINEAR)


# * -- Button Functions -- * #
def deleteLastImage(root):
    """ delButton function
    Removes last image in imageList (if empty, returns to mainFrame)
    """
    if len(frames.imageList) > 1:
        frames.imageList.pop()
        messagebox.showinfo("Deleted", "Previous image deleted!")
    else:
        frames.mainFrame(root)


def backWebcam(root):
    """ backWebcamButton function
    Stops webcam frame and returns back to mainFrame
    """
    frames.webcam.stopCam()
    frames.webcam.destroy()
    frames.mainFrame(root)


# * -- Misc. Functions -- * #
def checkFrame():
    """ Every Frame function
    """
    for widget in frames.frame.winfo_children():
        widget.destroy()
