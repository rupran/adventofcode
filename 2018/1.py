#!/usr/bin/env python3

import lib.common as lib

def part_one(line_gen):
    return sum(int(line) for line in line_gen)

def part_two(line_gen):
    freqs = set()
    cur_freq = 0
    in_list = list(line_gen)
    while True:
        for line in in_list:
            cur_freq += int(line)
            if cur_freq in freqs:
                return cur_freq
            freqs.add(cur_freq)

print("A: " + str(part_one(lib.get_input(1))))
print("B: " + str(part_two(lib.get_input(1))))
