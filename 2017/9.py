#!/usr/bin/env python3

import lib.common as lib

def parse(line, idx=0, cur_score=0):
    local_sum = cur_score
    ignored = False
    garbage = False
    garbage_count = 0
    while idx < len(line):
        cur_char = line[idx]
        if ignored:
            ignored = False
        elif cur_char == '!':
            ignored = True
        elif garbage and cur_char != '>':
            garbage_count += 1
        elif cur_char == '<':
            garbage = True
        elif cur_char == '>':
            garbage = False
        elif cur_char == ',':
            pass
        elif cur_char == '{':
            idx, sub_sum, sub_gct = parse(line, idx + 1, cur_score + 1)
            local_sum += sub_sum
            garbage_count += sub_gct
        elif cur_char == '}':
            return idx, local_sum, garbage_count
        idx += 1

    return (idx, local_sum, garbage_count)

def part_one(line_gen):
    return parse(next(line_gen))[1]

def part_two(line_gen):
    return parse(next(line_gen))[2]

print("A: " + str(part_one(lib.get_input(9))))
print("B: " + str(part_two(lib.get_input(9))))
