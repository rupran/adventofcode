#!/usr/bin/env python3

import collections
import re

import lib.common as lib

class Instr:

    def __init__(self, target, op, val, condition):
        self.target = target
        op = '+' if op == 'inc' else '-'
        self.instruction = 'registers[\'{}\'] {}= {}'.format(target, op, val)
        self.condition = re.sub(r'^(\w+)', r"registers['\g<0>']", condition)

def simulate(line_gen, second_part=False):
    registers = collections.defaultdict(int)
    max_val = 0

    for line in line_gen:
        match = re.match(r"^(\w+) (inc|dec) ([0-9-]+) if (.+)$", line)
        cur = Instr(*match.groups())

        if eval(cur.condition):
            exec(cur.instruction)

        max_val = max(max_val, registers[cur.target])

    if second_part:
        return max_val
    else:
        return max(registers.values())

def part_one(line_gen):
    return simulate(line_gen)

def part_two(line_gen):
    return simulate(line_gen, True)

print("A: " + str(part_one(lib.get_input(8))))
print("B: " + str(part_two(lib.get_input(8))))
