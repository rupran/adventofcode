#!/usr/bin/env python3

import math
import lib.common as lib

def part_one(line_gen):
    start = int(next(line_gen))
    current = start
    buses = [int(num) for num in next(line_gen).split(',') if num != 'x']
    while True:
        current += 1
        for bus in buses:
            if current % bus == 0:
                return bus * (current - start)

def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    c, d, e = extended_euclid(b, a % b)
    return (c, e, d - (a // b) * e)

def part_two(line_gen):
    _ = next(line_gen)
    inp = next(line_gen)
    current_mod_reduction = 0
    moduls = []
    for c in inp.split(','):
        if c != 'x':
            moduls.append((int(c) - current_mod_reduction, int(c)))
        current_mod_reduction += 1
        
    res = 0
    M = math.prod(m[1] for m in moduls)
    for a, m in moduls:
        m_cur = M // m
        _, _, s = extended_euclid(m, m_cur)
        e_cur = m_cur * s
        res +=  a * e_cur
    return res % M

print("A: " + str(part_one(lib.get_input(13))))
print("B: " + str(part_two(lib.get_input(13))))
