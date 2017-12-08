#!/usr/bin/env python3

import re

import lib.common as lib

class Instr:

    def __init__(self, target, op, val, condition):
        self.target = target
        if op == 'inc':
            op = '+'
        else:
            op = '-'
        self.instruction = 'registers[\'{}\'] {}= {}'.format(target, op, val)
        self.cond_target = re.match(r'^(\w+)', condition).group(0)
        self.condition = re.sub(r'^(\w+)', 'registers[\'\g<0>\']', condition)

def simulate(line_gen, part_two=False):
    program = []
    registers = {}
    # line = next(line_gen) # one line input
    for line in line_gen:
        match = re.match("^(\w+) (inc|dec) ([0-9-]+) if (.+)$", line)
        if match:
            program.append(Instr(*match.groups()))

    ip = 0
    max_val = 0
    while ip < len(program):
        cur = program[ip]
        ip += 1

        if not cur.target in registers:
            registers[cur.target] = 0

        if not cur.cond_target in registers:
            registers[cur.cond_target] = 0

        if eval(cur.condition):
            exec(cur.instruction)

        max_val = max(max_val, registers[cur.target])

    if part_two:
        return max_val
    else:
        return max(registers.values())


def part_one(line_gen):
    return simulate(line_gen)

def part_two(line_gen):
    return simulate(line_gen, True)

print("A: " + str(part_one(lib.get_input(8))))
print("B: " + str(part_two(lib.get_input(8))))
