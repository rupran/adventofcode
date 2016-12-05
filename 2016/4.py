#!/usr/bin/env python3

import re
import collections
import lib.common as lib

def decrypt(line, factor):
    res = ""
    for char in line:
        if char == "-":
            char_after = " "
        else:
            index_before = ord(char) - ord('a')
            index_after = (index_before + factor) % 26
            char_after = chr(ord('a') + index_after)
        res += char_after

    return res

def get_parts(line):
    # Get characters, sector id and checksum from line
    match_id = re.match("^([a-z-]+)([0-9]+)\[([a-z]+)\]$", line)

    name = match_id.group(1)
    sector_id = int(match_id.group(2))
    checksum = match_id.group(3)

    return name, sector_id, checksum

def part_one(line_gen):
    sum_of_valid_ids = 0

    for line in line_gen:
        name, sector_id, checksum = get_parts(line)
        chars_in_name = [x for x in name if not x == '-']

        # Count characters
        counts = collections.defaultdict(int)
        for letter in chars_in_name:
            counts[letter] += 1

        # Sort by number of occurrences decreasing, then by letter increasing
        reverse_key = lambda a: (-a[1], a[0])
        sorted_counts = sorted(counts.items(), key=reverse_key)

        # Compare five most common characters to checksum and add to sum
        five_most_common = "".join(x[0] for x in sorted_counts[:5])
        if five_most_common == checksum:
            sum_of_valid_ids += sector_id

    return sum_of_valid_ids

def part_two(line_gen):
    # Part B: decrypt line by shifting keys
    for line in line_gen:
        name, sector_id, _ = get_parts(line)
        decrypted = decrypt(name, sector_id)
        if "northpole object storage" in decrypted:
            return sector_id

print("A: " + str(part_one(lib.get_input(4))))
print("B: " + str(part_two(lib.get_input(4))))
