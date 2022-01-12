def decode_digit(number_digit):
    number_digit = set(number_digit)

    if len(number_digit) == 2:  # 1
        ans[1] = number_digit

    if len(number_digit) == 4:  # 4
        ans[4] = number_digit

    if len(number_digit) == 3:  # 7
        ans[7] = number_digit

    if len(number_digit) == 7:  # 8
        ans[8] = number_digit


def decode_number(number_digit):
    number_digit = set(number_digit)

    if len(number_digit) == 6:
        if ans[4].issubset(number_digit):
            return 9
        else:
            if ans[1].issubset(number_digit):
                return 0
            else:
                return 6
    elif len(number_digit) == 5:
        if ans[1].issubset(number_digit):
            return 3
        else:
            if len(number_digit.intersection(ans[4])) == 2:
                return 2
            else:
                return 5
    elif len(number_digit) == 2:  # 1
        return 1

    elif len(number_digit) == 4:  # 4
        return 4

    elif len(number_digit) == 3:  # 7
        return 7

    else:
        return 8


with open('8_input.txt') as reader:
    sum_of_numbers = 0

    for line in reader:
        ans = ['' for _ in range(10)]

        line_input = line.split(' | ')[0].split()
        line_output = line.split(' | ')[1].split()

        for digit_number in line_input:
            decode_digit(digit_number)

        decoded_number = ''

        for digit_number in line_output:
            decoded_number += str(decode_number(digit_number))

        sum_of_numbers += int(decoded_number)

print('Solution:', sum_of_numbers)
