#!/usr/bin/env python3

import collections
import lib.common as lib

def is_open_space(pos, fav):
    x, y = pos
    form = (x*x + 3*x + 2*x*y + y + y*y) + fav
    return collections.Counter(bin(form))["1"] % 2 == 0

def do_worklist(line_gen, part_one=True):
    fav = int(next(line_gen))
    seen = set()
    # Form: ((x, y), dist)
    worklist = [((1, 1), 0)]
    seen.add((1, 1))

    while worklist:
        (cur_x, cur_y), cur_dist = worklist.pop(0)

        if part_one and (cur_x, cur_y) == (31, 39):
            return cur_dist
        if not part_one and cur_dist > 50:
            return len(seen)

        seen.add((cur_x, cur_y))

        left = (cur_x - 1, cur_y)
        if cur_x > 0 and is_open_space(left, fav):
            if left not in seen:
                worklist.append((left, cur_dist + 1))

        up = (cur_x, cur_y - 1)
        if cur_y > 0 and is_open_space(up, fav):
            if up not in seen:
                worklist.append((up, cur_dist + 1))

        right = (cur_x + 1, cur_y)
        if is_open_space(right, fav):
            if right not in seen:
                worklist.append((right, cur_dist + 1))

        down = (cur_x, cur_y  + 1)
        if is_open_space(down, fav):
            if down not in seen:
                worklist.append((down, cur_dist + 1))

def part_one(line_gen):
    return do_worklist(line_gen)

def part_two(line_gen):
    return do_worklist(line_gen, part_one=False) 

print("A: " + str(part_one(lib.get_input(13))))
print("B: " + str(part_two(lib.get_input(13))))
