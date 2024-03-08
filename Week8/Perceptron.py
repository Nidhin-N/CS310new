import numpy as np


class Perceptron(object):

    #==========================================#
    # The init method is called when an object #
    # is created. It can be used to initialize #
    # the attributes of the class.             #
    #==========================================#
    def __init__(self, no_inputs, max_iterations=5, learning_rate=0.1):
        self.no_inputs = no_inputs
        self.weights = np.ones(no_inputs) / no_inputs
        self.max_iterations = max_iterations
        self.learning_rate = learning_rate

    #=======================================#
    # Prints the details of the perceptron. #
    #=======================================#
    def print_details(self):
        print("No. inputs:\t" + str(self.no_inputs))
        print("Max iterations:\t" + str(self.max_iterations))
        print("Learning rate:\t" + str(self.learning_rate))

    #=========================================#
    # Performs feed-forward prediction on one #
    # set of inputs.                          #
    #=========================================#
    def predict(self, inputs):
        assert len(inputs) == len(self.weights)
        a = np.dot(inputs, self.weights)
        if a > 0:
            return 1
        else:
            return 0

    #======================================#
    # Trains the perceptron using labelled #
    # training data.                       #
    #======================================#
    def train(self, training_data, labels):
        assert len(training_data) == len(labels)
        for _ in range(self.max_iterations):
            totalError = 0
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights = self.weights + self.learning_rate * error * inputs
                totalError += abs(error)
                print(self.weights)
            if totalError == 0:
                break

    #=========================================#
    # Tests the prediction on each element of #
    # the testing data.
    #=========================================#
    def test(self, testing_data, labels):
        assert len(testing_data) == len(labels)
        total = len(labels)
        valid = 0
        accuracy = 0.0
        for inputs, label in zip(testing_data, labels):
            prediction = self.predict(inputs)
            print("actual\t" +str(label)+"\t est\t" +str(prediction))
            if prediction == label:
                valid += 1
        accuracy = (valid / total)*100
        print("Accuracy:\t"+str(accuracy))


