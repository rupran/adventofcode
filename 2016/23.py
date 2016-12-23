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
        elif cur_instr[0] == "mul":
            registers[cur_instr[3]] = registers[cur_instr[2]] * registers[cur_instr[1]]
        eip += 1

    return registers["a"]

def optimize(code):
    new_code = []
    i = 0
    while i < len(code):
        new_code.append(code[i])
        # Optimize:
        # "cpy y z, inc x, dec z, jnz z -2, dec w, jnz w -5" becomes
        # "mul w y x, cpy 0 z, cpy 0 w + 2x nop"
        if code[i][0] != "cpy":
            i += 1
            continue
        y = code[i][1]
        if i + 1 >= len(code) or code[i+1][0] != "inc":
            i += 1
            continue
        x = code[i+1][1]
        if i + 2 >= len(code) or code[i+2][0] != "dec":
            i += 1
            continue
        z = code[i+2][1]
        if i + 3 >= len(code) or code[i+3][0] != "jnz" or code[i+3][1] != z or code[i+3][2] != "-2":
            i += 1
            continue
        if i + 4 >= len(code) or code[i+4][0] != "dec":
            i += 1
            continue
        w = code[i+4][1]
        if i + 5 >= len(code) or code[i+5][0] != "jnz" or code[i+5][1] != w or code[i+5][2] != "-5":
            i += 1
            continue
        # All checks passend, generate optimized code for multiplication
        new_code.append(["mul", w, y, x])
        new_code.append(["cpy", "0", z])
        new_code.append(["cpy", "0", w])
        new_code.append(["cpy", "0", w])
        new_code.append(["cpy", "0", w])
        i += 6  # Skip replaced instructions

    return new_code

def part_one(line_gen):
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    code = optimize([x.split() for x in line_gen])
    return simulate(code, registers)

def part_two(line_gen):
    registers = {"a": 12, "b": 0, "c": 0, "d": 0}
    code = optimize([x.split() for x in line_gen])
    return simulate(code, registers)
    # Non-optimized computation is too slow, see inputs/input_23_commented for
    # disassembunnied code -> Solution: a = a! + 81*93
    #return math.factorial(registers['a']) + 81*93

print("A: " + str(part_one(lib.get_input(23))))
print("B: " + str(part_two(lib.get_input(23))))
