import numpy as np


def check_winner(bingo_boards):
    for player in range(len(bingo_boards)):
        suma_row = np.sum(bingo_boards[player], axis=0)
        suma_column = np.sum(bingo_boards[player], axis=1)

        if -5 in suma_column or -5 in suma_row:
            return player
    return 0


with open('4_input.txt') as file:

    print_steps = True

    # read data
    bingo_numbers = [int(number) for number in file.readline().split(',')]

    if print_steps:
        print('>>Bingo numbers: \n', bingo_numbers)

    single_table = np.empty((0, 5), int)
    bingo_tables = []

    for line in file:
        line = line.split()

        if not line:
            single_table = np.empty((0, 5), int)
        else:
            line = np.array([[int(number) for number in line]])
            single_table = np.append(single_table, line, axis=0)
            if single_table.shape[0] == 5:
                bingo_tables.append(single_table)

    bingo_tables = np.array(bingo_tables, dtype=int)

    if print_steps:
        print('>> Iteration: 0')
        print(bingo_tables)

    for iteration in range(0, len(bingo_numbers)):

        bingo_tables[bingo_tables[:, :, :] == bingo_numbers[iteration]] = -1

        if print_steps:
            print('>> Iteration: ', iteration + 1)
            print('>> Random number: ', bingo_numbers[iteration])
            # print(bingo_tables)

        winner = check_winner(bingo_tables)

        if winner:
            print('>> Winner is: ', winner + 1)
            solution = sum(bingo_tables[winner][bingo_tables[winner] >= 0]) * bingo_numbers[iteration]
            print('>> Solution: ', solution)
            break
