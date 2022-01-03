import numpy as np

txt_file = '3_input.txt'

# power consumption = gamma rate * epsilon rate

with open(txt_file) as file:

    counter = file.readline().split()[0]
    counter = [int(bit) for bit in counter]

    for number, line in enumerate(file):
        value = line.split()[0]

        counter = [int(x) + y for (x, y) in zip(value, counter)]

    gamma_rate = ['1' if value > (number + 2 - value) else '0' for value in counter]
    epsilon_rate = ['0' if value == '1' else '1' for value in gamma_rate]

    gamma_rate = int(''.join(gamma_rate), 2)
    epsilon_rate = int(''.join(epsilon_rate), 2)
    power_consumption = gamma_rate * epsilon_rate

print('gamma_rate:', gamma_rate)
print('epsilon_rate:', epsilon_rate)

# SOLUTION
print('power_consumption:', power_consumption)