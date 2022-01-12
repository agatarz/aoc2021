# https://adventofcode.com/2021/day/5

import numpy as np
from collections import Counter

# get data from the file

line_points = []
with open('5_input.txt') as reader:
    for line in reader:
        start_point = line.split()[0].split(',')
        end_point = line.split()[2].split(',')

        line_points.append([int(start_point[0]), int(start_point[1]),
                            int(end_point[0]), int(end_point[1])])


# [start_x, start_y, end_x, end_y]
line_points = np.asarray(line_points)

# start_x == end_x
vertical_lines = line_points[(line_points[:, 0] == line_points[:, 2])]

# start_y == end_y
horizontal_lines = line_points[(line_points[:, 1] == line_points[:, 3])]

# list with points marked in diagram
diagram_points = []

for line in range(vertical_lines.shape[0]):

    x = vertical_lines[line][0]
    assert vertical_lines[line][0] == vertical_lines[line][2]
    
    if vertical_lines[line][1] < vertical_lines[line][3]:
        y = range(vertical_lines[line][1], vertical_lines[line][3] + 1)
    else:
        y = range(vertical_lines[line][3], vertical_lines[line][1] + 1)

    # add points from vertical lines
    diagram_points.extend([(x, _y) for _y in y])

for line in range(horizontal_lines.shape[0]):
    y = horizontal_lines[line][1]
    assert horizontal_lines[line][1] == horizontal_lines[line][3]

    if horizontal_lines[line][0] < horizontal_lines[line][2]:
        x = range(horizontal_lines[line][0], horizontal_lines[line][2] + 1)
    else:
        x = range(horizontal_lines[line][2], horizontal_lines[line][0] + 1)

    # add points from horizontal lines
    diagram_points.extend([(_x, y) for _x in x])

# count all points marked in diagram
counter = dict(Counter(diagram_points))

# points where at least two lines overlap
solution = len({k: v for k, v in counter.items() if v >= 2})
print('Solution: ', solution)
