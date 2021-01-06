import tkinter as tk
from tkinter import filedialog, messagebox
import cv2 as cv
import numpy as np
from PIL import ImageTk, Image
from components import frames, image

# TODO: Add commands for the rest

# * Image Functions
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


# * Misc. Functions
def deleteLastImage(root):
    """
    Removes last image in imageList (if empty, returns to mainFrame)
    """
    if len(frames.imageList) > 1:
        frames.imageList.pop()
        messagebox.showinfo("Deleted", "Previous image deleted!")
    else:
        frames.mainFrame(root)