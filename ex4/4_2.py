import numpy as np


def check_winner(bingo_boards):

    # 1 - bingo, 0 - no bingo
    player_score = [0 for _ in range(len(bingo_boards))]

    for player in range(len(bingo_boards)):
        suma_row = np.sum(bingo_boards[player], axis=0)
        suma_column = np.sum(bingo_boards[player], axis=1)

        if -5 in suma_column or -5 in suma_row:
            player_score[player] = 1
    return player_score


with open('4_input.txt') as file:

    # read data
    bingo_numbers = [int(number) for number in file.readline().split(',')]

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

    looser_index = None

    for iteration in range(0, len(bingo_numbers)):

        print('>> Iteration: ', iteration + 1)
        print('>> Random number: ', bingo_numbers[iteration])

        bingo_tables[bingo_tables[:, :, :] == bingo_numbers[iteration]] = -1

        players_score = check_winner(bingo_tables)

        if not sum(players_score) == len(players_score):
            # find first player in table who has no bingo
            looser_index = players_score.index(0)
        else:
            solution = sum(bingo_tables[looser_index][bingo_tables[looser_index] >= 0]) * bingo_numbers[iteration]

            print('>> Loser is player:', looser_index + 1)
            print('>> Solution: ', solution)

            break
