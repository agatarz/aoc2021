from collections import Counter

# 1 -> len=2
# 4 -> len=4
# 7 -> len=3
# 8 -> len=7

with open('8_input.txt') as reader:
    counter = 0

    for line in reader:
        line = line.split('| ')[1].split()
        line = [1 for number in line if len(number) in [2, 4, 3, 7]]
        counter += sum(line)

print('Solution:', counter)