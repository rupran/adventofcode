#!/usr/bin/env python3

import itertools
import lib.common as lib

def is_good_state(state):
    # Not underground or over the top
    if state[0] == 0 or state[0] == 5:
        return False
    # No chip with _other_ RTG on same floor
    for cur_chip_idx in range(2, len(state), 2):
        if state[cur_chip_idx] == state[cur_chip_idx-1]:
            continue
        for j in range(1, len(state), 2):
            if state[cur_chip_idx] == state[j]:
                return False
    return True

def get_new_state(old_state, to_update, delta):
    new_state = list(old_state)
    new_state[0] += delta
    for idx in to_update:
        new_state[idx] += delta
    return tuple(new_state)

def make_interchangeable_tuple(state):
    perm_state = [(state[0],)]
    for i in range(1, len(state), 2):
        perm_state.append((state[i], state[i+1]))
    return tuple(sorted(perm_state))

def update_worklist(worklist, old_state, to_update, delta, seen, cur_dist):
    next_state = get_new_state(old_state, to_update, delta)
    perm_tup = make_interchangeable_tuple(next_state)
    if perm_tup not in seen and is_good_state(next_state):
        seen.add(perm_tup)
        worklist.append((next_state, cur_dist + 1))

def solve(in_tuple):
    target = tuple([4] * len(in_tuple))

    seen = set()
    seen.add(make_interchangeable_tuple(in_tuple))

    start = (in_tuple, 0)
    worklist = [start]
    while worklist:
        cur, dist = worklist.pop(0)

        if cur == target:
            return dist

        same_floor_idxs = [x for x in range(1, len(cur)) if cur[x] == cur[0]]
        # try moving two things up one floor
        for comb in itertools.combinations(same_floor_idxs, 2):
            update_worklist(worklist, cur, comb, 1, seen, dist)

        # try moving one thing up one floor
        for item in same_floor_idxs:
            update_worklist(worklist, cur, [item], 1, seen, dist)

        # try moving one thing down one floor
        for item in same_floor_idxs:
            update_worklist(worklist, cur, [item], -1, seen, dist)

        # try moving things down two floors
        for comb in itertools.combinations(same_floor_idxs, 2):
            update_worklist(worklist, cur, comb, -1, seen, dist)

def part_one(line_gen):
    # Format: (elevator, curium_gen, curium_chip, plu_gen, plu_chip, ruth_gen,
    # ruth_chip, stron_gen, stron_chip, thul_gen, thul_chip)
    return solve((1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 3))

def part_two(line_gen):
    # Part one plus two generator/chip pairs on level 1
    return solve((1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 3, 1, 1, 1, 1))

print("A: " + str(part_one(lib.get_input(11))))
print("B: " + str(part_two(lib.get_input(11))))
