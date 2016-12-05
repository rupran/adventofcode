#!/usr/bin/env python3

import re
import lib.common as lib

for line in lib.get_input(1):
    instrs = re.split(", ", line)
    # X, Y -> positive means up/north and right/east
    loc = [0, 0]
    directions = ['north', 'east', 'south', 'west']
    current_direction_idx = 0

    # Location tracking for part B
    visited = set()
    visited.add((0, 0))
    first_twice = None

    # Go the path
    for instr in instrs:
        match = re.match("([LR])([0-9]+)", instr)
        turn_dir = match.group(1)
        steps = int(match.group(2))
        if turn_dir == 'L':
            current_direction_idx = (current_direction_idx - 1) % len(directions)
        else:
            current_direction_idx = (current_direction_idx + 1) % len(directions)

        for _ in range(0, steps):
            # north
            if current_direction_idx == 0:
                loc = [loc[0] + 1, loc[1]]
            # east
            elif current_direction_idx == 1:
                loc = [loc[0], loc[1] + 1]
            # south
            elif current_direction_idx == 2:
                loc = [loc[0] - 1, loc[1]]
            # west
            elif current_direction_idx == 3:
                loc = [loc[0], loc[1] - 1]

            if not first_twice:
                if (loc[0], loc[1]) in visited:
                    first_twice = loc
                else:
                    visited.add((loc[0], loc[1]))


    print("A: " + str(sum(abs(x) for x in loc)))
    print("B: " + str(sum(abs(x) for x in first_twice)))
