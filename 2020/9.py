#!/usr/bin/env python3

import lib.common as lib
import time

def contains_sum(num_list, result):
    for idx, x in enumerate(num_list):
        if result - x in num_list[idx+1:]:
            return True
#        for idx2, y in enumerate(num_list[idx:]):
#            if result == x + y:
#                return True
    return False

def find_non_summable(numbers, preamble):
    idx = preamble
    while idx < len(numbers):
        if not contains_sum(numbers[idx-preamble:idx], numbers[idx]):
            return numbers[idx]
        idx += 1
        
def part_one(line_gen):
    numbers = [int(line) for line in line_gen]
    return find_non_summable(numbers, 25)

def part_two(line_gen):
    numbers = [int(line) for line in line_gen]
    target = find_non_summable(numbers, 25)
    check_len = 2
    result = None
    while not result:
        idx = 0
        while idx + check_len < len(numbers):
            if sum(numbers[idx:idx+check_len]) == target:
                result = numbers[idx:idx+check_len]
                break
            idx += 1
        check_len += 1
    return max(result) + min(result)

print("A: " + str(part_one(lib.get_input(9))))
print("B: " + str(part_two(lib.get_input(9))))
