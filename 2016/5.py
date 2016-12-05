#!/usr/bin/python3

import hashlib
import re
import lib.common as lib

def calc_hash(in_value):
    return hashlib.md5(in_value.encode()).hexdigest()

def part_one(line):
    index = 0
    password = ""
    while len(password) < 8:
        digest = calc_hash(line + str(index))
        if digest.startswith("00000"):
            password += digest[5]

        index += 1

    return password

def part_two(line):
    password = [None] * 8
    index = 0

    while not all(password):
        digest = calc_hash(line + str(index))
        if digest.startswith("00000"):
            insert = digest[5]
            val = digest[6]

            if insert < '0' or insert >= '8':
                index += 1
                continue

            insert = int(insert)
            if password[insert] is None:
                password[insert] = val

        index += 1

    return "".join(password)

for input_line in lib.get_input(5):
    print("A: " + part_one(input_line))
    print("B: " + part_two(input_line))
