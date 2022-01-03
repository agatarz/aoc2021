# https://adventofcode.com/2021/day/1

txt_file = '1_input.txt'
count_increased = 0

with open(txt_file) as file:

    # read first line
    prev_measure = int(file.readline())
    print(prev_measure, '(N/A - no previous measurement)')

    for measure in file:
        measure = int(measure.split()[0])

        if prev_measure < measure:
            count_increased += 1
            print(measure, '(increased)')
        else:
            print(measure, '(decreased)')

        prev_measure = measure

print('larger than the previous measurement: ', count_increased)
