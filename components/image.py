import cv2 as cv
import numpy as np

# TODO: Get this one sorted

# Image class for any images inputted into CrudeOCR
class Image:
    def __init__(self, source):
        self.__source = source
        self.rotation = 0

    def edge(self):
        pass

    def denoise(self):
        pass

    def toPredict(self):
        predictList = []
        pass