[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://bitbucket.org/lbesson/ansi-colors)
# Crude OCR - Final Project for PDM Semester 1
Crude OCR is an OCR interpretation using Machine Learning as a base. It is able to interpret text from a written document in the form of a PNG or JPG file, as well as straight from the webcam. 

Results from the analysis will be in the form of plain text, which can then be copied for further use. There is also an option for the text to be read aloud through text-to-speech.

## Configuration
1. Git clone and cd into the folder
```
git clone https://github.com/digaji/CrudeOCR.git
cd CrudeOCR
```

2. Create virtual environment (Python version for this project == 3.8.6)
```
python -m venv venv
```

3. Activate the virtual environment and install the required libraries
```
venv/Scripts/activate
pip install -r requirements.txt
```

4. Run the main.py file
```
python main.py
```

## For model training / testing
For NVIDIA GPU Owners, follow the instructions in this [link](https://www.tensorflow.org/install/gpu) for faster model processing

The dataset used for the current model, and how it's set up, is in data/data.py

Data is saved in .pickle format for quicker access during model training

Follow the comments and directions in data/README.md and model.py to test new / existing models