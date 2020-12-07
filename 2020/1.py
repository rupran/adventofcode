#!/usr/bin/env python3

import lib.common as lib

def part_one(line_gen):
    numbers = [int(line) for line in line_gen]
    return [x * y for idx, x in enumerate(numbers) 
                    for y in numbers[idx:] 
            if x + y == 2020]

def part_two(line_gen):
    numbers = [int(line) for line in line_gen]
    return [x * y * z for idx, x in enumerate(numbers)
                        for idx2, y in enumerate(numbers[idx:])
                            for z in numbers[idx2:] 
            if x + y + z == 2020]

print("A: " + str(part_one(lib.get_input(1))))
print("B: " + str(part_two(lib.get_input(1))))
