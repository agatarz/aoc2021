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

        break

# max dimension of dots coordinates
max_x = max([x for x, _ in dots]) + 1
max_y = max([y for _, y in dots]) + 1

for fold_along_y in fold_along_y_table:
    new_dots = []
    for dot in dots:
        if dot[1] > fold_along_y:
            dot_y_folded = (dot[0], 2 * fold_along_y - dot[1])
            new_dots.append(dot_y_folded)
        else:
            new_dots.append(dot)
    dots = new_dots[:]

for fold_along_x in fold_along_x_table:
    new_dots = []
    for dot in dots:
        if dot[0] >= fold_along_x:
            dot_x_folded = (2 * fold_along_x - dot[0], dot[1])
            new_dots.append(dot_x_folded)
        else:
            new_dots.append(dot)
    dots = new_dots[:]

print('Solution:', len(set(dots)))
