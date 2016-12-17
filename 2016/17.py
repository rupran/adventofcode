#!/usr/bin/env python3

import collections
import hashlib
import lib.common as lib

def get_hash(cur):
    return hashlib.md5(cur.encode()).hexdigest()

def find_paths(inp):
    op_map = {0: (0, -1, "U"), 1: (0, 1, "D"), 2: (-1, 0, "L"), 3: (1, 0, "R")}

    start = (0, 0, "")
    solutions = set()

    worklist = collections.deque()
    worklist.append(start)
    while worklist:
        cur_x, cur_y, cur_path = worklist.popleft()
        if (cur_x, cur_y) == (3, 3):
            solutions.add(cur_path)
            continue

        cur_hash = get_hash(inp + cur_path)[:4]
        for op in op_map:
            if cur_hash[op] in "bcdef":
                d_x, d_y, d_path = op_map[op]
                if cur_x + d_x >= 0 and cur_x + d_x < 4 and cur_y + d_y >= 0 and cur_y + d_y < 4:
                    worklist.append((cur_x + d_x, cur_y + d_y, cur_path + d_path))

    return solutions


def part_one(line_gen):
    return min(find_paths(next(line_gen)), key=lambda s: len(s))

def part_two(line_gen):
    return len(max(find_paths(next(line_gen)), key=lambda s: len(s)))

print("A: " + str(part_one(lib.get_input(17))))
print("B: " + str(part_two(lib.get_input(17))))
