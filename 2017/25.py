#!/usr/bin/env python3

import collections

def part_one():
    tape = collections.defaultdict(int)
    state = 'A'
    pos = 0
    # transitions: (write if 0, move if 0, state if 0, write if 1, move if 1, state if 1)
    transitions = {'A': (1, 1, 'B', 0, -1, 'B'),
                   'B': (0, 1, 'C', 1, -1, 'B'),
                   'C': (1, 1, 'D', 0, -1, 'A'),
                   'D': (1, -1, 'E', 1, -1, 'F'),
                   'E': (1, -1, 'A', 0, -1, 'D'),
                   'F': (1, 1, 'A', 1, -1, 'E')}

    for _ in range(12629077):
        if tape[pos] == 0:
            tape[pos] = transitions[state][0]
            pos += transitions[state][1]
            state = transitions[state][2]
        else:
            tape[pos] = transitions[state][3]
            pos += transitions[state][4]
            state = transitions[state][5]

    return sum(tape.values())

def part_two():
    return 'There is no part two. We\'re done for this year!'

print("A: " + str(part_one()))
print("B: " + str(part_two()))
