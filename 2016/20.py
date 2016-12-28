#!/usr/bin/env python3

import lib.common as lib

def merge_ranges(line_gen):
    ranges = sorted((int(x[0]), int(x[1])) for x in
                    [l.split("-") for l in line_gen])

    merged_ranges = [ranges[0]]
    for cur_ind in range(1, len(ranges)):
        start_a, end_a = merged_ranges[-1]
        start_b, end_b = ranges[cur_ind]
        # Merge overlapping and adjacent, only keep merged pair
        # overlapping:  end_a >= start_b
        # adjacent: end_a + 1 == start_b
        if end_a + 1 >= start_b:
            merged_range = (start_a, max(end_a, end_b))
            merged_ranges.pop()
            merged_ranges.append(merged_range)
        # No merge possible, add this pair
        else:
            merged_ranges.append(ranges[cur_ind])

    return merged_ranges

def part_one(line_gen):
    merged_ranges = merge_ranges(line_gen)
    return merged_ranges[0][1] + 1

def part_two(line_gen, max_ip):
    merged_ranges = merge_ranges(line_gen)
    # Add fake range which blocks ports > max_ip
    merged_ranges.append((max_ip + 1, None))

    allowed = 0
    for cur_ind in range(len(merged_ranges) - 1):
        allowed += merged_ranges[cur_ind + 1][0] - merged_ranges[cur_ind][1] - 1

    return allowed

print("A: " + str(part_one(lib.get_input(20))))
print("B: " + str(part_two(lib.get_input(20), 4294967295)))
