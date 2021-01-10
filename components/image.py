import cv2 as cv
import numpy as np
import imutils
from imutils.contours import sort_contours
from components import frames, commands

# * -- Image class for any images inputted into CrudeOCR -- * #
class Image:
	def __init__(self, source, textOption):
		self.__source = source
		self.__characters = []

		self.__image = cv.imread(self.__source)  # Takes in image from source filepath

		# Resizes image to designated max resolution while keeping aspect ratio
		self.__image = commands.rescaleDimensions(self.__image, maxWidth=1280, maxHeight=720)

		# Converts image to grayscale
		self.__gray = cv.cvtColor(self.__image, cv.COLOR_BGR2GRAY)

		# Processing functions depending on the type of text that's being processed
		if textOption == "Multiple Lines":
		    self.multiLine(self.__gray)
		elif textOption == "Multiple Words":
		    self.multiWord(self.__gray)
		else:
			self.singleWord(self.__gray)

	@staticmethod
	def preprocess(image):
		""" Default preprocessing for images
		"""
		preprocessed = cv.GaussianBlur(image, (5, 5), 0)  # Applies blur to image to reduce potential noise
		preprocessed = cv.Canny(preprocessed, 30, 150)  # Finds canny edges in the image in between 2 threshold values
		return preprocessed

	def multiLine(self, image):
		""" For images with text that has more than one line
		"""
		imagePreprocessed = self.preprocess(image)
		# Grab image thresholds according to appropriate blockSize
		imagePreprocessed = cv.adaptiveThreshold(imagePreprocessed, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, blockSize=11, C=2)  # 11 to cover each line

		rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (100, 5))  # 100 to cover each line, 5 to get enough height in 2 part letters (e.g. i, j)
		# Dilate then erode the image to get a shape that covers a specific area (depends on rect_kernel size)
		imagePreprocessed = cv.morphologyEx(imagePreprocessed, cv.MORPH_CLOSE, rect_kernel)

		try:
			# Finds contours of each line and sorts them from top to bottom
			contours = cv.findContours(imagePreprocessed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[0]
			contours = sort_contours(contours, method="top-to-bottom")[0]

			# Loops through contour of each line to find characters
			for contour in contours:
				copy = image.copy()
				(x, y, width, height) = cv.boundingRect(contour)
				self.region = copy[y: y + height, x: x + width]
				self.multiWord(self.region)
				self.__characters.append("\n")
		except:
			pass

	def multiWord(self, image):
		""" For images with text that has multiple words, but only in one line
		"""
		imagePreprocessed = self.preprocess(image)
		# Grab image thresholds according to appropriate blockSize
		imagePreprocessed = cv.adaptiveThreshold(imagePreprocessed, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, blockSize=7, C=2)  # 7 to cover only each word

		rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (30, 5))  # 30 to cover each word, 5 to get enough height in 2 part letters (e.g. i, j)
		# Dilate then erode the image to get a shape that covers a specific area (depends on rect_kernel size)
		imagePreprocessed = cv.morphologyEx(imagePreprocessed, cv.MORPH_CLOSE, rect_kernel)

		try:
			# Finds contours of each word and sorts them from left to right
			contours = cv.findContours(imagePreprocessed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[0]
			contours = sort_contours(contours, method="left-to-right")[0]

			# Loops through contour of each word to find characters
			for contour in contours:
				copy = image.copy()
				(x, y, width, height) = cv.boundingRect(contour)
				self.region = copy[y: y + height, x: x + width]
				self.singleFromMulti(self.region)
				self.__characters.append(" ")
		except:
			pass

	def singleWord(self, image):
		""" For images with text that has only one word
		"""
		imagePreprocessed = self.preprocess(image)
		# Grab image thresholds according to appropriate blockSize
		imagePreprocessed = cv.adaptiveThreshold(imagePreprocessed, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, blockSize=3, C=2)  # 3 to cover only each character

		rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 5))  # 1 to cover each character, 5 to get enough height in 2 part letters (e.g. i, j)
		# Dilate then erode the image to get a shape that covers a specific area (depends on rect_kernel size)
		imagePreprocessed = cv.morphologyEx(imagePreprocessed, cv.MORPH_CLOSE, rect_kernel)  

		try:
			# Finds contours of each character and sorts them from left to right
			contours = cv.findContours(imagePreprocessed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[0]
			contours = sort_contours(contours, method="left-to-right")[0]

			# Sorts contours into function for finding characters
			self.region = image
			self.characterFinder(contours)
			self.__characters.append(" ")
		except:
			pass

	def singleFromMulti(self, image):
		""" For images that come from multiWord
		"""
		imagePreprocessed = self.preprocess(image)
		# Grab image thresholds according to appropriate blockSize
		imagePreprocessed = cv.adaptiveThreshold(imagePreprocessed, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, blockSize=3, C=2)  # 3 to cover only each character

		# Finds contours of each character and sorts them from left to right
		contours = cv.findContours(imagePreprocessed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)[0]
		contours = sort_contours(contours, method="left-to-right")[0]

		# Sorts contours into function for finding characters
		self.characterFinder(contours)

	def characterFinder(self, contours):
		""" Loops through each contour to find characters and appends prediction to self.__characters list
		"""
		for contour in contours:
			# Find the bounding box contour
			(x, y, width, height) = cv.boundingRect(contour)

			# Get the character's region to be thresholded
			region = self.region[y: y + height, x: x + width]
			# Threshold the image to either 0 (black) or 255 (white) using Otsu's method
			threshold = cv.threshold(region, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
			# Get the current dimensions of the threholded region
			(thresholdHeight, thresholdWidth) = threshold.shape

			# Resize to fit model prediction shape
			if thresholdWidth > thresholdHeight:
			    threshold = imutils.resize(threshold, width=28)
			else:
			    threshold = imutils.resize(threshold, height=28)

			# Get the new dimensions of the region
			(thresholdWidth, thresholdHeight) = threshold.shape
			# Determine how much padding is needed for the image to be 28x28
			padX = int(max(0, 28 - thresholdWidth) / 2.0)
			padY = int(max(0, 28 - thresholdHeight) / 2.0)

			# Pad the thresholded image with invisible border and force the size to be 28x28
			padded = cv.copyMakeBorder(threshold, top=padY, bottom=padY, left=padX, right=padX, borderType=cv.BORDER_CONSTANT, value=(0, 0, 0))
			final = cv.resize(padded, (28, 28))

			# Convert the threshold image for model prediction
			final = final.astype("float32") / 255.0
			final = np.expand_dims(final, axis=-1)  # Adds 1 colour channel to the thresholded image (now it will be (28, 28, 1))
			final = np.expand_dims(final, axis=0)  # Adds 1 dimension to the front of the thresholded image (now it will be (1, 28, 28, 1))

			# Predict the final image with loaded model and append the result to character list
			prediction = frames.model.predict(final)
			self.__characters.append(prediction)

	def getPrediction(self):
		""" Returns character list from image
		"""
		return self.__characters
