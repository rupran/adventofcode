#!/usr/bin/env python3

import collections
import re

import lib.common as lib

def part_one(line_gen):
    particles = []
    velocs = {}
    i = 0
    for line in line_gen:
        m = re.match(r'position=<\s*([-]?\d+),\s*([-]?\d+)> velocity=<\s*([-]?\d+),\s*([-]?\d+)>', line)
        x, y, vx, vy = (int(x) for x in m.groups())
        particles.append([x, y])
        velocs[i] = (vx, vy)
        i += 1

    steps = 0
    while True:
        # check for letters
        max_x = max(x[0] for x in particles)
        max_y = max(x[1] for x in particles)
        min_x = min(x[0] for x in particles)
        min_y = min(x[1] for x in particles)
        if max_x - min_x < 100 and max_y - min_y == 9:
            printable = [[' ' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
            for p in particles:
                printable[p[1] - min_y][p[0] - min_x] = '#'
            for line in printable:
                print(''.join(line))
            print(steps)
            break
        # update positions
        for i in range(len(particles)):
            particles[i][0] += velocs[i][0]
            particles[i][1] += velocs[i][1]
        steps += 1

def part_two(line_gen):
    # line = next(line_gen) # one line input
    # for line in line_gen: # multi line input
    pass

print("A: " + str(part_one(lib.get_input(10))))
print("B: " + str(part_two(lib.get_input(10))))
