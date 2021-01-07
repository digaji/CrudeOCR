import tkinter as tk
from tkinter import messagebox
import cv2 as cv
import numpy as np
from components import frames, image

# * -- Image Functions -- * #
def convertSingleToPredict(image):
    """
    Converts a single image to model readable format (ndarray (1, 28, 28, 1))
    """
    image = image.reshape(1, 28, 28, 1) 
    return image


def rescaleDimensions(image):
    """
    Returns rescaled image that's below max width and height (aspect ratio kept)
    """
    MAX_HEIGHT = 600
    MAX_WIDTH = 800
    
    factor = MAX_HEIGHT / float(image.shape[0])
    if MAX_WIDTH / float(image.shape[1]) < factor:
        factor = MAX_WIDTH / float(image.shape[1])

    return cv.resize(image, None, fx=factor, fy=factor, interpolation=cv.INTER_AREA)


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
