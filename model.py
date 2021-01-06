import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Hide initial log outputs from Tensorflow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import numpy as np
from time import time, ctime

# # * Configuration for CUDA-enabled GPUs (UNCOMMENT)
# physical_devices = tf.config.list_physical_devices("GPU")
# tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

IMG_HEIGHT = 28
IMG_WIDTH = 28
shape = IMG_WIDTH * IMG_HEIGHT

# # * Import data from Pickle format (ONLY FOR TRAINING AND TESTING)
# import pickle
# imagesTrain = pickle.load(open("data/imagesTrain.pickle", "rb"))
# labelsTrain = pickle.load(open("data/labelsTrain.pickle", "rb"))
# imagesTest = pickle.load(open("data/imagesTest.pickle", "rb"))
# labelsTest = pickle.load(open("data/labelsTest.pickle", "rb"))

class Model:
    labelsReal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    LABELS_LENGTH = len(labelsReal)
    def __init__(self, name):
        self.__name = name
        print(f"Model = {name}")
        self.__callbacks = [
            tf.keras.callbacks.EarlyStopping(monitor="val_accuracy", verbose=1, patience=30, mode="max"),
            tf.keras.callbacks.TensorBoard(log_dir=f"models/logs/{self.__name} TB Logs"),
            tf.keras.callbacks.TerminateOnNaN(),
        ]

    def createNetwork(self):
        self.model = keras.models.Sequential()

        # 2 stacked Convolutional layers
        self.model.add(
            Conv2D(
                32,
                kernel_size=(3, 3),
                input_shape=(28, 28, 1),
                activation="relu",
            )
        )
        self.model.add(
            Conv2D(
                64,
                kernel_size=(3, 3),
                activation="relu"
            )
        )
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.2))  # Reducing chances of overfitting
        # 2 stacked Convolutional layers
        self.model.add(
            Conv2D(
                64,
                kernel_size=(3, 3),
                activation="relu"
            )
        )
        self.model.add(
            Conv2D(
                64,
                kernel_size=(3, 3),
                activation="relu"
            )
        )
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.5))  # Reducing chances of overfitting
        # Flatten results before going to Dense layer
        self.model.add(Flatten())
        # 3 hidden layers
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
        print(f"Model {self.__name} saved!")

    def load(self):
        self.model = keras.models.load_model(f"models/{self.__name}.h5")
        print(f"Model {self.__name} loaded!")
        return self.model

    def train(self, epochs: int, batchSize: int, trainImages, trainLabels, testImages, testLabels):
        startTime = time()
        print(f"Training for {self.__name} started at {ctime()}\n")
        try:
            self.model.fit(
                trainImages,
                trainLabels,
                epochs=epochs,
                batch_size=batchSize,
                validation_data=(testImages, testLabels),
                callbacks=self.__callbacks,
            )
        except tf.errors.ResourceExhaustedError:
            print(
                f"Batch size of {batchSize} is too large! Try using a smaller amount."
            )
        else:
            print(f"Training finished at {ctime()}")
            print(f"Training took {time() - startTime} seconds to run.\n")

    @property
    def info(self):
        print(f"Summary for model: {self.__name}")
        return self.model.summary()

    def evaluate(self, testImages, testLabels, batchSize):
        print(f"Evaluating {self.__name}!")
        return self.model.evaluate(testImages, testLabels, batch_size=batchSize)

    def predict(self, image):
        predictions = []
        prediction = self.model.predict(image)
        try:
            if prediction.shape[0] > 1:
                for i in range(len(prediction)):
                    predictions.append(self.labelsReal[np.argmax(prediction[i])])
                return predictions
            else:
                return self.labelsReal[np.argmax(prediction[0])]
        except:
            print(f"{self.__name} ERROR IN PROCESSING CHARACTERS! TRY AGAIN!")
            return "ERROR IN PROCESSING CHARACTERS! TRY AGAIN!"


# # * Testing Area (uncomment to test models) (uncomment import data from Pickle first)
# import matplotlib.pyplot as plt
# CrudeV6 = Model("CrudeV6")
# CrudeV6.load()

# CrudeV7 = Model("CrudeV7")
# CrudeV7.load()

# CrudeV8 = Model("CrudeV8")
# CrudeV8.load()

# CrudeV6.evaluate(imagesTest, labelsTest, 256)
# CrudeV7.evaluate(imagesTest, labelsTest, 256)
# CrudeV8.evaluate(imagesTest, labelsTest, 256)

# test = imagesTest[10096:10098]
# print(test.shape)

# plt.imshow(test[0], cmap="gray")
# plt.show()
# plt.imshow(test[1], cmap="gray")
# plt.show()

# print(CrudeV6.predict(test))
# print(CrudeV7.predict(test))
# print(CrudeV8.predict(test))

# # * To create your own model (uncomment import data from Pickle first)
# CrudeCommunity = Model("CrudeCommunity")
# CrudeCommunity.createNetwork()
# CrudeCommunity.train(
#     epochs=3, 
#     batchSize=128, 
#     trainImages=imagesTrain, 
#     trainLabels=labelsTrain, 
#     testImages=imagesTest, 
#     testLabels=labelsTest)
# CrudeCommunity.save()
# CrudeCommunity.info
# CrudeCommunity.evaluate(imagesTest, labelsTest, 256)
