txt_file = '1_input.txt'

count_increased = 0
with open(txt_file) as file:

    first = int(file.readline())
    second = int(file.readline())
    third = int(file.readline())

    prev_sum = sum([first, second, third])
    print(prev_sum, '(N/A - no previous sum')

    for measure in file:
        measure = int(measure.split()[0])

        first, second, third = second, third, measure
        curr_sum = sum([first, second, third])

        if curr_sum > prev_sum:
            print(curr_sum, '(increased)')
            count_increased += 1
        elif curr_sum == prev_sum:
            print(curr_sum, '(no change)')
        else:
            print(curr_sum, '(decreased)')

        prev_sum = curr_sum

print('sums are larger than the previous sum:', count_increased)

