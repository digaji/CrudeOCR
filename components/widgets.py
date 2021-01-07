import tkinter as tk
from tkinter import ttk
import cv2 as cv
from PIL import Image, ImageTk
import datetime as dt
from components import frames, commands

# * -- Widgets -- * #
def title(frame, x, y):
    tk.Label(frame, text="Crude OCR", font="Helvetica 100", 
	bg="white").place(relx=x, rely=y, anchor="center")


def webcamButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Start Webcam", bg="#a8cbff", 
	command=lambda: frames.webcamFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def fileButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Open File", bg="#ff7272", 
	command=lambda: frames.fileFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def testButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Test the AI!", bg="#f0f0f0", 
	command=lambda: frames.testFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def backButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Back", bg="#ff7272", 
	command=lambda: frames.mainFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def backWebcamButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Back", bg="#ff7272", 
	command=lambda: commands.backWebcam(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def confirmButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Confirm?", bg="#f0f0f0", 
	command=lambda: frames.mainFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def addButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Add More Images", bg="#a8cbff", 
	command=lambda: frames.fileFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def delButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Delete Last Image", bg="#ff7272", 
	command=lambda: commands.deleteLastImage(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def textField(frame, x, y, width, height):
    pass


def scrollbarText(frame):
    pass


class TestAI(tk.Canvas):
    def __init__(self, parent, relx, rely, **kwargs):
        super().__init__(parent, **kwargs)
        self.relx = relx
        self.rely = rely

        # Mouse bindings for painting
        self.bind("<Button-1>", self.lastPos)
        self.bind("<B1-Motion>", self.addLine)

        # Place the canvas in the desired location
        self.place(relx=self.relx, rely=self.rely, anchor="center")

    def lastPos(self, event):
        # Remembers the last position of the mouse click
        self.lastX, self.lastY = event.x, event.y

    def addLine(self, event):
        # Creates lines for painting
        self.create_line(self.lastX, self.lastY, event.x, event.y, fill="white", width=5)
        self.lastPos(event)


class Camera(tk.Label):
	def __init__(self, parent, relx, rely, camNumber=0, resolution=(640, 480), **kwargs):
		super().__init__(parent, **kwargs)
		self.width, self.height = resolution
		self.parent = parent
		self.relx = relx
		self.rely = rely

		# Start video capture
		self.capture = cv.VideoCapture(camNumber) 

		# Set video capture to designated resolution
		self.capture.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
		self.capture.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)

		# Place the webcam in the desired location
		self.place(relx=self.relx, rely=self.rely, anchor="center")
		self.startCam()

	def setCamNumber(self, camNumber):
		self.capture = cv.VideoCapture(camNumber)

	def setResolution(self, resolution):
		self.width, self.height = resolution

		self.capture.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
		self.capture.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)
	
	def startCam(self):
		global frameTk

		# Starts webcam, else return to mainFrame
		try:
			# Take each frame from video capture and turn it into TkInter format
			self.frame = self.capture.read()[1]
			frameRaw = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)
			frameTk = Image.fromarray(frameRaw)
			frameTk = ImageTk.PhotoImage(frameTk)

			self.configure(image=frameTk)
			self.after(ms=10, func=self.startCam)
		except:
			frames.mainFrame(self.parent)

	def stopCam(self):
		self.capture.release()

	def takePhoto(self):
		cv.imwrite(f"images/{dt.datetime.now().strftime(r'%H-%M-%S_%d-%m-%Y')}.jpg", self.frame.copy())
		print("Image saved")
