import tkinter as tk
import cv2 as cv
import numpy as np
from components import windows, image

# TODO: Add commands for the rest

# Image Adjustments
def convertToGrayscale(img: image):
    """
    Returns image that's grayscaled
    """
    img = cv.cvtColor(img, cv.COLOR_BAYER_BG2BGR)

def rotateClockwise(img: image):
    """
    Returns image that's rotated clockwise
    """
    (height, width) = img.shape[:2]
    rotationPoint = (width // 2, height // 2)
    rotationMatrix = cv.getRotationMatrix2D(rotationPoint, angle=(-90 + img.rotation), scale=1.0)  # Needed for warpAffine function
    dimensions = (width, height)

    img = cv.warpAffine(img, rotationMatrix, dimensions)

def rotateCounterClockwise(img: image):
    """
    Returns image that's rotated counterclockwise
    """
    (height, width) = img.shape[:2]
    rotationPoint = (width // 2, height // 2)
    rotationMatrix = cv.getRotationMatrix2D(rotationPoint, angle=(90 + img.rotation), scale=1.0)  # Needed for warpAffine function
    dimensions = (width, height)

    img = cv.warpAffine(img, rotationMatrix, dimensions)

def flip(img: image):
    """
    Returns image that's horizontally flipped
    """
    img = cv.flip(img, flipCode=1)  # flipCode of 1 returns horizontally flipped image
