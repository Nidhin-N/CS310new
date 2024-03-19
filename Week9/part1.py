import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense, Dropout
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


data_path = "./"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

# Dataset preparation
train_input = np.array([np.array(d[1:]) for d in train_data])
# Separating the labels from the image
train_label = np.array([int(d[0]) for d in train_data])

test_input = np.array([np.array(d[1:]) for d in test_data])
# Separating the labels from the image
test_label = np.array([int(d[0]) for d in test_data])

def modelling(train_input, train_label, test_input, test_label):
    # All model work should be submitted in this function
    # THis includes creation, training, evaluation etc.

    # determine the number of input features
    n_features = train_input.shape[1]

    # Create model
    model = Sequential()

    model.add(Dense(64, activation='softmax', input_shape=(n_features,)))
    model.add(Dense(10, activation='softmax'))

    model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.summary()

    model.fit(train_input, train_label, epochs=10, batch_size=32, verbose=1)

    loss, acc = model.evaluate(test_input, test_label, verbose=1)
    print('Test Accuracy: %.3f' % acc)

    # Return model at end
    return model


def visualisation(test_input, test_label, model):

    labelchoice = 0

    predictData = np.array(test_input[labelchoice])[None, ...]
    predictLabel = test_label[labelchoice]

    # make prediction
    yhat = model.predict(predictData)

    print("actual: ", predictLabel)

    # Display prediction
    print('Predicted: %s (class=%d)' % (yhat, np.argmax(yhat)))
    fig = plt.figure()
    plt.plot(yhat[0])
    plt.show()


model = modelling(train_input, train_label, test_input, test_label)
visualisation(test_input, test_label, model)