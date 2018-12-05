#!/usr/bin/env python3

import lib.common as lib

def calc_len(line):
    # Fast: only append if it doesn't get reduced away
    stack = []
    for c in line:
        if not len(stack):
            stack.append(c)
        else:
            prev = stack[-1]
            if prev != c and c.upper() == prev.upper():
                stack.pop()
            else:
                stack.append(c)
    return len(stack)

    # Slow: creating new strings
    change = True
    while change:
        change = False
        new = []
        idx = 0
        while idx < len(line):
            c = line[idx]
            if idx == len(line) - 1:
                new.append(c)
                break
            next_c = line[idx + 1]
            if c.isupper() and next_c.islower() and c.lower() == next_c.lower():
                idx += 2
                change = True
            elif c.islower() and next_c.isupper() and c.lower() == next_c.lower():
                idx += 2
                change = True
            else:
                new.append(c)
                idx += 1
        line = new[:]
    return len(line)

def part_one(line_gen):
    return calc_len(list(next(line_gen)))

def part_two(line_gen):
    inp = list(next(line_gen))
    best = len(inp)
    chars = set(x.lower() for x in inp)
    for char in chars:
        def preprocess(line):
            return [x for x in line if not x.lower() == char]
        best = min(best, calc_len(preprocess(inp)))
    return best

print("A: " + str(part_one(lib.get_input(5))))
print("B: " + str(part_two(lib.get_input(5))))
