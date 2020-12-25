import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Hide initial log outputs from Tensorflow
from tensorflow import keras
import numpy as np
import tensorflow_datasets as tfds
import pickle

# # * Configuration for CUDA-enabled GPUs (UNCOMMENT)
# physical_devices = tf.config.list_physical_devices("GPU")
# tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

# * Run this file to reconstruct dataset into Pickle format

dataTrain, dataTest = tfds.as_numpy(
    tfds.load(  # as_numpy to get the dataset as numpy arrays
        "emnist",
        split=["train", "test"],
        batch_size=-1,  # Loads the full dataset in a single batch
        shuffle_files=True,
        as_supervised=True,  # Returns a tuple instead of dictionary
    )
)

# Split data into images and labels
raw_imagesTrain, raw_labelsTrain = dataTrain
raw_imagesTest, raw_labelsTest = dataTest

IMG_HEIGHT = 28
IMG_WIDTH = 28
shape = IMG_WIDTH * IMG_HEIGHT

# Reshapes to 1-Dimensional layer of size 28x28 -> 784
imagesTrain = raw_imagesTrain.reshape(len(raw_imagesTrain), shape)
imagesTest = raw_imagesTest.reshape(len(raw_imagesTest), shape)


def rotate(image):
    image = image.reshape([IMG_HEIGHT, IMG_WIDTH])  # Reshapes back to 28x28
    image = np.fliplr(image)
    image = np.rot90(image)
    return image


# Rotate and reshape all images in the dataset
imagesTrain = np.apply_along_axis(rotate, 1, imagesTrain)
imagesTest = np.apply_along_axis(rotate, 1, imagesTest)

# Converts from uint8 to float32
imagesTrain = imagesTrain.astype("float32")
imagesTest = imagesTest.astype("float32")

# Normalization of bytes (reduces values to range from 0 - 1 only)
imagesTrain /= 255
imagesTest /= 255

# Reshape for Tensorflow (batch, width, height, colour channel)
imagesTrain = imagesTrain.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 1)  # -1 batch size to include everything
imagesTest = imagesTest.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 1)

# Converts to one-hot encoding
labelsTrain = keras.utils.to_categorical(raw_labelsTrain)
labelsTest = keras.utils.to_categorical(raw_labelsTest)

# Export data as Pickle format
pickle_out = open("data/imagesTrain.pickle", "wb")
pickle.dump(imagesTrain, pickle_out)
pickle_out.close()

pickle_out = open("data/labelsTrain.pickle", "wb")
pickle.dump(labelsTrain, pickle_out)
pickle_out.close()

pickle_out = open("data/imagesTest.pickle", "wb")
pickle.dump(imagesTest, pickle_out)
pickle_out.close()

pickle_out = open("data/labelsTest.pickle", "wb")
pickle.dump(labelsTest, pickle_out)
pickle_out.close()
