import numpy as np
import matplotlib.pyplot as plt

days_number = 256

initial_state = [0] * 9
with open('6_input.txt') as reader:
    data = reader.readlines()[0].split(',')
    for number in data:
        initial_state[int(number)] += 1


# print('Initial state:')
# print(0, initial_state, sum(initial_state))

first = initial_state[0]

for day in range(1, days_number + 1):

    initial_state = initial_state[1:9] + [first]

    if first != 0:
        initial_state[6] += first

    if day == days_number:
        print('SOLUTION: Day: %i, Fishes: %i' %(day, sum(initial_state)))

    first = initial_state[0]



