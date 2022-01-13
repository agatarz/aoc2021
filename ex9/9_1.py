with open('9_input.txt') as reader:
    sum_numbers = 0

    # read data and add 9 to the beginning and to the end of each column and row
    data = [line.split()[0] for line in reader.readlines()]
    data = ['9' * len(data[0])] + data + ['9' * len(data[0])]
    data = [[9] + [int(number) for number in line] + [9] for line in data]

    # go through orginal cells (without frame made of 9)
    for row in range(1, len(data) - 1):
        for column in range(1, len(data[row]) - 1):

            # for each cell cerate table with neighbours sorounded it (another 8 cells)
            neighbors = data[row - 1][column - 1:column + 2]
            neighbors += [data[row][column - 1]] + [data[row][column + 1]]
            neighbors += data[row + 1][column - 1:column + 2]

            # how many surrounding cells are greater than cell
            neighbors = [(neighbour - data[row][column]) > 0 for neighbour in neighbors]

            # if all surrounding cells are grater tha cell -> add cell to summary
            if all(neighbors):
                sum_numbers += data[row][column] + 1

print('Solution:', sum_numbers)

