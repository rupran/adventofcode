#!/usr/bin/env python3

import collections
import lib.common as lib

def gen_next(state):
    cur_state = ["."] + state + ["."]
    next_state = [None] * len(cur_state)
    for i in range(1, len(next_state) - 1):
        next_state[i] = "."
        if cur_state[i-1] != cur_state[i+1]:
            next_state[i] = "^"

    return next_state[1:-1]

def count_safe(line):
    return collections.Counter(line)['.']

def simulate(line_gen, count):
    state = list(next(line_gen))
    total = count_safe(state)
    for _ in range(count - 1):
        state = gen_next(state)
        total += count_safe(state)
    return total

def part_one(line_gen):
    return simulate(line_gen, 40)

def part_two(line_gen):
    return simulate(line_gen, 400000)

print("A: " + str(part_one(lib.get_input(18))))
print("B: " + str(part_two(lib.get_input(18))))
