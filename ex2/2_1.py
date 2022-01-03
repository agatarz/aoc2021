# https://adventofcode.com/2021/day/2

txt_file = '2_input.txt'

position = [0, 0]

with open(txt_file) as file:

    for line in file:
        direction, value = line.split()
        # print(direction, value)

        if direction == 'forward':
            position[0] += int(value)
        elif direction == 'down':
            position[1] += int(value)
        else:
            position[1] -= int(value)

print('horizontal:', position[0])
print('depth:', position[1])

# solution
print('multiplying:', position[0] * position[1])


