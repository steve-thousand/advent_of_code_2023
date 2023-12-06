import re

def solve(puzzle_input):
    records = [[int(x) for x in re.split(r'\s+', line.split(":")[1].strip())] for line in puzzle_input.strip().split("\n")]
    part_1 = 0
    for i in range(0, len(records[0])):
        length = records[0][i]
        record = records[1][i]
        total_possible = 0
        for m in range(0, length + 1):
            distance = (length - m) * m
            total_possible += 1 if distance > record else 0
        part_1 = part_1 * total_possible if part_1 != 0 else total_possible
    print(part_1)

    length = int(''.join([str(x) for x in records[0]]))
    record = int(''.join([str(x) for x in records[1]]))
    part_2 = 0
    for m in range(0, length + 1):
        distance = (length - m) * m
        part_2 += 1 if distance > record else 0
    print(part_2)

    return

solve('''
Time:        40     82     91     66
Distance:   277   1338   1349   1063
''')