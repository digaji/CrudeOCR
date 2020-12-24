import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Hide initial log outputs from Tensorflow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.regularizers import l2
import numpy as np
import tensorflow_datasets as tfds
from time import time

# Configuration for GPU
physical_devices = tf.config.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

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

IMG_HEIGHT = len(raw_imagesTrain[0])
IMG_WIDTH = len(raw_imagesTrain[1])
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

imagesShape = imagesTrain.shape[1:]

# Converts to one-hot encoding
labelsTrain = keras.utils.to_categorical(raw_labelsTrain)
labelsTest = keras.utils.to_categorical(raw_labelsTest)


class Model:
    labelsReal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    LABELS_LENGTH = len(labelsReal)
    def __init__(self, name, trainImages, trainLabels, testImages, testLabels):
        self.__name = name
        self.__trainImages = trainImages
        self.__trainLabels = trainLabels
        self.__testImages = testImages
        self.__testLabels = testLabels
        print(f"Model {name} created!")
        self.__callbacks = [
            tf.keras.callbacks.EarlyStopping(
                monitor="val_accuracy", verbose=1, patience=120, mode="max"
            ),
            tf.keras.callbacks.TensorBoard(log_dir="models/"),
            tf.keras.callbacks.TerminateOnNaN(),
        ]

    def createNetwork(self):
        self.model = keras.models.Sequential()

        # 2 stacked Convolutional layers
        self.model.add(
            Conv2D(
                16,
                kernel_size=(3, 3),
                input_shape=imagesShape,
                activation="relu",
                padding="same",
            )
        )
        self.model.add(
            Conv2D(
                32,
                kernel_size=(3, 3),
                activation="relu",
                padding="same",
                kernel_regularizer=l2(0.001),
            )
        )
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.2))  # Reducing chances of overfitting
        # 2 stacked Convolutional layers
        self.model.add(
            Conv2D(
                32,
                kernel_size=(3, 3),
                activation="relu",
                padding="same",
                kernel_regularizer=l2(0.001),
            )
        )
        self.model.add(
            Conv2D(
                32,
                kernel_size=(3, 3),
                activation="relu",
                padding="same",
                kernel_regularizer=l2(0.001),
            )
        )
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.5))  # Reducing chances of overfitting
        # Flatten results before going to Dense layer
        self.model.add(Flatten())
        # 4 hidden layers
        self.model.add(Dense(512, activation="relu", kernel_regularizer=l2(0.001)))
        self.model.add(Dense(256, activation="relu"))
        self.model.add(Dense(128, activation="relu"))
        self.model.add(Dense(64, activation="relu"))
        # Final output layer
        self.model.add(Dense(self.LABELS_LENGTH, activation="softmax"))

        # Compile the model
        self.model.compile(
            optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
        )
        print("Network created!")

    def save(self):
        self.model.save(f"models/{self.__name}.h5")
        print(f"Model {self.__name} saved!\n")

    def load(self):
        self.model = keras.models.load_model(f"models/{self.__name}.h5")
        print(f"Model {self.__name} loaded!\n")
        return self.model

    def train(self, epochs: int, batchSize: int):
        startTime = time()
        try:
            self.model.fit(
                self.__trainImages,
                self.__trainLabels,
                epochs=epochs,
                batch_size=batchSize,
                validation_data=(self.__testImages, self.__testLabels),
                callbacks=self.__callbacks,
            )
        except tf.errors.ResourceExhaustedError:
            print(
                f"Batch size of {batchSize} is too large! Try using a smaller amount."
            )
        else:
            print(f"Training took {time() - startTime} seconds to run.\n")

    @property
    def info(self):
        print(f"Summary for model: {self.__name}")
        return self.model.summary()

    def predict(self, image):
        predictions = []
        prediction = self.model.predict(image)
        for i in range(len(prediction)):
            predictions.append(self.labelsReal[np.argmax(prediction[i])])
        return predictions

    def evaluate(self, batchSize: int):
        try:
            print(f"Starting evaluate process for {self.__name}!")
            self.model.evaluate(
                self.__testImages, self.__testLabels, batch_size=batchSize
            )
        except tf.errors.ResourceExhaustedError:
            print(
                f"Batch size of {batchSize} is too large! Try using a smaller amount."
            )

def convertSingleToPredict(image):
    """Converts a single image to model readable format (ndarray (1, 28, 28, 1))

    Args:
        image (ndarray): 3 dimensional numpy array

    Returns:
        ndarray: 4 dimensional numpy array (1, 28, 28, 1)
    """
    image = image.reshape(1, IMG_WIDTH, IMG_HEIGHT, 1) 
    return image


# # Testing Area (uncomment to test models)
# import matplotlib.pyplot as plt
# CrudeV5 = Model("CrudeV5", imagesTrain, labelsTrain, imagesTest, labelsTest)
# CrudeV5.load()

# CrudeV6 = Model("CrudeV6", imagesTrain, labelsTrain, imagesTest, labelsTest)
# CrudeV6.load()

# CrudeV5.evaluate(16384)
# CrudeV6.evaluate(16384)
# test3 = imagesTest[10090:10092]
# print(test3.shape)

# plt.imshow(test3[0], cmap="gray")
# plt.show()
# plt.imshow(test3[1], cmap="gray")
# plt.show()

# print(CrudeV5.predict(test3))
# print(CrudeV6.predict(test3))

# # To create your own model
# CrudeCommunity = Model("CrudeCommunity", imagesTrain, labelsTrain, imagesTest, labelsTest)
# CrudeCommunity.createNetwork()
# CrudeCommunity.train(epochs=3, batchSize=128)
# CrudeCommunity.save()
# CrudeCommunity.info
# CrudeCommunity.evaluate(batchSize=128)
