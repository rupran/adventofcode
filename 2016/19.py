#!/usr/bin/env python3

import collections
import math
import lib.common as lib

def part_one(line_gen):
    n = int(next(line_gen))
    m = math.floor(math.log(n, 2))
    l = n - 2**m
    return 2*l + 1

def part_two(line_gen):
    n = int(next(line_gen))
    first_half = collections.deque()
    second_half = collections.deque()
    for i in range(1, math.ceil(n/2) + 1):
        first_half.append(i)
    for i in range(math.ceil(n/2) + 1, n + 1):
        second_half.append(i)

    while n > 1:
        if n % 2 == 0:
            # there is an exact opposite, remove it (first in second half)
            second_half.popleft()
        else:
            # if there isn't, pick smaller number - which is last in first_half
            first_half.pop()
        # Advance in ring, by:
        # a) moving oldest member from first to second (advance current elf)
        second_half.append(first_half.popleft())
        # b) moving oldest member from second to first (advance opposite 'pointer')
        first_half.append(second_half.popleft())
        n -= 1

    return first_half.popleft()

print("A: " + str(part_one(lib.get_input(19))))
print("B: " + str(part_two(lib.get_input(19))))
