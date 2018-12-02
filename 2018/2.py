#!/usr/bin/env python3

import collections
import lib.common as lib

def part_one(line_gen):
    twos = 0
    threes = 0
    for line in line_gen: # multi line input
        count = collections.Counter(line)
        twos += int(2 in count.values())
        threes += int(3 in count.values())
    return twos * threes

def part_two(line_gen):
    ids = list(line_gen)
    for idx, first in enumerate(ids):
        for second in ids[idx+1:]:
            diff = 0
            equal = []
            for i in range(len(first)):
                if first[i] != second[i]:
                    diff += 1
                else:
                    equal.append(first[i])
            if diff == 1:
                return ''.join(equal)

print("A: " + str(part_one(lib.get_input(2))))
print("B: " + str(part_two(lib.get_input(2))))
