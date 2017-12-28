#!/usr/bin/env python3

import collections

import lib.common as lib

def get_value(op, registers):
    if op.isalpha():
        return registers[op]
    else:
        return int(op)

def operate(instr, op1, op2, registers):
    src = get_value(op2, registers)
    if instr == 'set':
        registers[op1] = src
    elif instr == 'sub':
        registers[op1] -= src
    elif instr == 'mul':
        registers['mul_count'] += 1
        registers[op1] *= src
    else:
        print('ERROR ' + instr)

def part_one(line_gen):
    registers = collections.defaultdict(int)
    prog = []
    for line in line_gen:
        prog.append(tuple(line.split()))

    while registers['ip'] < len(prog):
        cur = prog[registers['ip']]
        if cur[0] == 'jnz':
            val = get_value(cur[1], registers)
            offset = get_value(cur[2], registers)
            if val != 0:
                registers['ip'] += offset
                continue
        else:
            operate(*cur, registers)
        registers['ip'] += 1

    return registers['mul_count']

def part_two():
    b = 109300
    c = 126300
    h = 0
    while b <= c:
        for d in range(2, b):
            if b % d == 0:
                h += 1
                break
        b += 17

    return h

print("A: " + str(part_one(lib.get_input(23))))
print("B: " + str(part_two()))
