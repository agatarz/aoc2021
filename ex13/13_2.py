def print_table(table):
    for row in table:
        print(' '.join(row))


def print_dots(max_y, max_x, dots_coord):
    dotted_table = []
    for i in range(max_y):
        dotted_table.append(['.' for _ in range(max_x)])

    for dot_coord in dots_coord:
        dotted_table[dot_coord[1]][dot_coord[0]] = 'X'

    print_table(dotted_table)


def count_dots(dots_coord):
    dot_counter = len(set(dots_coord))
    return dot_counter


dots = []
fold_along_y_table = []
fold_along_x_table = []

with open('13_input.txt') as reader:
    for line in reader:
        line = line.replace('\n', '')
        if not line:
            break
        line = line.split(',')
        line = (int(line[0]), int(line[1]))
        dots.append(line)

    for line in reader:
        fold = line.replace('\n', '').split('=')
        if fold[0] == 'fold along x':
            fold_along_x_table.append(int(fold[1]))
        if fold[0] == 'fold along y':
            fold_along_y_table.append(int(fold[1]))

# size of initial dotted table    
max_x_coord = max([x for x, _ in dots]) + 1
max_y_coord = max([y for _, y in dots]) + 1

# initial data
dots_amount = count_dots(dots)
# print('Dots:', dots_amount)

# y folding
for fold_along_y in fold_along_y_table:
    new_dots = []
    for dot in dots:
        if dot[1] > fold_along_y:
            dot_y_folded = (dot[0], 2 * fold_along_y - dot[1])
            new_dots.append(dot_y_folded)
        elif dot[1] == fold_along_y:
            continue
        else:
            new_dots.append(dot)

    dots = new_dots[:]

dots_amount = count_dots(dots)
# print('Dots:', dots_amount)

# x folding
for fold_along_x in fold_along_x_table:

    new_dots = []
    for dot in dots:
        if dot[0] > fold_along_x:
            dot_x_folded = (2 * fold_along_x - dot[0], dot[1])
            new_dots.append(dot_x_folded)
        elif dot[0] == fold_along_x:
            continue
        else:
            new_dots.append(dot)
    dots = new_dots[:]

# answer
print_dots(fold_along_y_table[-1], fold_along_x_table[-1], dots)
