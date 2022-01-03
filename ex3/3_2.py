import numpy as np


def oxygen_generator_rating(data):
    for column in range((np.shape(data))[1]):

        summed_bit = np.sum(data, axis=0)
        amount_bit = data.shape[0]
        most_common_bit = int(summed_bit[column] >= (amount_bit - summed_bit[column]))

        data = data[data[:, column] == most_common_bit, :]

        if data.shape[0] == 1:
            return int(''.join(data.astype(str)[0]), 2)


def CO2_scrubber_rating(data):
    for column in range((np.shape(data))[1]):

        summed_bit = np.sum(data[:, column], axis=0)
        amount_bit = data.shape[0]
        least_common_bit = int(summed_bit < (amount_bit - summed_bit))

        data = data[data[:, column] == least_common_bit, :]

        if data.shape[0] == 1:
            return int(''.join(data.astype(str)[0]), 2)


txt_file = '3_input.txt'

report = np.loadtxt(txt_file, dtype=str)
report = np.array([(list(character)) for row in report for character in row.split()])
report = report.astype(int)

CO2_scrubber = CO2_scrubber_rating(report)
oxygen_generator = oxygen_generator_rating(report)

life_support_rating = CO2_scrubber * oxygen_generator

print('CO2_scrubber', CO2_scrubber)
print('oxygen_generator', oxygen_generator)

# SOLUTION
print('life_support_rating', life_support_rating)
