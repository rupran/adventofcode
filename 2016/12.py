#!/usr/bin/env python3

import lib.common as lib

def simulate(instrs, registers):
    eip = 0
    while eip < len(instrs):
        cur_instr = instrs[eip]
        if cur_instr[0] == "cpy":
            target = cur_instr[2]
            try:
                src = int(cur_instr[1])
            except ValueError:
                src = registers[cur_instr[1]]
            registers[target] = src
        elif cur_instr[0] == "inc":
            registers[cur_instr[1]] += 1
        elif cur_instr[0] == "dec":
            registers[cur_instr[1]] -= 1
        elif cur_instr[0] == "jnz":
            try:
                src = int(cur_instr[1])
            except ValueError:
                src = registers[cur_instr[1]]
            if src != 0:
                eip += int(cur_instr[2]) - 1
        eip += 1

    return registers["a"]

def part_one(line_gen):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    return simulate([x.split() for x in line_gen], registers)

def part_two(line_gen):
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    return simulate([x.split() for x in line_gen], registers)

print("A: " + str(part_one(lib.get_input(12))))
print("B: " + str(part_two(lib.get_input(12))))
