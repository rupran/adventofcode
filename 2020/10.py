#!/usr/bin/env python3

import lib.common as lib

def knapsack(joltages, idx, cache):
    # Early exit if we were at that index before
    if idx in cache:
        return cache[idx]
    # If we arrived at the last item, we found one way
    if idx == len(joltages) - 1:
        return 1
    # Otherwise, find the valid next indices, continue the search
    # from these indices and add up all possible ways from here
    options_here = 0
    for next_idx in range(idx + 1, idx + 4):
        # We're reaching past the end of our adapter list
        if next_idx >= len(joltages):
            continue
        # The next adapter has a too high joltage
        if joltages[next_idx] > joltages[idx] + 3:
            continue
        options_here += knapsack(joltages, next_idx, cache)

    # Cache the result to avoid duplicate descents through the whole tree
    cache[idx] = options_here
    return options_here

def part_one(line_gen):
    joltages = sorted([int(n) for n in line_gen])
    idx, last, num_ones, num_threes = 0, 0, 0, 0
    while idx < len(joltages):
        cur = joltages[idx]
        if last == cur - 1:
            num_ones += 1
        elif last == cur - 3:
            num_threes += 1
        last = cur
        idx += 1
    num_threes += 1
    return num_ones * num_threes

def part_two(line_gen):
    joltages = [0] + sorted([int(n) for n in line_gen])
    cache = {}
    return knapsack(joltages, 0, cache)

print("A: " + str(part_one(lib.get_input(10))))
print("B: " + str(part_two(lib.get_input(10))))
