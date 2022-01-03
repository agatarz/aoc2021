txt_file = '2_input.txt'

# position = [horizontal, depth, aim]
position = [0, 0, 0]

with open(txt_file) as file:

    for line in file:
        direction, value = line.split()

        if direction == 'forward':
            position[0] += int(value)
            position[1] += position[2] * int(value)
        elif direction == 'down':
            position[2] += int(value)
        else:
            position[2] -= int(value)

print('horizontal:', position[0])
print('depth:', position[1])

# solution
print('multiplying:', position[0] * position[1])

