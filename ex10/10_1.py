keys = {'(': ')', '[': ']', '{': '}', '<': '>'}
counter = {'}': 0, ')': 0, '>': 0, ']': 0}

with open('10_input.txt') as reader:
    bad_lines = []
    for line in reader:
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
                    counter[char] += 1
                    break

solution = counter['}'] * 1197 + counter[')'] * 3 + counter[']'] * 57 + counter['>'] * 25137
print('Solution:', solution)
