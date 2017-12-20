#!/usr/bin/env python3

import re

import lib.common as lib

def manhattan(particle):
    return sum(abs(x) for x in particle)

def simulate(line_gen, second_part=False):
    particles = []
    vels = []
    accels = []
    destroyed = set()
    for line in line_gen: # multi line input
        cur_p, cur_v, cur_a = re.match(r'p=<(.*)>, v=<(.*)>, a=<(.*)>$', line).groups()
        particles.append(list(int(x) for x in cur_p.split(',')))
        vels.append(list(int(x) for x in cur_v.split(',')))
        accels.append(list(int(x) for x in cur_a.split(',')))

    min_idx = -1
    for _ in range(1000):
        for idx, p in enumerate(particles):
            if idx in destroyed:
                continue
            for i, k in enumerate(accels[idx]):
                vels[idx][i] += k
            for i, k in enumerate(vels[idx]):
                p[i] += k

        if not second_part:
            min_idx = min((manhattan(p), idx) for idx, p in enumerate(particles))
        else:
            for idx, p in enumerate(particles):
                if idx in destroyed:
                    continue
                for idx_2 in range(idx + 1, len(particles)):
                    if p == particles[idx_2]:
                        destroyed.add(idx)
                        destroyed.add(idx_2)

    if second_part:
        return len(particles) - len(destroyed)
    else:
        return min_idx[1]

def part_one(line_gen):
    return simulate(line_gen)

def part_two(line_gen):
    return simulate(line_gen, True)

print("A: " + str(part_one(lib.get_input(20))))
print("B: " + str(part_two(lib.get_input(20))))
