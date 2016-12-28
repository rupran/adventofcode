#!/usr/bin/env python3

import re
import lib.common as lib

def parse_pattern(line, index):
    """ Parse a repetition specification in @line at index @index.
    Returns the new index pointing to the next non-pattern character, the number
    of repeated characters and the number of repetitions."""
    n_chars = 1
    n_repetitions = 1

    match = re.match(r"^(\((\d+)x(\d+)\)).*", line[index:])
    if match:
        index += len(match.group(1))
        n_chars = int(match.group(2))
        n_repetitions = int(match.group(3))

    return index, n_chars, n_repetitions

def get_added_factor(line, offset, n_chars, n_repetitions, task):
    """ Calculate the number of chars added by a pattern. For task A, this is
    non-recursive and just returns the product of n_chars and n_repetitions.
    For task B, we need to recursively evaluate the pattern(s) at @offset."""
    if task == "A":
        return n_chars * n_repetitions
    else:
        return eval_pattern_length(line, offset, n_chars, task) * n_repetitions

def eval_pattern_length(line, offset, length, task):
    index = offset
    total_len = 0
    while index < offset + length:
        char = line[index]
        if char != "(":
            total_len += 1
            index += 1
        else:
            # Move index past the current pattern specification
            index, n_chars, n_repetitions = parse_pattern(line, index)
            # Add length by this pattern to total length
            total_len += get_added_factor(line, index, n_chars, n_repetitions, task)
            # Advance index past the chars covered by pattern
            index += n_chars

    return total_len

def part_one(line_gen):
    line = next(line_gen)
    return eval_pattern_length(line, 0, len(line), "A")

def part_two(line_gen):
    line = next(line_gen)
    return eval_pattern_length(line, 0, len(line), "B")

print("A: " + str(part_one(lib.get_input(9))))
print("B: " + str(part_two(lib.get_input(9))))
