#!/usr/bin/env python3

import collections
import lib.common as lib

def gen_occurrences(line_gen):
    occurrences = collections.defaultdict(dict)

    for line in line_gen:
        for idx, _ in enumerate(line):
            if line[idx] not in occurrences[idx]:
                occurrences[idx][line[idx]] = 1
            else:
                occurrences[idx][line[idx]] += 1

    return occurrences

def calc_solution(line_gen, fun):
    occs = gen_occurrences(line_gen)

    return "".join(fun(occs[x].items(), key=lambda a: a[1])[0] for x in occs)

def part_one(line_gen):
    return calc_solution(line_gen, max)

def part_two(line_gen):
    return calc_solution(line_gen, min)

print("A: " + str(part_one(lib.get_input(6))))
print("B: " + str(part_two(lib.get_input(6))))
