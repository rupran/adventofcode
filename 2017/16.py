#!/usr/bin/env python3

import re

import lib.common as lib

def swap(lst, idx1, idx2):
    tmp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = tmp

def dance(line, steps):
    rawops = line.split(',')
    ops = []
    for op in rawops:
        if op[0] == 's':
            ops.append(('s', int(op[1:])))
        elif op[0] == 'x':
            first, second = (int(x) for x in re.match(r'(\d+)/(\d+)', op[1:]).groups())
            ops.append(('x', first, second))
        elif op[0] == 'p':
            ops.append(op)
    row = [chr(x) for x in range(ord('a'), ord('p')+1)]
    seen = []
    for i in range(steps):
        if ''.join(row) in seen:
            return seen[steps % i]
        seen.append(''.join(row))

        for op in ops:
            if op[0] == 's':
                shift = op[1]
                row = row[-shift:] + row[:-shift]
            elif op[0] == 'x':
                swap(row, op[1], op[2])
            elif op[0] == 'p':
                swap(row, row.index(op[1]), row.index(op[3]))

    return ''.join(row)

def part_one(line_gen):
    return dance(next(line_gen), 1)

def part_two(line_gen):
    return dance(next(line_gen), 1000000000)

print("A: " + str(part_one(lib.get_input(16))))
print("B: " + str(part_two(lib.get_input(16))))
