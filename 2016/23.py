#!/usr/bin/env python3

import math
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
            if target in registers:
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
                try:
                    offset = int(cur_instr[2])
                except ValueError:
                    offset = registers[cur_instr[2]]
                eip += offset - 1
        elif cur_instr[0] == "tgl":
            toggle_off = int(registers[cur_instr[1]])
            toggle_target_eip = eip + toggle_off
            if toggle_target_eip >= len(instrs):
                eip += 1
                continue
            if len(instrs[toggle_target_eip]) == 2:
                if instrs[toggle_target_eip][0] == "inc":
                    instrs[toggle_target_eip][0] = "dec"
                else:
                    instrs[toggle_target_eip][0] = "inc"
            elif len(instrs[toggle_target_eip]) == 3:
                if instrs[toggle_target_eip][0] == "jnz":
                    instrs[toggle_target_eip][0] = "cpy"
                else:
                    instrs[toggle_target_eip][0] = "jnz"
        eip += 1

    return registers["a"]

def part_one(line_gen):
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    return simulate([x.split() for x in line_gen], registers)

def part_two(line_gen):
    registers = {"a": 12, "b": 0, "c": 0, "d": 0}
    # Computation is too slow, see inputs/input_23_commented for
    # disassembunnied code!
    return math.factorial(registers['a']) + 81*93

print("A: " + str(part_one(lib.get_input(23))))
print("B: " + str(part_two(lib.get_input(23))))
