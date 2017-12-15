#!/usr/bin/env python3

import re

import lib.common as lib

class RNG:
    def __init__(self, factor, initial, modulus=None):
        self.factor = factor
        self.value = initial
        self.modulus = modulus

    def next(self):
        while True:
            self.value = (self.value * self.factor) % 2147483647
            if not self.modulus or self.value % self.modulus == 0:
                break
        return self.value

def run_generators(rng1, rng2, limit):
    count = 0
    for _ in range(limit):
        if rng1.next() & 0xffff == rng2.next() & 0xffff:
            count += 1
    return count

def part_one(line_gen):
    init1 = int(re.match(r'.* (\d+)$', next(line_gen)).group(1))
    init2 = int(re.match(r'.* (\d+)$', next(line_gen)).group(1))
    return run_generators(RNG(16807, init1), RNG(48271, init2), 40000000)

def part_two(line_gen):
    init1 = int(re.match(r'.* (\d+)$', next(line_gen)).group(1))
    init2 = int(re.match(r'.* (\d+)$', next(line_gen)).group(1))
    return run_generators(RNG(16807, init1, 4), RNG(48271, init2, 8), 5000000)

print("A: " + str(part_one(lib.get_input(15))))
print("B: " + str(part_two(lib.get_input(15))))
