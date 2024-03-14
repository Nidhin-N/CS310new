import numpy as np
from PerceptronPt3 import Perceptron
import matplotlib.pyplot as plt

p = Perceptron(785)

data_path = "./"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

target_digit = 7
train_input = [ np.append([1],d[1:]) for d in train_data ]
train_label = [ int(d[0]==target_digit) for d in train_data ]

test_input = [ np.append([1],d[1:]) for d in test_data ]
test_label = [int(d[0]==target_digit) for d in test_data ]

fig = plt.figure(figsize=(4,4))
data = p.weights[1:].reshape(28,28)
vis = train_input[15][1:].reshape(28,28)
plt.imshow(vis)
plt.show()

p.print_details()
p.test(test_input, test_label)

p.train_batch(train_input, train_label)

p.test(test_input, test_label)