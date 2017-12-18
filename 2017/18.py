#!/usr/bin/env python3

from collections import defaultdict
from queue import Queue

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
    elif instr == 'add':
        registers[op1] += src
    elif instr == 'mul':
        registers[op1] *= src
    elif instr == 'mod':
        registers[op1] %= src
    else:
        print('ERROR')

send_count = 0

def run_program(code, registers, second_part=False, pid=0, out_qs=None):
    global send_count
    last_snd = -1
    other = 1 - pid
    if second_part:
        registers['p'] = pid
    while registers['ip'] < len(code):
        cur = code[registers['ip']]
        if cur[0] == 'snd':
            if not second_part:
                last_snd = registers[cur[1]]
            else:
                val = get_value(cur[1], registers)
                out_qs[pid].put(val)
                if pid == 1:
                    send_count += 1
        elif cur[0] == 'rcv':
            if not second_part:
                src = registers[cur[1]]
                if src != 0:
                    return last_snd
            else:
                if out_qs[other].empty():
                    return True
                else:
                    val = out_qs[other].get()
                    registers[cur[1]] = val
        elif cur[0] == 'jgz':
            val = get_value(cur[1], registers)
            offset = get_value(cur[2], registers)
            if val > 0:
                registers['ip'] += offset
                continue
        else:
            operate(*cur, registers)
        registers['ip'] += 1

def part_one(line_gen):
    return run_program([x.split() for x in line_gen], defaultdict(int))

def part_two(line_gen):
    prog = [x.split() for x in line_gen]
    queues = [Queue(), Queue()]
    regs_1 = defaultdict(int)
    regs_2 = defaultdict(int)

    while True:
        blocked_1 = run_program(prog, regs_1, True, 0, queues)
        blocked_2 = run_program(prog, regs_2, True, 1, queues)
        if blocked_1 and blocked_2 and all(x.empty() for x in queues):
            return send_count

print("A: " + str(part_one(lib.get_input(18))))
print("B: " + str(part_two(lib.get_input(18))))
