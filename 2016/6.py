#!/usr/bin/env python3

import collections
import lib.common as lib

def gen_occurrences(line_gen):
    occurrences = collections.defaultdict(dict)

    for line in line_gen:
        for idx in range(len(line)):
            if line[idx] not in occurrences[idx]:
                occurrences[idx][line[idx]] = 1
            else:
                occurrences[idx][line[idx]] += 1

    return occurrences

def calc_solution(line_gen, fun):
    occurrences = gen_occurrences(line_gen)
    msg = ""

    for idx in occurrences:
        msg += str(fun(occurrences[idx].items(), key=lambda a: a[1])[0])

    return msg

def part_one(line_gen):
    return calc_solution(line_gen, max)

def part_two(line_gen):
    return calc_solution(line_gen, min)

print("A: " + str(part_one(lib.get_input(6))))
print("B: " + str(part_two(lib.get_input(6))))
