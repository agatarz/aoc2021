import numpy as np
import matplotlib.pyplot as plt
#initial = np.array([3, 4, 3, 1, 2])
initial =[0, 0, 0, 0, 0, 0, 0, 0, 0]
with open('6_test.txt') as reader:
    data = reader.readlines()[0].split(',')
    for number in data:
        initial[int(number)] += 1


print('Initial state:')
print(initial, sum(initial))

