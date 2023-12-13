def can_fit(space, required_length):
    possible = []
    max_i = min(space.index('#') + 1 if '#' in space else len(space), len(space) - required_length + 1)
    for i in range(0, max_i):
        if i + required_length == len(space) or space[i + required_length] != '#':
            if '.' in space[i:i+required_length]:
                continue
            remainder_space = ''.join(space[i + required_length + 1:]) if len(space) - 1 > i + required_length else ''
            taken_space = [x for x in space[:i + required_length + 1]]
            for j in range(0, len(taken_space)):
                taken_space[j] = '.' if j < i else '#' if j < i + required_length else '.'
            possible.append((''.join(taken_space), remainder_space))
    return possible

def find_possible_arrangements(space, required, cache={}):
    if len(required) == 0:
        return 0 if '#' in space else 1
    found = 0
    first_required = required[0]
    can_fit_spaces = can_fit(space, first_required)
    for can_fit_space in can_fit_spaces:
        cache_key = (can_fit_space[1], ','.join([str(x) for x in required[1:]]))
        if cache_key not in cache:
            lower_founds = find_possible_arrangements(can_fit_space[1], required[1:], cache)
            cache[cache_key] = lower_founds
        found += cache[cache_key]
    return found

def solve(puzzle_input):
    condition_records = [(line.split(" ")[0], [int(x) for x in line.split(" ")[1].split(",")]) for line in puzzle_input.strip().splitlines()]
    possible = 0
    for condition_record in condition_records:
        possible += find_possible_arrangements(condition_record[0], condition_record[1])
    print(possible)

    possible = 0
    for condition_record in condition_records:
        unfolded_0 = condition_record[0] + "?" + condition_record[0] + "?" + condition_record[0] + "?" + condition_record[0] + "?" + condition_record[0]
        unfolded_1 = condition_record[1] + condition_record[1] + condition_record[1] + condition_record[1] + condition_record[1]
        possible += find_possible_arrangements(unfolded_0, unfolded_1)
    print(possible)
    return

solve('''
???????????#??? 5,2,1
#??##.??.?# 5,1,1
.??###?..???#?.?##?. 4,4,3
??..?#??#??#?.???? 5,1,1
?????#???? 2,1,1
?#?##???#????? 1,8
??#?.?#????.? 1,4
?#####??#?????.?#.. 9,2,1
??????#???? 1,3,1
.?.?#?????#?.??.? 2,2
.????#????... 1,6
.##?#???????????? 8,5
.?.?#?#??#??#?? 1,8,1,1
???#?#?????#???? 1,1,7,1,1
???.????.?..????? 3,1,1,3
???????#???.?#?#? 2,5,4
##?#??#?.#??????? 8,2,1
.??..??????????#??.# 2,1,1,6,1
??.????#?????? 1,1,3,1
?#??##?????? 5,1,1
?????.?##? 2,1,3
??.?.????.?? 1,1,1,1
#.#?????.?.????? 1,6,1,1,1
?.????????# 2,1,2
???#?????????#??.?? 1,3,5,1,1,1
??.??#.?###???? 1,3,7
???????.?? 1,3
.??#??????#??#?.?. 1,1,1,1,6,1
???#??.?#.???#??? 1,2,1,6
??#??##??? 2,5
#?????###???##?# 5,3,5
???##?.?.#?##? 5,5
??#????#?#??#??. 1,2,6
?#?????#???#?#?#???. 1,1,12,1
?###??????..??#?. 8,3
????#..??.# 4,1,1
##..??##???????? 2,7
#..??#?#?? 1,5
??????????###.?#.#? 1,1,7,2,1
..#???.?..?? 1,1,1,1
?#?.?.??.??#?#?#? 1,1,3,4
?#??#.???????.? 4,1,5,1
.#?????#????##??...? 1,8
?????#??.???.. 5,2
?###???.?##? 3,1,3
???..???????#?? 2,2,4,1
?#???.???? 1,1,1
??#?????.#??.??? 7,1,1
?????.??#?#?# 4,3,1
???#.?##???..???#? 3,4,5
?##?.????#???.#.? 2,2,1,1,1
??#???#??#????? 7,1,1
???.??#????.#??. 1,5,1,1
...?#???.?. 2,1
?#?#??????? 4,1,1
?????.?#.?. 2,1
?#.????#?. 1,1,2
????####.?.? 1,5,1
#??..????????#???? 1,1,6,1,3
?????.????#? 2,1,5
????????##???#?.? 11,1,1
??????#.??.#????.??. 3,3,2,1,2,2
?.?#??#??#?.????? 1,2,5,1,1
?.##?#.?#??????? 1,4,5,2
?.???????### 1,2,1,4
???.?#.?#???????.? 3,1,4,1
????.?????#?#?# 2,1,2,5
?????###???.?.??#.# 1,6,1,1,1,1
??????.??..#?#?? 1,1,2,1,5
.#???#???#???#??? 9,1,1,2
???#????#.?#??#?? 6,1,2,3
.?#????##??..?? 9,1
??#??#????? 2,2,1
.??..#?..?.?? 1,2,1,1
...??????##??.?. 3,3
??#?????#??.#????? 8,1,1,1
?????#??.. 1,3
.#?????????? 3,1
????#?##???? 7,1
??.?#??????#??.? 1,3,1,5
?????#?#?????#????# 7,6
.????.?????? 1,3
???#??##??? 5,1
?#???.????#?#???.??? 2,1,7,1,1
?????##.??????#? 4,1,3
??.??????#???#?.?? 2,2,1,3,2,1
?##?.?#???????????. 2,4,4,1
?#?#??#????? 1,4,1,1
.?????.????.??? 3,1
#???#.?.??.. 1,2,2
??#.??????. 1,2,1
????????????.###. 5,1,3
.??.#???#?? 2,2,3
????????????##???#? 5,6
??#????#?.? 2,3
#.???????? 1,1,1
?#????#?##???.?.? 1,6,2,1,1
??????????#??? 4,4,1
?##??...???##?????. 4,7
#??##??????.#???.??# 5,1,1,1,3
?.?..?##?????.# 1,1,8,1
?.?.#??#?. 1,2,1
?.???.#??? 2,3
..?????????#? 1,4,1
??????????#????.? 2,6,1
.?????#????.?.????. 1,5,1,3
??????.?#?? 6,2
####???????#?.? 4,2,1,1
?#?##?????.... 1,7
.?.??#??.?#???.???? 1,1,1,1,1,4
??.#.?????#?? 2,1,2,4
???#?#?????#???## 1,3,1,7
#????.??##?????. 5,4
??#.?#???##?????# 1,7,4
.??.??.#????.???#.? 2,1,2,1,1,1
.?###???????.??##..? 7,3,1,2,1
..???#???##? 1,7
??.?.???##?#??.##.? 1,1,7,2
???.?.???.?.? 1,1,3
????#???#.#???#### 8,1,6
?...##??.????#?#??#? 4,6
#???#.#???###???? 3,1,8,1
#???##?#??.?#??. 1,5,1,1
????#?.###?????. 1,2,3,4
??#?###??.???.?#? 7,1,3,1
#?.??#?????#??.????? 2,9,2,1
?????###?##.?????.. 6,4
#?..??#??????#???? 2,4,3,2
???##?##???#????? 1,2,11
????.?.#?#??????? 2,1,3,1,1
??????#?.???? 1,2,2,1
#.???????##.??#? 1,2,3,2
?.?????#.?##..????# 1,2,1,2,1,3
#??.#?#?.? 1,4
?????????##? 3,1,3
#.?.?#??#??#.?#??? 1,1,7,1,1
.?..#?.????#???#???? 1,9
?#?#?.??????#????? 2,2,1,3,1,1
.??.???#?????#?? 1,1,5,3
?#.?#???.. 1,3
?.?..??????? 1,1,1,4
????????#?. 3,1,2
??.#???.#???????#?. 1,1,1,3,2,2
??#???##??.?? 1,1,5,1
??????.??????? 5,5
#?#??..?????.??#??#. 5,3,5
???????#.????.##. 1,3,1,1,2
.???#...#? 4,1
##???????????? 3,2,1,2
????????#??# 1,1,4
#??????????.??#.?# 7,1,1,1,1,1
#?...????.??###?? 1,3,6
??????##.????? 3,2,2
.#?..????##?.??????? 2,1,4,1,5
?????.????# 3,1,2
????##???????? 4,3
?.?????#?.? 1,4
??#.?.?.??#??#??...? 1,6
??#???#??? 4,1,1
??#????.?#.??#???.? 5,1,1,3,1
??#?#.##?#???. 2,1,7
.??#????#????#?? 2,6
???.???.???. 2,1,1,1
?#????#???? 2,1
#???.#?##?.?##..?? 1,1,1,2,2,1
#?.#.?#.???.??. 1,1,2,1,1
??.???#???????? 1,9
.?.??.???#??#?? 1,1,8
???????????? 3,5,1
#####????#?.??. 11,1
.?#???.?#. 2,1,1
????.???????#??????? 5,1
???#..?#???? 1,1,1,2
????##??????#??#???# 2,12,1
?#.???#?#??#??#. 1,7,1,2
#?#?#?.???? 5,3
?#...?????? 1,1
??#?.#??##? 3,1,2
.#???#??.?.?????? 7,4
?#???.???#.?????.??# 4,1,1,1,1,2
???.?????###??#?? 2,1,9
#???????#?###. 2,8
???#?#????#?#??#. 6,2,1,1
??#?.????#?????.? 1,1,1,7,1
#???#???#????###?#?. 3,1,6,5
#.???#????#??.##???# 1,2,6,3,1
???????#.?#? 8,1
????.?#?#.??????. 2,4,5
??.?#?#??????#?#??? 4,5
.?#??###?#?.????? 9,1
#?#??.#?????#??##??? 1,3,1,1,1,4
.??.???##??#? 1,4,1
???#.?##??#? 1,6
?????##?.?..#?#???? 1,1,2,1,1,4
??.#????.# 1,1,1
????????#. 2,1,1
.??.???#??#? 2,1,1,2
#..???#??#???? 1,1,7
?.??.?#.#? 1,1,1
??#.????..?????###?? 3,4,1,2,4
?.??.?#?.??#???.. 2,4
??##??????..#???? 5,1,4
??????..#???#??#??? 1,3,1,7
.??.???##??.#. 2,3,1
.#???.#??#???#?#??# 1,2,5,2,1,1
??#?#.?#?? 4,1
???##?..?#?????..? 4,6
??.??.??????? 1,1,1,3
.?????????.???. 6,1,1,1
.??#?#?.???#. 4,1,1
????#??.?.??????? 5,4
..#.#????.???? 1,4,2
.?##.?#.??. 2,2
???.#?#?###????.??#? 1,8,2,3
????...??#?#???? 1,6
?????##?#???? 1,6,1
??.??#??#??#?#?????? 1,3,1,8,1
????#????#????? 8,1
????#?#?#.?? 1,6,1
.?#????##?????????? 2,1,10
?#.????#..?? 1,2,2
.????.???#?#??? 2,5
????#..#?? 2,2,1
???#???.?##???#? 4,8
???????..??.?? 4,1,2,1
??.?#?????? 2,1
.???.????#??.?? 3,4
.#.???.??? 1,2
??#???????????.#.??? 1,1,5,1,1,2
##???##..?????#????? 2,3,2,1
?#.?????#??? 1,2,4
#?#????..??? 1,5,2
.??#?.???#??????? 4,1,6
.?#????.?#.?.? 4,1,1,1
.???.??????? 1,2,4
..????#?????#???. 2,4,5
#?#?#?.?.???#? 5,1,1,1
??????##?##????? 1,1,6,1
?##???????????.?. 4,1,1,1,1
???#?..?.??? 1,1,1,2
??#?????#???.?#? 4,6,3
????????????.#? 5,1,1,1
?.??.??#?..?.#?.?? 1,2
#..#???????#??? 1,7,1
???????.?.????# 5,1,1,1,1
??.??.??#?. 2,1,3
.???.??#?##??.#.?# 3,6,1,1,2
.???..???? 1,2
..???##??#??.??..?.. 8,2
?#.#?.#?##??. 1,2,1,2
???.????..? 2,2
?###.?...?.????? 3,1,1,1,2
?????#.??????.??#? 1,3,1,1,1,1
##?#??.#?#.??. 5,3,1
.?.#?#??????##? 1,3,1,2
?####?.????. 5,1,1
???##.??..?#???#???? 5,2,9
?#??.?##???#????? 2,12
#?#????#??..##?? 3,1,3,2
???#???##?#?.???? 1,1,4,3
???.??.?##???.??? 1,5
???#?..#?#???#.???? 4,7,4
????#???????????#? 12,1,2
.#?#.??#.?## 1,1,3,2
.?????#???????#? 3,1,7
#??#?????#?????? 13,1
?##??.?#.????.#?? 5,1,2,1,1
.??#??.???#????. 3,5
?#?#??#.#??.??. 3,2,1,1,1
#??????..???#??? 1,2,2,3,1
.?.???...??? 2,1
.????#?.#?#???#???## 2,12
.??#???#?#.??#?#???? 1,1,5,1,6
?????#.?????#???? 5,6
????.??.?? 2,1
.??#?????#??????? 1,1,1,5,2
???#.?#..? 3,1
??#????#?#?##?##?.? 5,10
?????.??#?##.??? 5,6,1
?#???.???? 3,1
??.#??##?##???????# 1,14
#.???????#???.?.#. 1,1,2,2,1,1
#?#???#????#??#?#?? 8,3,2,1
#.??#??#????????? 1,7,2,3
?.#.???#???#?# 1,9
####????????.# 6,4,1
?#?#?#??.? 6,1
#??.?#?????#?#??? 3,5,1,2,1
?#??????#???.? 10,1
.??.##.???#?????. 2,8
.???#????.?.#??? 2,2
???.?#?#???#????? 2,8,3
??.?..?#?..??##?.??? 1,4
????#????#??? 1,7
.????#????#???#?#? 2,2,2,2,1,1
????#?#?#.?.??????? 1,5,1,1,1,1
?#??#??..##???#??# 1,2,1,2,1,4
?.???##?#????##??. 1,4,1,4
???#???#?###?..?#... 11,2
#?#.?.?.#?..? 1,1,1,1
###?.?.?.???#???#.? 3,8
#.???#?????#?? 1,10
.?#?????.?#.??? 6,1,2
?.#?.????.? 2,4,1
#?.??#???#? 2,1,3
?.#.??????.??#??# 1,1,1,3,6
?##??????##.?????### 3,7,1,1,3
??##?#?#???.?###???? 8,6
?#?.???.??#???# 2,1,6
????#??.???# 2,1
#??.???.??? 1,2,1
.???##???? 1,7
#???.#??.#.? 2,1,1,1
??????????# 3,1,2
#?#?.??.??.?? 3,1,1,2
???#??.##???..?#?? 4,4,3
??#???.???#? 1,1,3
???#??????# 3,4
?#..??????? 2,2,3
?#?#.??..?????. 4,1,1,2
???????###??? 1,1,4
.????#.??????.?????? 5,2,3,2,1
???#???#.? 3,3,1
?..??#?##? 1,1,5
?.??..?????. 1,2,2,1
???.??..##?#? 1,1,2,1
????????#??. 2,1,2
????###???????#?? 7,4
????#????#?#??.#??? 1,5,4,1,1
??#?.???#?#?##? 4,1,7
???.??#??#????###? 1,1,5,3
????.???????. 2,5
.#??????#??#..??? 3,1,4,2
?.??#?????#? 1,4,3
????.#???#??? 1,1,1,5
?.#??????????? 1,3,1,1
????..???#?.??#????? 1,2,5,3,2,1
??###????#???.??.?#? 13,1,1
?????.?.?? 5,1
#??#??##????.# 1,1,7,1
?##????????#?.?? 8,2,2
?#??#???#?????..?? 5,6
..??..?.??? 1,2
???.??????.??##??. 3,1,1,5
.???#??.?.?????##??. 1,2,1,1,6
??#?#.??????#??. 5,1,5
???#???##???.#?? 11,1
#?#????????.????.?? 11,1,1,2
??#?.???#?????????? 4,11
.??.?????. 1,5
##??##?#.??.? 8,2
???#??##?#?###??## 12,2
?##???.????##?#?? 3,1,7
??#????#?#?.# 4,2,1,1
?#??????#???????? 12,1
?..??#????#??????##. 1,10,5
??.??????#??.. 1,4
?????.#??? 3,2
???#???##???? 1,8,1
??.?????.??????????? 3,1
?#??#?##?###?????## 11,2
?.???????????? 6,2
???.?.???#???#.?? 1,7,2
???#??#???#?????? 3,2,2,2
..?#####????# 9,1
?#??????.?? 1,2,1
#?#???#??#. 7,1
..#??##?#????#???##? 2,11,3
?#????????.???#??? 3,1,2,4
?#?.??.#????.. 2,2,5
?#.?#??????##.??#?? 1,1,7,4
???##??###??..#? 1,2,6,2
?#????#?????. 7,1
#?????##?#? 2,2,4
#?.??#??..#??#?#?? 1,4,1,1,1,1
#??????..??##?.? 6,1,3,1
???#???.#??#?? 4,2,1
?..??#?????? 4,2
???????#???.#??#???? 3,4,1,1,2
##???#?#?.??????. 3,3,4
?##?.#..?#??#??#? 2,1,1,1,1
?#???????#?? 2,5
????#?????. 5,1
?.??.#???#???? 2,8
??#.?????#???###???? 1,1,1,1,1,9
?#?????#.#????.?..?? 1,4,4,1,1
.???.##????????. 2,1
#.?#??#????#??? 1,1,10
????.?.#.#??##?#??? 1,1,1,1,1,7
???#????##?.?? 8,1
?.#??.??????###.??.? 1,2,2,5,1,1
??#??.#?.. 1,1
??????????????#?? 1,5,5
????##??.?#.??? 1,3,1,1,3
?????##??.#????#?.? 7,1,1,2,1
#??.?#???. 1,1,3
.?#??????#??.#?#?? 2,1,5,1,1
???##.??.????#?. 5,2
???????#?#?#????# 1,7,1,4
?..?#...?.? 2,1,1
????????#??? 1,2,2
.?#?????#???.#?.?.?# 11,2,1,1
?.?.??#??????????. 6,1
??.?????##??# 1,3,2,2
??##.###?#?#?#?. 1,2,9
????.##?????? 2,2,2
.?#??##??# 6,1
?#????#????? 2,1,1,4
.???#?#???.#??# 3,3,4
???#?????#.?? 1,2,5,1
????##??#???#. 8,1
?#??????..?.???? 3,2,1
???????#????##??? 3,4,5
??.##.???? 2,1,1
??..#??..???# 2,2,1,1
?#??.?#?#??????? 3,2,2,1
##?#??????###?#.???. 15,1
??.???????#?.? 3,3,1
?##????.?.? 3,2,1
???.????###??# 2,7,1
#????#?#??#?###????? 1,2,13
????????????.#????. 1,8,1,1,1,1
#?????#??#????? 4,1,2,1,2
??????????#.??.?.#? 1,7,1,1,1,1
?.??#??????#??#??# 1,1,3,1,1,2
??.??##?..?#???. 1,4,1,2
?.?#..???.?# 1,1,1,1
???.#??#??????. 2,2,2,2
.??#?????#?#??????.? 3,8,1
??#??#?#??#????.#??? 11,1,3
????#??????? 1,3,1
?##???#???.???? 2,6
?#?#?#?????. 5,1
#?..????.. 1,1,1
????##?????#??? 1,5,1,1,1
.?###??????#??????? 12,2
.????..??#.? 1,2
???##..#????. 1,3,1,2
##?#?#?##.??? 6,2,1
?.?.??.?.##??????.? 1,1,4,1,1
??#??.#???..?????? 2,4,6
?#???.???.??? 4,2
.??.???.#####??? 3,7
????.?????#?????. 1,2,4,2,1
?????##?#??#? 1,10
.?.?###???#???#?? 4,1,1
.#?.????#???.?#. 1,8,1
?###?#?????.?.?#?. 9,1,3
?.?##.??#.??.?.##??. 1,3,2,1,4
??????.??? 2,2,1
????.????????#?#??#? 2,1,2,9
?????#???????? 6,2
?#.?#??..?. 1,3,1
????#???.#.???. 2,1,1,1,1
##?..??.??#..??????? 3,2,4
.????###???.?.??? 8,1,1
????.?.??. 4,2
.??#.?????##?.?#.?#? 3,7,2,2
?#????.????# 1,1,1,2
??#??####?##???.?? 1,11,1
???#??#???#???.??? 1,9,1,1,1
?#???#???.??# 2,2,2,1
?????.???#??? 3,7
?..#?.??#.?????? 1,1,1,1,6
????#...#...?.? 4,1,1,1
.?#???..????? 3,1,1
??###??#???????##?# 5,12
?#?????#?? 4,1,1
??????????.?#? 1,1,2,2
#.???????????.?#?.? 1,6,2,1,1
???.?#???#??##???##? 1,4,2,4,3
????....?#?###. 3,6
?????.?.#??? 1,1,1,2
?#??..##?#?#??.???? 1,1,4,2,2,1
??#????##???? 7,3
..????.????. 2,2
???.???.##?#?#?#? 1,1,9
.???.??.?. 1,1,1
.####???????#.??. 7,2,1
#?#?##??.?#??.?#?? 1,1,2,3,2
##?##???#??.???? 6,2,2
?.###???????#? 6,2
??????#..?...????. 4,1,1,1,1
?..??##????#?. 1,4,2
???#??????#?. 5,1,1
????????#????? 1,1,4,2
???.???.?#?? 1,2,1
????#.??#? 1,1,2
.??#??##??#????.? 9,1
??.?..?#?????## 1,1,9
??#???..???????. 4,5
#..?.#????.???#?.??? 1,1,5,4,1
?.#?.?#??##?#..??? 2,7,1
.?????.?#?##??? 1,7
???????#??.?#?? 3,2,4
.???#??#??????#? 9,1
???#??.????. 1,2,1,1
??.?.?#?.????#???? 2,1,8
??#????#.?##?????? 1,3,1,3,2,2
????#???#???? 2,2,3,2
#.????.#??????. 1,1,1,6
?#???..??#?#?.? 3,1,1,1,1
??.??#?#??? 1,6
???.#????##???? 2,4,1
.???????#?# 4,1,1
#???##..???#?#? 1,4,1,1,2
#??#??#?.???????.#? 1,5,2,1,2,2
..?.?#????#???##???? 1,13,1
?#??#???###??? 3,3,5
.??##????## 5,2
???.?.???#???.# 1,1,4,1
??.?????.????#?.??? 1,1,2,6,2
##??.#?#?? 3,5
.??????.?#??. 1,2
?????.?..#?#? 3,4
.??.???#??? 1,3
??#????#??????# 1,8,1,1
??.??#?.?????##???#? 4,3,6
?.#?#?#?#.????#??#?? 7,4
??????????#?. 3,3,1
????#?.??#?? 5,3
#???????.?.#?# 1,4,1,3
#.??#.#??.??.?#.?. 1,3,2,1,2,1
???#?.???#? 3,1,2
????#.???#???##?#??? 1,1,5,7
?#??##?.???#?#?.#? 1,2,6,1
?##?????##??? 3,3
??????????#??? 4,2
????.???##? 3,1,4
.????#?.??.??.??? 1,2
?..##?#??????????? 5,5
????????.?#?? 5,2
?###???????????.? 9,1
?#.?#??#..????. 1,2,1,3
??.#???.?????..???? 1,1,1,4,1,1
#?#?#?.???##???? 1,3,2,3,1
??.?.?#???#????#??? 2,1,3,1,5
?#??#?.#??????#. 4,2,1,1
??#???#??? 2,4
#??#?##?????#?? 2,1,2,1,2
#?##.?#???#??? 4,1,1,1
.???##.##.# 5,2,1
#???.#???????### 1,1,1,9
??##??????. 4,2
?#??#????.?.?? 4,3,1,2
?.#?#????.#???????# 1,6,1,3,2
?????.#??? 4,1
.????#?##?#??? 1,8
??#??.#.????? 2,1,1,1
.???.???..? 1,2,1
?#?#?.???# 5,1
???.#?.????.#? 1,2,2,1
.#.????#????#.???? 1,6
?.#?#?##.?.??? 6,1
???#?..##?#?.?? 3,5
#???##?##??#.??.#..# 12,1,1,1
?#?#?#???#?#?? 6,4
#??.???###? 1,6
????.#.#???######?. 1,1,2,7
??#.?#?#??#???. 1,8
?????????.???..??. 1,7,1,1
.??#?#????#???? 1,1,3,1,2
#??.?#????##???#?#? 3,1,1,9
?.????#???????????. 3,1,5,2
??.?#????.#??? 1,1,3,1
?.???????.?. 6,1
#?#??#.??#?#??## 1,4,7
.?.?###???..?#? 5,2
???#??#??#?#?###??? 5,8
?????.??.?. 4,1
.?.???#?##????? 1,4,2
????????.??.????..? 6,1,4
????.?#?#? 1,3
??#??.#??????#? 1,1,3,1,1
#?.?????.?.#?##?. 2,1,1,4
?#??#??????# 2,2,3,1
?#?#?????..??#?#?#? 2,1,1,1,8
?##?.?#?####? 4,7
#?????.#??.? 1,2,3,1
?#??????..?? 1,4,1
.##???##?#?.?? 10,1
????##?????.???.?.# 1,7,1,1,1,1
?#??????#??? 2,2,2
?#???.??.????.#?? 3,1,1,1,2
.?.???..##?##??#?#? 1,1,6,3
?????#?.??#. 1,4,1,1
?.?.#?.#?#????##.??. 1,1,2,9,1
???.?##???..#.?? 1,4,1,1,1
?????#????#?#???. 1,10
.??????#???. 8,1
??????#?#?#.?. 9,1,1
#?.??????..? 1,1,3,1
?#??.??.?.?. 1,1,1,1
??????#??.???.?? 5,3,1,2
#????#?.####??#?#? 1,1,1,9
..??#???#..# 1,2,1,1
????????.?.?.??.???? 8,1,1,1,4
???.??.???.???? 1,1,3,4
?#??.?????# 1,2
?#????#??????????? 2,4,1,1,1
???.#?##?#?????? 1,9
#.???#?????.?#???.? 1,6,1,2,1
?#..????????? 2,1,2,3
???#.???##.??.?. 2,3
??#?????????? 5,1,1
?#????.#???? 4,1,1,1
??..?#?##????????. 1,7,1
?????#..??..# 4,1,1
??..#?????.??#?????? 2,4,1,3,1,3
???????????????#?.?# 1,4,5,2
#?.?????.#??????? 2,4,1,5
.?.???#??..??????#?? 1,4,1,6
??#?#?.#??# 3,1,2
#?#??????????##? 1,1,6,4
?.???????? 1,2
.??#??.????? 1,3,1,3
.?#?##?.#?.??#?? 2,2,2,2,1
?#???????? 1,2
???#?#.#??#???????? 1,1,1,3,2,1
.??..????? 1,1,1
???.????.? 1,3,1
?????#?????????#? 6,1,2
.?.#??.?.?..?#?###?? 1,6
#?#??#?.???# 4,1,1,1
?#????#.??. 1,3,1
????.??#..????????? 2,1,3,2,4
?#?..????##.. 2,5
??.##..?.?#? 1,2,1,1
???#####??.??.?????? 9,5
??#??#??#??????.???? 2,8,1,1,1
??????????#???.? 6,4
?.?#??.#.??#??##.?#? 1,1,1,1,7,3
??..#?.??? 1,1,2
??#?#?#?#??#. 9,1
?##??##???????#??? 8,3,1
#??#??.?#.? 1,3,1
?????#?..????#?#? 4,2,2,1,1
?.??.?#??? 1,1,1
??#??..#?..? 1,1,1,1
.????.????#???? 1,6
??#????##??.??#?.? 9,3
??#???.#??????#??.? 2,2,1,1,5,1
?#??#?###?.?.??? 9,1,2
?????????? 4,3
#?????????.??.?? 1,1,1,3,1
.??????..?? 4,1
????.????.?.?# 2,3,2
??..?.?.?#? 2,1,1
??#?????#?. 1,3
???#??#??.?. 2,5
.??#?###??#.?#. 9,1
???.???#?.? 1,4
?????#.?.?#?. 2,1,2
?#?.??##.. 3,2
?#????#?.#?.?. 3,4,1,1
.?#.?##.??#? 2,3,1,1
..?#?????? 6,1
???...??#?..??? 1,1,1,2,1
????#?????????# 1,2,1,1,4
???#???#??##??? 4,2,3,1
??#?#???##???# 1,4,4,1
.?????#?#. 1,1,1
#.??????#???..??.??? 1,1,5,1,2,2
?.??.???..?## 1,1,3,3
?..??#????##.??? 1,1,2,3,2
??.?#.?.#.. 2,1,1
????.??????.#.#?# 1,3,1,1,3
?????#??##..?#. 2,3,2,1
?.??##?.??#?#???? 2,6
#?????#.#??##?.# 1,2,1,6,1
?#.??###??.????? 1,5,1,4
##?????#???????.?. 9,1,1,1,1
??????#???#??#?? 1,1,1,5
???#.?#??????##? 2,2,1,3
???.?.#????#???..??? 2,8
.?.?#.????#??##???? 2,11
#???#??#??????##?#?# 2,2,5,2,3
???.#????..?? 1,5,1
??#?.#??##??.?????? 3,6,4
.????.#?#??##??? 2,10
??.#?..?????????# 1,1,2,1,4
?.???#?..??.??#?? 1,3,1,2
#??#???.????##?#?. 7,6
?#.??#?.?#.????#.?# 1,3,1,4,1
???????##??##??##?? 2,6,3,3
#????????????##?.. 9,4
?#..?##?.???? 1,3,4
.?.#??.??.? 2,1
.???#????. 1,2,1
??????#???#.?. 1,6,1
.????#??????#??#..? 2,4,1,2,1,1
?#?..#?.???#????? 2,2,7
??.?#?##.#.?#????? 1,4,1,3,1,1
?.????#???. 1,4,1
.???.?????? 1,2,1
????.?#??##???? 3,8
.?.##?.??#.?# 2,3,1
.?#??#?##???#.?? 1,8,1
?##?????#???? 3,1,4,1
???????????#.???#### 1,1,4,7
??#?..?#???#?? 3,2,2
?##?.??#.??.?.?? 3,3,1,1
?????##?###.??#? 3,6,1
?#???#??#????? 8,1,1
???.#??###??#?##?#? 1,7,1,2,1
#?#????.#?????? 5,1,1,1,2
????##?###??#. 1,1,6,2
?.#??#?#?#???. 2,5,1
#????#?#????? 2,4,1
#?#?????##??.???. 11,2
????#??.??? 4,1
.??.?.???# 2,1,1
??.#?.#..???.?. 1,1,1,2,1
???????#??. 7,1
????#??##? 5,2
#??.?#?.?#?#??#?? 3,2,9
?###????#?#?#??.??. 15,1
?.##?????????#??#? 6,4
????.?#.?#?#? 2,1,5
?#?..?#?## 3,2,2
?#??????#??.??#?. 2,3,1,1,1
????.????#??. 1,1,4
#.??##????? 1,8
??#??#?.????#?# 6,1,5
????#..???#?? 4,5
???????#?###?? 1,1,6
.??????..###? 1,1,1,3
???????#?.#??##??##? 1,1,2,9
.????????##?#???#??? 2,2,11
.#?.##?##????.??#.? 1,9,1
.?.???#?#??####????# 1,1,11,2
???????..? 1,2,1
??.??#???? 2,2,1
?????#?.??? 3,2,1
????#?.##???#?.???? 4,7,2
#?.???????#??.#?? 1,4,3,1
.?#?#?##?#????????. 4,12
???#?#?#?##?..???? 10,1,1
?????.??#?.??.?.?? 1,1,4,1,1,1
.#?.????.?? 1,1,2
?????#??????#? 7,2
???.?.?????.??..?.. 2,1
?#?#.?????####????? 3,11
???????#???#? 2,1,2,1
??#?.?.?#?? 3,3
####???.?? 4,1,1
??????.##?. 1,2
????##.?#?.. 1,3,2
??#???#?#?#.??#? 10,2
??????#???????.?#??? 1,3,4,2,1
??????#?##????#??.?? 1,10,1
#????#??????# 6,1,1,1
??????#??##???#?. 7,3,2
??.?#.#?#?. 2,1,4
.?#..???#?.? 2,1,2
.#?#?##?.?#?. 1,4,1
.?.?..#.#? 1,2
??..??.?????#?#? 2,2,1,1,1
?????????.???#???? 2,5
????.#????#?????.??? 1,1,1,9,1,1
.??##???????? 5,2,1
??#?#?.?.??#???#? 5,1,2,3
.??#?????..? 5,1
??#????..??????#?.? 7,3,2
??????.?#??# 4,5
?#??.????#?? 2,4
?.??#?##??.??? 8,1
#??###????#??.?? 7,1,3,1
??#?.????.#?#????? 2,1,1,5,1
??#?##?.#?.?.#?#??? 5,2,4
..????????.? 2,3
#????#???.?#?#?? 6,1,2,1,1
??.??#????#?? 1,4,3
???#?#?.?.#?? 1,4,2
??.??.??#?? 2,1,2
.???.?.?#?#??# 1,7
?...#????.?#?. 5,2
??##?#?#?? 3,3,1
??.?.##??#?#??.?? 1,8,1
#?????.?????#?? 1,1,8
????#.#.##?? 2,1,1,4
?.???..??. 1,1,2
??#???#?#????#???#.# 2,10,1,1
????????#????#?? 1,1,4,3
.?#?.???#? 1,1,1
????#????????.#?.# 1,6,2,1,1,1
?#..??????.???????# 2,1,2,7
??#.???#???????. 3,1,2,3,1
??#?#.?????..???? 5,1,2,1,1
???????????.#.#?.?. 2,4,1,1,2,1
??..#?####??#.????.? 9,2
??..??.????. 1,1,1,1
?#?#???#?...# 2,5,1
#?.?.?.?.?#? 1,1,1,1
?#.?????#?#??#?##??. 1,2,12
??.??##.#?.?#.?. 1,2,1,2,1
?????#?.???.??.?? 1,3,2,1,1
??#???.??? 1,1
.#?...??.????#?????# 1,1,1,6,2
??????#????. 1,7
??????#????? 2,3,2
?????????##??????? 9,1
#?###???#??.???????# 5,3,1,2,2
??#?.?#????.??.. 4,1,1,2
?###?????# 7,1
??#.?#?###.? 1,1,6
??..???????? 1,1,1,1
?###?#???????#.. 9,2
.??.?.?????#?.#? 2,2,4,2
?..?#.?.?#???#??? 1,1,1,2,4
???#???????????.. 7,1
?#?##?#.??#?.##??? 1,4,3,3,1
?#???.???. 4,1
??????##?#?.#? 1,7,1
..?#?????.? 2,1,1
??#????#??#??#??? 10,4
.??#???#?#.?#??## 3,3,6
?##??###???..?##???? 8,1,3,2
?.?#?#?.?.????#??#?? 4,8
????????????#.. 1,8
#.?.????##???.?#. 1,1,1,6,1
.?##???????. 3,1
.???.??.???##? 2,1,3
????#???#.? 2,2
????.??#??#??#?#? 1,12
???#.??#?#???? 2,4
?#...??#???? 2,3
?#????#???? 1,3,2
???.###?#???# 1,5,2
?????#???#???#.?? 1,1,10,1
??##??#?????.??#? 12,3
?????????#?.?.#? 1,2,1,4,1
#???#??.#???##?? 2,1,1,5
?.?##???.. 3,1
???#?##?.?? 1,3,2
####.?????#???# 4,1,7
?????#????##? 1,7
?.?#??#.??#.??. 5,3
#???????.??? 4,1,1
???#????#.? 2,1
.##??.?.#####?.. 4,6
????#.?##.??.?## 4,2,2,2
???????.????##?? 5,1,2
?#?#???#?.# 1,6,1
???#.?.???????#?.#.? 1,1,1,9,1,1
?.#??#??.???? 1,1,1,1
?????#????#.?? 3,6,1
##???.#?.??#. 2,2,1,2
????.?#?#??????????? 4,1
??#??????#???.????? 5,1,2,1,1
??.?#..#????? 1,1,1,2
???.????##????#?.#? 1,1,10,2
?.#????#????.??#? 1,2,3,1,3
?###?.?###.?.#?? 4,4,2
#???????..??# 2,1,1,3
##?????##??#.?.???.# 12,2,1
.??????#.?.??#???? 5,1,1,1,1,1
??.???.?.?. 1,2,1
??#?#?##.?????? 6,3
.?.??.?#??? 2,1
.?.?##?#?##?.?.#? 1,9,2
.?????##?.? 1,5
??#???????#???. 3,7
??.?#?..??##??#?? 2,8
??##??.?#?#.?.?? 6,1,1,1,1
???#??????.? 2,1,1,1
??.????#..???.?#??? 1,1,1,1,2,5
.##?#???#??###?????. 6,10
.?.?.?.??##.. 1,2
??????#???#???? 1,2,2,1,4
?.?????.#??? 5,2
????#??###??.??.?#?? 1,8,2,2
?#????#????#??.??. 3,3,4,1
??#??..?.????.? 4,1
.#?#????#?#??? 5,1,3
.##????#????. 2,1,5
???#????#??.??#?#??? 1,2,4,1,1,1
.??#?#?????#?#????#? 1,1,1,12
?#.#.?.??.###?##??# 1,1,1,6,1
?.??????#?.????? 1,1,1,1,4
??????#????..?#?? 11,2
??##????????#..? 1,7,1,1,1
??.?###???. 1,5
????##?#?#???# 1,7,3
????#?????##?..??? 3,2,1
??#?????#?.??.??.? 1,8,1,2,1
??.?###?#??#?#??? 1,12
?#???????? 3,2
.???????..?##? 1,1,4
#?.???#??????#?#? 2,4,5
????#???#.. 1,1,2
??#???#?????.??.?#?? 3,1,2,1,2,1
..????.??? 1,1
.????#???#?? 1,3,1
???##.?.???.?? 5,1,1
?.?????.?????#???. 3,1,3
???.#??#????#???? 3,2,1,6
????##?.?? 1,4,1
???#????????#? 1,5
...#???##??????????? 2,12
#.?.??.????????? 1,2,1,2,1
????.?#.???#?. 1,2,1,2
??#???#.???# 2,1,1,1
?###.?.?.#?.# 3,1,1,1
####?..?##??# 5,6
?.?.#.?##????#? 1,1,3,3
?#.?#.?##?#..#?? 2,1,4,3
??.??????..??? 1,2,2,2
?????.?.#???.???#??. 4,3,5
?#??#??.???##. 6,4
???#?????? 3,1,1
.????????#??.???.?.? 10,1
?#?????????# 3,4,2
.#??.?#?##??.?? 2,7,1
.??#??.#.?.#???. 3,1,1,2
????.?????? 1,4
????#?????.??. 6,1,2
..#??#????#???? 9,2
?.?.??.#?? 1,3
?#?????#?.??????. 2,3,1,3
???????#.?????#? 1,2,6
.?.?.?.#??????.?. 1,3
##?###?##??#??????. 2,10,1
??###???.?#????????? 4,1,3,1,1
??##????.????#.?.? 6,1,1,1,1,1
.#?#???..??.#? 3,1,2,2
?#?#?##?#??#???#??? 2,7,1,5
???.?#??#??#?## 1,2,7
???????????.??? 1,8,1,1
..#?##????.? 4,1
#??##?#???#?#?#? 1,13
..#???????????.?? 1,1,1,5,1
??.??????.? 1,1
?#??.????.?.?.. 4,1,1,1,1
?????????##?#???? 5,8
#??.???????#?? 1,1,5,3
#?#???#?.??? 1,1,4,1
?..?#?.####.? 2,4
.???##.?##?#????. 1,2,3,3
?????.#?##??????? 1,11
?????##?#??#.?.????? 9,1,1,2,1
???##?#???? 5,2,1
???.???#??????# 1,1,1,2,5
???.???#?. 1,3
???##?????????. 5,3
?#?.#.??#.#???#? 1,1,2,1,2
?.?##?##.?.?.?#?? 5,4
?????.?.?#??.#????.? 5,2,2,1,1
.??.???##???????? 2,1,6,1,1
.?.??..#???. 1,1,1,1
.???.#.??#?? 1,1,1,2
.???.#.#??##?#?.# 2,1,2,4,1
?#.?.????.#? 1,1,1,2
??##?##??.????.?.?. 9,2,1
????..????#.? 1,4
?#??#????????#.????? 8,1,1,1,1
????#.??#???#. 4,1,2
?#?#??#???#. 5,1,1,1
??##?##??#???#.#? 10,2,1
.?#??.?##?.??#? 4,4,1,2
#???##.??.#?? 2,2,1,2
.????#??#????.??..# 9,2,1
?#?..?#????#??###? 1,2,7
#?.#..??#?.? 1,1,4
?#???#??.???#??#? 6,1,1,1
.?##???.??#?????? 3,7
??.??.?#????.?. 1,1,6,1
??#??#???.?#??.? 1,5,3,1
..??????#?.??#?##?.? 7,6
?#?????#???#?#?#?? 1,11
.?????.?????.#?#? 1,1,5,1,1
???#?.?#??? 3,4
?????.????.#??. 1,1,1,1,3
?#????.???#??#?????? 1,1,1,8,1
?#.#?????? 1,2,4
??#????????#?##???? 4,1,9
???.?.?????? 2,1,1,1
##???#?#????.#.????# 9,1,1,1,1,1
??.?????.?. 2,5,1
?.????????????.??. 1,4,2,1,1,1
#?#??#???#??? 1,1,1,2
?#??????#??#??# 2,1,1,1,5
#??#??#..???? 1,5,1,1
#...#?????.? 1,1,1,1
#?...????...??? 1,4,2
?##??.??..##???# 4,1,6
??..???### 1,4
?#.?.?????#?.???#? 1,1,1,1,3,4
###???#???#?##???#? 4,13
?#?????????? 3,4
?###?#????.?.#????# 10,1,1,1,1
????.?????#??. 3,7
?###???##?#?#.?#??? 9,3,3
??????.??????#???.? 2,4
?.?#????.? 3,1
.??##????????.????? 11,3
?.?????#??#?#???? 1,1,1,1,4
???.#?#?.????? 1,1,1,5
??#??.???#?. 1,3,2
??#...?#???? 2,6
    ''')