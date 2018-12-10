#!/usr/bin/env python3

import collections

import lib.common as lib

def run_game(n_players, last_marble):
    marbles = collections.deque([0])
    cur_marble = 0
    scores = [0] * n_players
    cur_player = 0
    while cur_marble <= last_marble:
        next_marble = cur_marble + 1
        if next_marble % 23 == 0:
            scores[cur_player] += next_marble
            marbles.rotate(7)
            scores[cur_player] += marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(next_marble)
        cur_player = (cur_player + 1) % n_players
        cur_marble = next_marble

    return(max(scores))

def part_one(line_gen):
    return run_game(476, 71431)

def part_two(line_gen):
    return run_game(476, 71431 * 100)

print("A: " + str(part_one(lib.get_input(9))))
print("B: " + str(part_two(lib.get_input(9))))
