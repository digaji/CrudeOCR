import tkinter as tk
import cv2 as cv
from PIL import Image, ImageTk
import datetime as dt

# Webcam Frame Label Class
class Camera(tk.Label):
	def __init__(self, parent, camNumber, resolution=(640, 480), **kwargs):
		super().__init__(parent, **kwargs)
		self.width, self.height = resolution

		# Start video capture
		self.capture = cv.VideoCapture(camNumber)

		# Set video capture to designated resolution
		self.capture.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
		self.capture.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)

		self.startCam()

	def setCamNumber(self, camNumber):
		self.capture = cv.VideoCapture(camNumber)

	def setResolution(self, resolution):
		self.width, self.height = resolution

		self.capture.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
		self.capture.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)
	
	def startCam(self):
		global frameTk
		try:
			# Take each frame from video capture and turn it into TkInter format
			self.frame = self.capture.read()[1]
			frameRaw = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)
			frameTk = Image.fromarray(frameRaw)
			frameTk = ImageTk.PhotoImage(frameTk)

			self.configure(image=frameTk)
			self.after(10, self.startCam)
		except:
			pass

	def stopCam(self):
		self.capture.release()
		self.takePhoto()

	def takePhoto(self):
		cv.imwrite(f"images/{dt.datetime.now().strftime(r'%H-%M-%S_%d-%m-%Y')}.jpg", self.frame.copy())
		print("Image saved")
