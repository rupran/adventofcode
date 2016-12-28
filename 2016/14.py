#!/usr/bin/env python3

import hashlib
import re
import lib.common as lib

def calc_hash(in_value, stretched):
    ret_hash = hashlib.md5(in_value.encode()).hexdigest()
    if not stretched:
        return ret_hash
    else:
        for _ in range(2016):
            ret_hash = hashlib.md5(ret_hash.encode()).hexdigest()
        return ret_hash

def get_hash(cache, data, stretched=False):
    if data not in cache:
        cache[data] = calc_hash(data, stretched)
    return cache[data]

def find_index_64(salt, stretched=False):
    index = 0
    cache = {}
    keys = []
    while True:
        cur_val = salt + str(index)
        cur_hash = get_hash(cache, cur_val, stretched)
        match = re.search(r"(.)\1{2}", cur_hash)
        if match:
            tripled_char = match.group(1)
            quint_regex = re.compile(r"%s{5}" % tripled_char)
            for j in range(1, 1001):
                fwd_val = salt + str(index + j)
                fwd_hash = get_hash(cache, fwd_val, stretched)
                match = quint_regex.search(fwd_hash)
                if match:
                    keys.append(cur_val)

        if len(keys) == 64:
            return index
        index += 1

def part_one(line_gen):
    salt = next(line_gen)
    return find_index_64(salt)

def part_two(line_gen):
    salt = next(line_gen)
    return find_index_64(salt, stretched=True)

print("A: " + str(part_one(lib.get_input(14))))
print("B: " + str(part_two(lib.get_input(14))))
