import numpy as np
from Perceptron import Perceptron

not_input = [np.array([0]), np.array([1])]
not_label = [1, 0]

logic_input = [np.array([1, 0, 0]), np.array([1, 0, 1]), np.array([1, 1, 0]), np.array([1, 1, 1])]
#or gate
or_label = [0, 1, 1, 1]
#and gate
and_label = [0, 0, 0, 1]
#xor gate
xor_label = [0, 1, 1, 0]

p = Perceptron(3)
p.print_details()
p.test(logic_input, or_label)

# Train the Perceptron on XOR gate data
p.train(logic_input, or_label)

# Test the Perceptron after training
p.test(logic_input, or_label)