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

sum_of_valid_ids = 0

for line in lib.get_input(4):
    # Get characters, sector id and checksum from line
    match_id = re.match("^([a-z-]+)([0-9]+)\[([a-z]+)\]$", line)
    sector_id = int(match_id.group(2))
    checksum = match_id.group(3)
    chars_in_name = [x for x in match_id.group(1) if x != '-']

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

    # Part B: decrypt line by shifting keys
    decrypted = decrypt(match_id.group(1), sector_id)
    if "northpole object storage" in decrypted:
        storage_id = sector_id

print("A: " + str(sum_of_valid_ids))
print("B: " + str(storage_id))
