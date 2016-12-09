#!/usr/bin/env python3

import lib.common as lib

def get_index_count_repeatlen(line, index):
    next_count = 0
    repeat_len = 0
    
    index += 1
    char = line[index]
    while char != "x":
        next_count *= 10
        next_count += int(char)
        index += 1
        char = line[index]
    index += 1
    char = line[index]
    while char != ")":
        repeat_len *= 10
        repeat_len += int(char)
        index += 1
        char = line[index]
    index += 1

    return index, next_count, repeat_len

def eval_pattern_length_one(line, offset, length):
    index = offset
    cur_len = 0
    while index < offset + length:
        char = line[index]
        if char != "(" and char != ")":
            cur_len += 1
            index += 1
        else:
            index, next_count, repeat_len = get_index_count_repeatlen(line, index)
            cur_len += (repeat_len * next_count)
            index += next_count

    return cur_len

def eval_pattern_length_two(line, offset, length):
    index = offset
    cur_len = 0
    while index < offset + length:
        char = line[index]
        if char != "(" and char != ")":
            cur_len += 1
            index += 1
        else:
            index, next_count, repeat_len = get_index_count_repeatlen(line, index)
            cur_len += eval_pattern_length_two(line, index, next_count) * repeat_len
            index += next_count

    return cur_len
    
def part_one(line_gen):
    line = next(line_gen)
    return eval_pattern_length_one(line, 0, len(line))

def part_two(line_gen):
    line = next(line_gen) # one line input
    return eval_pattern_length_two(line, 0, len(line))

print("A: " + str(part_one(lib.get_input(9))))
print("B: " + str(part_two(lib.get_input(9))))
