import numpy as np
from collections import Counter


diagram_points = []

with open('5_input.txt') as reader:

    for line in reader:
        start_point = line.split()[0].split(',')
        start_point = int(start_point[0]), int(start_point[1])

        end_point = line.split()[2].split(',')
        end_point = int(end_point[0]), int(end_point[1])

        magnitude_y = (end_point[1] - start_point[1])
        magnitude_x = (end_point[0] - start_point[0])

        # vertical_condition = (end_point[0] - start_point[0] == 0)
        # horizontal_condition = (end_point[1] - start_point[1] == 0)
        # diagonal_condition = ((abs(end_point[0] - start_point[0])) == (abs(end_point[1] - start_point[1])))

        if magnitude_y == 0 or magnitude_x == 0 or abs(magnitude_y) == abs(magnitude_x):

            # x_coord for vertical line
            if magnitude_x == 0:
                x = [start_point[0] for _ in range(abs(magnitude_y) + 1)]

            # x_coord for diagonal/horizontal line
            else:
                direction_x = int(magnitude_x / abs(magnitude_x))
                x = range(start_point[0], end_point[0] + direction_x, direction_x)

            # y_coord for horizontal line
            if magnitude_y == 0:
                y = [start_point[1] for _ in range(abs(magnitude_x) + 1)]

            # y_coord for diagonal/vertical line
            else:
                direction_y = int(magnitude_y / abs(magnitude_y))
                y = range(start_point[1], end_point[1] + direction_y, direction_y)

            diagram_points.extend([(x_coord, y_coord) for (x_coord, y_coord) in zip(x, y)])

# count all points marked in diagram
counter = dict(Counter(diagram_points))

# points where at least two lines overlap
solution = len({k: v for k, v in counter.items() if v >= 2})
print('Solution: ', solution)


