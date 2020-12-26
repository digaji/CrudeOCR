import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np

def convertSingleToPredict(image):
    """Converts a single image to model readable format (ndarray (1, 28, 28, 1))

    Args:
        image (ndarray): 3 dimensional numpy array

    Returns:
        ndarray: 4 dimensional numpy array (1, 28, 28, 1)
    """
    image = image.reshape(1, 28, 28, 1) 
    return image