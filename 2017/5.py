#!/usr/bin/env python3

import lib.common as lib

def read_program(line_gen):
    return [int(x) for x in line_gen]

def simulate(line_gen, part_two=False):
    program = read_program(line_gen)
    pc = 0
    count = 0
    while pc < len(program):
        count += 1
        old_pc = pc
        pc += program[pc]
        if part_two and program[old_pc] >= 3:
            program[old_pc] -= 1
        else:
            program[old_pc] += 1

    return count

print("A: " + str(simulate(lib.get_input(5))))
print("B: " + str(simulate(lib.get_input(5), True)))
