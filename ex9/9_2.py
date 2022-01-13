def check_cell(row, column):
    """ Check if cell is not 9 or X, and add its surrounding cells to check in next move"""

    # look for the basin moving up/down/right/left
    direct_cells_to_check = [(row, column - 1), (row, column + 1), (row - 1, column), (row + 1, column)]

    # cells, which surrounding are checked in next move
    cells_surroundings_to_check = []

    for (x, y) in direct_cells_to_check:
        if data[x][y] != 9:
            if (x, y) not in new_cells_basin:
                new_cells_basin.append((x, y))
                cells_surroundings_to_check.append((x, y))
            data[row][column] = 'X'
    return cells_surroundings_to_check


def check_cell_surrounding(cells_to_check):
    """ check cells surroundings until the list is empty"""
    if not cells_to_check:
        return True
    else:
        for item in cells_to_check:
            next_cells_to_check = check_cell(item[0], item[1])
            check_cell_surrounding(next_cells_to_check)


with open('9_input.txt') as reader:
    basins = []

    # read data and add 9 to the beginning and to the end of each column and row
    data = [line.split()[0] for line in reader.readlines()]
    data = ['9' * len(data[0])] + data + ['9' * len(data[0])]
    data = [[9] + [int(number) for number in line] + [9] for line in data]

    # go through orginal cells (without frame made of 9)
    for row in range(1, len(data) - 1):
        for column in range(1, len(data[row]) - 1):

            if data[row][column] not in (9, 'X'):
                new_cells_basin = [(row, column)]
                current_basin_points = check_cell_surrounding(new_cells_basin)
                basins.append(len(new_cells_basin))

ans = sorted(basins, reverse=True)[:3]
print(ans[0] * ans[1] * ans[2])