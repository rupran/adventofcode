#!/usr/bin/env python3

import lib.common as lib
import re

def calc_checksum(state, disk_len):
    while len(state) < disk_len:
        b = "".join('1' if x == '0' else '0' for x in reversed(state))
        state = "{}0{}".format(state, b)

    checksum = state[:disk_len]
    while len(checksum) % 2 != 1:
        match = re.findall(r"(.)(.)", checksum)
        checksum = "".join('1' if m[0] == m[1] else '0' for m in match)

    return checksum

def part_one(line_gen):
    return calc_checksum(next(line_gen), 272)

def part_two(line_gen):
    return calc_checksum(next(line_gen), 35651584)

print("A: " + str(part_one(lib.get_input(16))))
print("B: " + str(part_two(lib.get_input(16))))
