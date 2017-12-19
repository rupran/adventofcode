#!/usr/bin/env python3

import lib.common as lib

def part_one(line_gen):
    line = next(line_gen) # one line input
    increment = int(line)
    lst = [0]
    idx = 0
    cur = 1
    while True:
        idx = ((idx + increment) % len(lst)) + 1
        lst.insert(idx, cur)
        if cur == 2017:
            return lst[(idx+1) % len(lst)]
        cur += 1

def part_two(line_gen):
    line = next(line_gen) # one line input
    increment = int(line)
    lst = [0]
    idx = 0
    cur = 1
    val = -1
    while True:
        idx = ((idx + increment) % cur) + 1
        if idx == 1:
            val = cur
        if cur == 50000000:
            return val
        cur += 1

print("A: " + str(part_one(lib.get_input(17))))
print("B: " + str(part_two(lib.get_input(17))))
