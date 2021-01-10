import tkinter as tk
import cv2 as cv
from PIL import Image, ImageTk
import datetime as dt
from components import frames, commands

# * -- mainFrame -- * #
def webcamButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Start Webcam", bg="#a8cbff", 
	command=lambda: frames.webcamFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def fileButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Open File", bg="#ff7272", 
	command=lambda: frames.fileFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def testButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Test the AI!", bg="#f0f0f0", 
	command=lambda: frames.testFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


# * -- webcamFrame -- * #
class Camera(tk.Label):
	def __init__(self, parent, relx, rely, camNumber=0, resolution=(640, 480), **kwargs):
		super().__init__(parent, **kwargs)
		self.width, self.height = resolution
		self.relx = relx
		self.rely = rely
		self.camNumber = camNumber

		# Check if there's a camera available, else return to mainFrame
		try:
			# Start video capture
			self.capture = cv.VideoCapture(camNumber)

			# Set video capture to designated resolution
			self.capture.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
			self.capture.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)

			# Place the webcam in the desired location
			self.place(relx=self.relx, rely=self.rely, anchor="center")
			self.startCam()
		except:
			frames.mainFrame(self.parent)
			tk.messagebox.showerror(title="No Webcam", message="No Webcam detected on your machine!")

	def setCamNumber(self, camNumber):
		self.capture = cv.VideoCapture(camNumber)

	def setResolution(self, resolution):
		"""For future cases when higher resolution webcams are available
		"""
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
		"""Saves a screenshot of the webcam image and appends it to fileList
		"""
		self.photo = f"images/{dt.datetime.now().strftime(r'%H-%M-%S_%d-%m-%Y')}.jpg"
		cv.imwrite(self.photo, self.frame.copy())
		frames.fileList.append(self.photo)
		print("Image saved")


def confirmWebcamButton(frame, root, x, y, width, height):
	tk.Button(frame, text="Confirm?", bg="#f0f0f0", 
	command=lambda: commands.confirmWebcam(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def switchWebcamButton(frame, x, y, width, height):
	tk.Button(frame, text="Switch Webcam (if available)", bg="#a8cbff", 
	command=commands.switchCamNumber).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def backWebcamButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Back", bg="#ff7272", 
	command=lambda: commands.backWebcam(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


# * -- fileFrame -- * #
def confirmFileButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Confirm?", bg="#f0f0f0", 
	command=lambda: commands.confirmFile(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def addFileButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Add More Images", bg="#a8cbff", 
	command=lambda: commands.addFile(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def delFileButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Delete Last Image", bg="#ff7272", 
	command=lambda: commands.deleteFile(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


# * -- testFrame -- * #
class TestAI(tk.Canvas):
	def __init__(self, parent, relx, rely, **kwargs):
		super().__init__(parent, **kwargs)
		self.relx = relx
		self.rely = rely

		# Mouse bindings for painting
		self.bind("<Button-1>", self.lastPos)  # Mouse left click
		self.bind("<B1-Motion>", self.addLine)
		self.bind("<Button-3>", self.lastPos)  # Mouse right click
		self.bind("<B3-Motion>", self.delLine)

		# Place the canvas in the desired location
		self.place(relx=self.relx, rely=self.rely, anchor="center")

	def lastPos(self, event):
		# Remembers the last position of the mouse click
		self.lastX, self.lastY = event.x, event.y
		
	def addLine(self, event):
		# Creates lines for painting
		self.create_line(self.lastX, self.lastY, event.x, event.y, fill="black", width=10)
		self.lastPos(event)
	
	def delLine(self, event):
		# Deletes lines by painting in white
		self.create_line(self.lastX, self.lastY, event.x, event.y, fill="white", width=30)
		self.lastPos(event)


def confirmAIButton(frame, root, x, y, width, height):
	tk.Button(frame, text="Confirm?", bg="#f0f0f0", 
	command=lambda: commands.confirmAI(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


# * -- resultFrame -- * #
def textBox(frame, x, y, width, height):
	global text
	text = tk.Text(frame, width=width, height=height, font="Helvetica 20", highlightthickness=5)
	text.place(relx=x, rely=y, anchor="center")

	scrollbar = tk.Scrollbar(frame)
	scrollbar.place(relx=x + 0.4, rely=y - 0.25, anchor="center")

	# Bind textBox scroll vertical scroll to scrollbar
	text.config(yscrollcommand=scrollbar.set)
	scrollbar.config(command=text.yview)


def speechButton(frame, text, x, y, width, height):
	tk.Button(frame, text="Speech", bg="#a8cbff", 
	command=lambda: commands.speechResult(text)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


# * -- In multiple frames -- * #
def backButton(frame, root, x, y, width, height):
    tk.Button(frame, text="Back", bg="#ff7272", 
	command=lambda: frames.mainFrame(root)).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)


def textMenu(frame, x, y, width, height):
	global clicked
	options = ["Single Word", "Multiple Words", "Multiple Lines"]

	clicked = tk.StringVar()
	clicked.set(options[0])
	tk.OptionMenu(frame, clicked, *options).place(relx=x, rely=y, anchor="center", relwidth=width, relheight=height)
