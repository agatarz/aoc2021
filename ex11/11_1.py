import numpy as np
import itertools


def cells_adjacent(arr, row_array, col_array):
    """ Return cells adjacent to current cell """

    row_adjacent = [row_array - 1, row_array + 1]
    col_adjacent = [col_array - 1, col_array + 1]

    if row_array == 0:
        row_adjacent[0] = row_array
    elif row_array == arr.shape[0] - 1:
        row_adjacent[1] = row_array
    if col_array == 0:
        col_adjacent[0] = col_array
    elif col_array == arr.shape[1] - 1:
        col_adjacent[1] = col_array

    row_adjacent = list(range(row_adjacent[0], row_adjacent[1] + 1))
    col_adjacent = list(range(col_adjacent[0], col_adjacent[1] + 1))

    cell_adjacent = [(x, y) for x, y in itertools.product(row_adjacent, col_adjacent) if
                     (x, y) != (row_array, col_array)]

    return cell_adjacent


with open('11_input.txt') as reader:
    current_data = []

    for line in reader:
        line = line.split()[0]
        line = [int(number) for number in line]
        current_data.append(line)

current_data = np.asarray(current_data)

counter_lights = 0

print(' ---- STEP: {} ---- '.format({0}))
print(current_data)
counter = 0

for i in range(1, 101):

    # the energy level of each octopus increases by 1
    current_data = current_data + 1

    next_data = np.array(current_data, copy=True)

    while np.any([9 < current_data]) and np.any([20 > current_data]):
        for row in range(current_data.shape[0]):
            for col in range(current_data.shape[1]):

                # any octopus greater than 9 increases all adjacent octopuses by 1
                if 9 < current_data[row, col] < 20:
                    adjacent = cells_adjacent(current_data, row, col)

                    for cell in adjacent:
                        next_data[cell[0], cell[1]] += 1

                    # octopus flashes -> at most once per step
                    next_data[row, col] = 20

        current_data = np.copy(next_data)

        # octopus that flashed during this step has its energy level set to 0
        current_data[current_data >= 20] = 0

    if i == 100:
        print(' ---- STEP: {} ---- '.format({i}))
        print(current_data)
        print(len(current_data[current_data == 0]))
    counter += len(current_data[current_data == 0])

print('solution: ', counter)
