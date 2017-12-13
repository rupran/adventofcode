#!/usr/bin/env python3

import re

import lib.common as lib

def simulate(layers, delay=0):
    pos = {depth: 0 for depth in layers.keys()}
    direction = {depth: 1 for depth in layers.keys()}
    packet = -1 - delay
    severity = 0
    caught = False

    while packet <= max(layers.keys()):
        packet += 1
        if packet in pos:
            if pos[packet] == 0:
                severity += packet * layers[packet]
                caught = True
                if delay > 0:
                    break
        for key in pos.keys():
            pos[key] = pos[key] + direction[key]
            if pos[key] == layers[key] - 1:
                direction[key] = -1
            elif pos[key] == 0:
                direction[key] = 1

    return (severity, caught)

# Actually running the simulation is waaay too slow for the second part, so we
# need something more clever than that. We know that after 2*(length-1) ticks,
# the scanner is back at position 0. We also know where the packet is after N
# ticks (which is delay + depth) and if the scanner at that depth is at 0 as
# well, we are caught.
def fast_check(layers, delay=0):
    severity = 0
    caught = False
    for depth, length in layers.items():
        if (delay + depth) % (2*(length-1)) == 0:
            severity += depth * length
            caught = True
            # Stop analysis if we're in part two
            if delay > 0:
                break
    return (severity, caught)

def read(line_gen):
    layers = {}
    for line in line_gen:
        depth, length = (int(x) for x in re.match(r'(\d+): (\d+)$', line).groups())
        layers[depth] = length
    return layers

def part_one(line_gen):
    return simulate(read(line_gen))[0]

def part_two(line_gen):
    layers = read(line_gen)
    delay = 0
    while True:
        if not fast_check(layers, delay)[1]:
            break
        delay += 1
    return delay

print("A: " + str(part_one(lib.get_input(13))))
print("B: " + str(part_two(lib.get_input(13))))
