#!/usr/bin/env python3

import lib.common as lib

def run(numbers, iterations):
    seen_in_move = {}

    for idx, n in enumerate(numbers):
        seen_in_move[n] = idx + 1

    cur_move = len(numbers) + 1
    last = 0    # provided all numbers in input are unique
    while cur_move < iterations:
        if last in seen_in_move:
            diff = cur_move - seen_in_move[last]
            seen_in_move[last] = cur_move
            last = diff
        else:
            seen_in_move[last] = cur_move
            last = 0
        cur_move += 1
    
    return last

def part_one(line_gen):
    numbers = [int(n) for n in next(line_gen).split(',')]
    return run(numbers, 2020)

def part_two(line_gen):
    numbers = [int(n) for n in next(line_gen).split(',')]
    return run(numbers, 30000000)

print("A: " + str(part_one(lib.get_input(15))))
print("B: " + str(part_two(lib.get_input(15))))
