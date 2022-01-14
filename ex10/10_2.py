keys = {'(': ')', '[': ']', '{': '}', '<': '>'}
counter = {'}': 0, ')': 0, '>': 0, ']': 0}
points = {')': 1, ']': 2, '}': 3, '>': 4}


def fill_line(bad_line):
    return ''.join([keys[line_char] for line_char in (bad_line[::-1])])


def point_line(bad_line):
    score_line = 0
    for line_char in bad_line:
        score_line = score_line * 5 + points[line_char]
    return score_line


sum_scores = []

with open('10_input.txt') as reader:

    bad_lines = []
    for nr, line in enumerate(reader):
        line = line.split()[0]
        line2 = []
        popped = []

        for char in line:
            if char in '[{(<':
                line2.append(char)
            else:
                if keys[line2[-1]] == char:
                    line2 = line2[:-1]
                else:
                    line2 = []
                    break
        if line2:
            sum_scores.append(point_line(fill_line(line2)))

solution = sorted(sum_scores)[len(sum_scores) // 2]
print('Solution:', solution)
