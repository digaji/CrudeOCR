# Crude OCR - Final Project for PDM Semester 1
Crude OCR is an OCR interpretation using Machine Learning as a base. It is able to interpret text from a written document in the form of a PNG or JPG file, as well as straight from the webcam. 

Results from the analysis will be in the form of plain text, which can then be copied for further use. There is also an option for the text to be read aloud through text-to-speech.

## Configuration
1. Git clone the project
```PowerShell
git clone https://github.com/digaji/CrudeOCR.git
```
2. CD into the project
```Powershell
cd CrudeOCR
```

3. Create virtual environment (Python version for this project == 3.8.6)
```PowerShell
python -m venv venv
```

3. Activate the virtual environment
```PowerShell
# For Windows
venv/Scripts/activate
# For Mac or Linux
. venv/bin/activate
```

4. Install the required libraries
```PowerShell
pip install -r requirements.txt
```

5. Run the main.py file
```PowerShell
python main.py
```
Or you know... you can also use GitHub Desktop...
## Notice for Mac Users
The playsound module currently doesn't work by itself. To get around this, do
```zsh
pip install PyObjC
``` 

---

**The current way that the testFrame works to grab an image of the canvas is broken on Mac. There is currently no workaround for that problem hence, testFrame doesn't work on Mac.**

---

When opening the webcam, macOS tends to ask the user to allow camera permission for the app that's opening it. In the case that it doesn't, the app needs to be run with **sudo** permissions.  
An example with Visual Studio Code
```zsh
sudo /Applications/Visual\ Studio\ Code.app/Contents/MacOS/Electron
```

## For Model Training / Testing
**For NVIDIA GPU Owners**, follow the instructions in this [link](https://www.tensorflow.org/install/gpu) for faster model processing

The dataset used for the current model, and how it's set up, is in data/data.py

Data is saved in .pickle format for quicker access during model training

Follow the comments and directions in data/README.md and model.py to test new / existing models