#!/usr/bin/env python3

import collections
import re
import lib.common as lib

Disc = collections.namedtuple('Disc', 'start, mod')

def simulate(discs):
    pos = [0] # Placeholder, discs are numbered from 1
    for disc in sorted(discs.keys()):
        pos.append(discs[disc].start)

    time = 0
    while True:
        for i in range(1, len(pos)):
            pos[i] = (discs[i].start + time + i) % discs[i].mod

        if sum(pos) == 0:
            return time
        time += 1

def init_discs(line_gen, second_part=False):
    # disc no -> (start, mod)
    discs = {}
    for line in line_gen:
        match = re.match(r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).",
                         line)
        discs[int(match.group(1))] = Disc(int(match.group(3)), int(match.group(2)))

    if second_part:
        discs[max(discs.keys()) + 1] = Disc(0, 11)

    return discs

def part_one(line_gen):
    return simulate(init_discs(line_gen))

def part_two(line_gen):
    return simulate(init_discs(line_gen, second_part=True))

print("A: " + str(part_one(lib.get_input(15))))
print("B: " + str(part_two(lib.get_input(15))))
