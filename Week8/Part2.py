import numpy as np
import matplotlib.pyplot as plt
from Perceptron import Perceptron

p = Perceptron(785)

data_path = "./"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

target_digit = 5
# Replacing first letter with a bias value
train_input = [ np.append([1],d[1:]) for d in train_data ]
# Separating the labels from the image
train_label = [ int(d[0]==target_digit) for d in train_data ]

test_input = [ np.append([1],d[1:]) for d in test_data ]
test_label = [int(d[0]==target_digit) for d in test_data ]

fig = plt.figure(figsize=(4,4))
data = p.weights[1:].reshape(28,28)
vis = train_input[0][1:].reshape(28,28)
plt.imshow(vis)
plt.show()

p.print_details()
p.test(test_input, test_label)

p.train(train_input, train_label)

p.test(test_input, test_label)


