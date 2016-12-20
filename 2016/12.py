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
        elif cur_instr[0] == "add":
            src = cur_instr[1]
            target = cur_instr[2]
            registers[target] += registers[src]
        eip += 1

    return registers["a"]

def fix_jumps(code, cur_start, cur_end):
    #print("fix from %d to %d" % (cur_start, cur_end))
    # Fix later jumps which go back into or before this block
    cur_ip = cur_end
    for instr in code[cur_end:]:
        if instr[0] == "jnz" and int(instr[2]) + cur_ip <= cur_start:
            # ... by increasing relative offset by one
            #print("fix after")
            code[cur_ip][2] = str(int(instr[2]) + 1)
        cur_ip += 1
    # Fix jumps in earlier code which go beyond this block
    cur_ip = 0
    for instr in code[:cur_start]:
        if instr[0] == "jnz" and int(instr[2]) + cur_ip >= cur_end:
            # ... by decreasing relative offset by one
            #print("fix before")
            code[cur_ip][2] = str(int(instr[2]) - 1)
        cur_ip += 1

def optimize(code):
    ip = 0
    bb_ranges = []
    jmp_targets = [0]
    while ip < len(code):
        instr = code[ip]
        if instr[0] == "jnz":
            tgt = int(instr[2]) + ip
            jmp_targets.append(tgt)
            jmp_targets.append(ip + 1)
        ip += 1

    jmp_targets.append(len(code))
    jmp_targets = sorted(set(jmp_targets))

    bb_ranges = [(jmp_targets[i], jmp_targets[i+1]) for i in range(len(jmp_targets) - 1)]
    bbs = [code[rng[0]:rng[1]] for rng in bb_ranges]

    new_bbs = []
    for i, bb in enumerate(bbs):
        cur_start = bb_ranges[i][0]
        cur_end = bb_ranges[i][1]
        # Optimize inc x, dec y, jnz y -2 to add y x, cpy 0 y
        # Hardcoded offsets because jnz -2 always makes it a contained block
        if bb[0][0] == "inc":
            inc_tgt = bb[0][1]
            if len(bb) > 1 and bb[1][0] == "dec":
                dec_tgt = bb[1][1]
                if len(bb) > 2 and bb[2][0] == "jnz" and bb[2][1] == dec_tgt and bb[2][2] == "-2":
                    new_bbs.append([["add", dec_tgt, inc_tgt],
                                    ["cpy", "0", dec_tgt]])

                    fix_jumps(code, cur_start, cur_end)
                    continue

#        fixed_bb = []
#        for instr_idx in range(len(bb)):
#            if bb[instr_idx][0] == "cpy" and bb[instr_idx][1] == "0":
#                tgt = bb[instr_idx][2]
#                if instr_idx + 1 < len(bb):
#                    if bb[instr_idx + 1][0] == "cpy" and bb[instr_idx + 1][2] == tgt:
#                        print("zero copy: " + str(bb[instr_idx + 1]))
#                         # Doesn't work properly yet, own block would need fixing
#                        fix_jumps(code, cur_start, cur_end)
#                        continue
#
#            fixed_bb.append(bb[instr_idx])

#        bb = fixed_bb
        new_bbs.append(bb)

    opt_code = [item for bb in new_bbs for item in bb]
#    if opt_code == code:
#        return opt_code
#    else:
#        print("rec")
    return opt_code

def part_one(line_gen):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    code = [x.split() for x in line_gen]
    code = optimize(code)
    with open("inputs/input_12.opt", "w") as outfile:
        for instr in code:
            outfile.write(" ".join(instr) + "\n")

    return simulate(code, registers)

def part_two(line_gen):
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    code = [x.split() for x in line_gen]
    code = optimize(code)
    return simulate(code, registers)

print("A: " + str(part_one(lib.get_input(12))))
print("B: " + str(part_two(lib.get_input(12))))
