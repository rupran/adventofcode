#!/usr/bin/env python3

import collections

import lib.common as lib

def part_one(line_gen):
    preds = collections.defaultdict(list)
    for line in line_gen:
        preds[line[-12]].append(line[5])
        if not line[5] in preds:
            preds[line[5]] = list()
    result = []
    while preds:
        n = sorted(k for k, v in preds.items() if not v)[0]
        preds.pop(n)
        result.append(n)
        for k, v in preds.items():
            if n in v:
                v.remove(n)
    return ''.join(result)

def part_two(line_gen):
    preds = collections.defaultdict(list)
    for line in line_gen:
        preds[line[-12]].append(line[5])
        if not line[5] in preds:
            preds[line[5]] = list()

    n_workers = 5
    addend = 60
    workers = [0] * n_workers
    working_on = [None] * n_workers
    # Initialize workers
    steps = sorted(k for k, v in preds.items() if not v)
    for i in range(n_workers):
        if not steps:
            break
        working_on[i] = steps.pop(0)
        preds.pop(working_on[i])
        workers[i] = ord(working_on[i]) - ord('A') + addend + 1

    steps = 0
    while True:
        if sum(workers) == 0:
            return steps
        steps += 1
        # Tick
        for i in range(n_workers):
            if working_on[i]:
                workers[i] -= 1
        # Take done ones
        for i in range(n_workers):
            if working_on[i] and workers[i] == 0:
                for k, v in preds.items():
                    if working_on[i] in v:
                        v.remove(working_on[i])
                working_on[i] = None
        # Resupply
        up = sorted(k for k, v in preds.items() if not v)
        for i in range(n_workers):
            if not up:
                break
            if not working_on[i]:
                working_on[i] = up.pop(0)
                preds.pop(working_on[i])
                workers[i] = ord(working_on[i]) - ord('A') + addend + 1


print("A: " + str(part_one(lib.get_input(7))))
print("B: " + str(part_two(lib.get_input(7))))
