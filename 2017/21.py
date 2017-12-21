#!/usr/bin/env python3

import re

import lib.common as lib

def gen_all_rules(in_rule):
    in_rule_arr = in_rule.split('/')
    size = len(in_rule_arr)

    # Original
    retval = set([in_rule])
    # Flip up/down
    retval.add('/'.join(reversed(in_rule_arr)))
    # Flip left/right
    retval.add('/'.join(''.join(reversed(x)) for x in in_rule_arr))

    # Rotate original and flipped versions
    for trans in retval.copy():
        in_rule_arr = trans.split('/')
        # Three left rotations to cover 90, 180 and 270 degrees
        for _ in range(3):
            next_list = [[0 for _ in range(size)] for _ in range(size)]
            for idx, item in enumerate(in_rule_arr.copy()):
                for idx_2, _ in enumerate(item):
                    next_list[idx][idx_2] = in_rule_arr[size-1-idx_2][idx]
            in_rule_arr = list(''.join(x) for x in next_list)
            retval.add('/'.join(in_rule_arr))

    return retval

def print_pattern(pattern, step):
    print('===== Step {} ====='.format(step))
    for _, row in enumerate(pattern):
        print(''.join(row))

def draw(rules, iterations):
    pattern = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
    size = len(pattern)

    for _ in range(iterations):
        for modulus in [2, 3]:
            if size % modulus == 0:
                n_patterns = size // modulus
                new_patterns = [[0 for _ in range(n_patterns)] for _ in range(n_patterns)]
                # Go through the pattern in modulus-sized steps, generate input
                # pattern for the current NxN square and find output pattern
                for start_y in range(0, size, modulus):
                    for start_x in range(0, size, modulus):
                        rule = '/'.join(''.join(pattern[y][start_x:start_x + modulus])
                                        for y in range(start_y, start_y + modulus))
                        new_patterns[start_y//modulus][start_x//modulus] = rules[rule]

                # Expand 2D list of new patterns into actual new pattern
                new_width = modulus + 1
                new_size = n_patterns * new_width
                pattern = [[0 for _ in range(new_size)] for _ in range(new_size)]
                for y_idx in range(n_patterns):
                    for x_idx, patt in enumerate(new_patterns[y_idx]):
                        patt_lst = patt.split('/')
                        for r_idx, row in enumerate(patt_lst):
                            for c_idx, val in enumerate(row):
                                pattern[y_idx * new_width + r_idx][x_idx * new_width + c_idx] = val

                size = new_size
                # Break to avoid evaluating both moduli in one iteration if the
                # new size is dividable by the second modulus as well
                break

    return sum(c == '#' for lst in pattern for c in lst)

def gen_rules(line_gen):
    rules = {}
    for line in line_gen:
        left, right = re.match(r'(.*) => (.*)$', line).groups()
        for rule in gen_all_rules(left):
            rules[rule] = right
    return rules

def part_one(line_gen):
    return draw(gen_rules(line_gen), 5)

def part_two(line_gen):
    return draw(gen_rules(line_gen), 18)

print("A: " + str(part_one(lib.get_input(21))))
print("B: " + str(part_two(lib.get_input(21))))
