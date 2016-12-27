#!/usr/bin/env python3

import lib.common as lib

def simulate(instrs, registers):
    eip = 0
    out_values = []
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
        elif cur_instr[0] == "out":
            out_value = registers[cur_instr[1]]
            if len(out_values) == 0:
                out_values.append(out_value)
            else:
                if out_values[-1] == out_value:
                    return False
                out_values.append(out_value)
            if len(out_values) > 20:
                return True
        eip += 1 

def part_one(line_gen):
    a = 1
    code = [x.split() for x in line_gen]
    while True:
        registers = {"a": a, "b": 0, "c": 0, "d": 0}
        success = simulate(code, registers)
        if success:
            break
        a += 1
    return a

def part_two(line_gen):
    return "There is no part two, we're done! :-)"

print("A: " + str(part_one(lib.get_input(25))))
print("B: " + str(part_two(lib.get_input(25))))
