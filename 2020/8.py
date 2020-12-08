#!/usr/bin/env python3

import copy
import lib.common as lib

def simulate(instructions):
    ip = 0
    acc = 0
    visited = set()
    while ip < len(instructions):
        if ip in visited:
            return acc, True
        visited.add(ip)
        cur_instr, val = instructions[ip]
        if cur_instr == 'acc':
            acc += val
        elif cur_instr == 'jmp':
            ip += val
            continue
        elif cur_instr == 'nop':
            pass
        ip += 1
    return acc, False

def parse_instructions(line_gen):
    instructions = []
    for line in line_gen:
        instr, val = line.split()
        instructions.append([instr, int(val)])
    return instructions

def part_one(line_gen):
    return simulate(parse_instructions(line_gen))[0]

def part_two(line_gen):
    initial_instructions = parse_instructions(line_gen)
    for idx in range(len(initial_instructions)):
        current_instructions = copy.deepcopy(initial_instructions)
        if initial_instructions[idx][0] == 'jmp':
            current_instructions[idx][0] = 'nop'
        elif initial_instructions[idx][0] == 'nop':
            current_instructions[idx][0] = 'jmp'
        acc, loop = simulate(current_instructions)
        if not loop:
            return acc

print("A: " + str(part_one(lib.get_input(8))))
print("B: " + str(part_two(lib.get_input(8))))
