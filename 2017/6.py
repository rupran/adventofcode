#!/usr/bin/env python3

import lib.common as lib

def redistribute(numbers, index):
    val = numbers[index]
    numbers[index] = 0
    while val > 0:
        index = (index + 1) % len(numbers)
        numbers[index] += 1
        val -= 1

def calc(line_gen, second_part=False):
    numbers = [int(x) for x in next(line_gen).split()]
    seen = {}
    counter = 0
    while True:
        last_state = tuple(numbers)
        if last_state in seen:
            if second_part:
                return counter - seen[last_state]
            else:
                return counter
        seen[last_state] = counter
        idx = numbers.index(max(numbers))
        redistribute(numbers, idx)
        counter += 1

def part_one(line_gen):
    return calc(line_gen)

def part_two(line_gen):
    return calc(line_gen, True)

print("A: " + str(part_one(lib.get_input(6))))
print("B: " + str(part_two(lib.get_input(6))))
