import numpy as np

with open('7_input.txt') as reader:
    data = [int(number) for number in reader.readline().split(',')]


data = np.asarray(data)

# move all crabs to 0 position
minimum_sum = sum(map(lambda x: sum(range(x+1)), data))
minimum_position = 0

for position in range(1, max(data)):

    iter_sum = sum(map(lambda x: sum(range(x+1)), abs(data - position)))

    if iter_sum < minimum_sum:
        minimum_sum, minimum_position = iter_sum, position

print('SOLUTION')
print('position:', minimum_position)
print('fuel:', minimum_sum)