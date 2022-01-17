from collections import Counter

with open('14_input.txt') as file:
    initial_polymer = file.readline().split()[0]
    next(file)

    template = {}
    for line in file:
        key, value = line.replace('\n', '').split(' -> ')
        template[key] = value

# step 0
polymers = Counter()

for i in range(1, len(initial_polymer)):
    polymers[initial_polymer[i - 1:i + 1]] += 1


def make_polymer(polymer_key):
    new_1 = polymer_key[0] + template[polymer_key]
    new_2 = template[polymer_key] + polymer_key[1]
    return new_1, new_2


step = 1

while step <= 40:

    polymers_next_step = Counter()
    for key, items in polymers.items():

        for new_polymer in make_polymer(key):
            polymers_next_step[new_polymer] += items

    polymers = polymers_next_step.copy()
    step += 1

count = Counter()

for key, item in polymers_next_step.items():
    count[key[0]] += item
    count[key[1]] += item

count[initial_polymer[0]] += 1
count[initial_polymer[-1]] += 1

print('Solution:', int(count.most_common()[0][1] / 2 - count.most_common()[-1][1] / 2))
