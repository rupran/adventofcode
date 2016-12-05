#!/usr/bin/env python3

import hashlib
import re
import lib.common as lib

def calc_hash(in_value):
    return hashlib.md5(in_value.encode()).hexdigest()

def part_one(line_gen):
    line = next(line_gen)
    index = 0
    password = ""
    while len(password) < 8:
        digest = calc_hash(line + str(index))
        if digest.startswith("00000"):
            password += digest[5]

        index += 1

    return password

def part_two(line_gen):
    line = next(line_gen)
    password = [None] * 8
    index = -1

    while not all(password):
        index += 1
        digest = calc_hash(line + str(index))
        if digest.startswith("00000"):
            insert = digest[5]
            val = digest[6]

            if insert < '0' or insert >= '8':
                continue

            insert = int(insert)
            if password[insert] is None:
                password[insert] = val

    return "".join(password)

print("A: " + str(part_one(lib.get_input(5))))
print("B: " + str(part_two(lib.get_input(5))))
