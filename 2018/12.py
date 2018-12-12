#!/usr/bin/env python3

import collections

import lib.common as lib

def transform(state, rules):
    new_state = {}
    min_idx = min(state.keys())
    cur_idx = min_idx - 2
    while cur_idx <= max(state.keys()) + 2:
        pt = []
        for field_idx in range(cur_idx - 2, cur_idx + 3):
            pt.append(state.get(field_idx, '.'))
        pt = ''.join(pt)
        if pt in rules:
            new_state[cur_idx] = rules[pt]
        else:
            new_state[cur_idx] = '.'
        cur_idx += 1
    return new_state

def get_value(state):
    return sum(k for k, v in state.items() if v == '#')

def simulate(state, rules, n_iter, part_two=False):
    for i in range(1, n_iter + 1):
        prev_state = state.copy()
        state = transform(state, rules)
        if part_two:
            prev = ''.join([v for k, v in sorted(prev_state.items())]).strip('.')
            cur = ''.join([v for k, v in sorted(state.items())]).strip('.')
            if prev == cur:
                # No more change after this situation, only a shift in values
                prev_val = get_value(prev_state)
                cur_val = get_value(state)
                diff = cur_val - prev_val
                return cur_val + diff * (n_iter - i)
    return state

def parse_input(line_gen):
    state = {}
    rules = {}
    for line in line_gen:
        if 'initial' in line:
            for idx, c in enumerate(line.split(' ')[2]):
                state[idx] = c
        elif '=>' in line:
            rules[line[:5]] = line[-1]
    return state, rules

def part_one(line_gen):
    state, rules = parse_input(line_gen)
    state = simulate(state, rules, 20)
    return get_value(state)

def part_two(line_gen):
    state, rules = parse_input(line_gen)
    res = simulate(state, rules, 50000000000, True)
    return res

print("A: " + str(part_one(lib.get_input(12))))
print("B: " + str(part_two(lib.get_input(12))))
