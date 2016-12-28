#!/usr/bin/env python3

import collections
import re
import lib.common as lib

def rotate(in_deque, in_char):
    char_ind = in_deque.index(in_char)
    if char_ind > 3:
        char_ind += 1
    in_deque.rotate(char_ind + 1)

def swap(in_deque, index_1, index_2):
    tmp = in_deque[index_1]
    in_deque[index_1] = in_deque[index_2]
    in_deque[index_2] = tmp

def reverse_range(in_deque, start, end):
    prefix = list(in_deque)[:start]
    middle = collections.deque(list(in_deque)[start:end + 1])
    middle.reverse()
    suffix = list(in_deque)[end + 1:]
    return collections.deque(prefix + list(middle) + suffix)

def move_item(in_deque, from_index, to_index):
    value = in_deque[from_index]
    in_deque.remove(value)
    in_deque.insert(to_index, value)

def part_one(line_gen, in_deque):

    for line in line_gen:
        match = re.match(r"swap position (\d+) with position (\d+)", line)
        if match:
            swap(in_deque, int(match.group(1)), int(match.group(2)))
            continue
        match = re.match(r"swap letter (\w+) with letter (\w+)", line)
        if match:
            swap(in_deque, in_deque.index(match.group(1)),
                           in_deque.index(match.group(2)))
            continue
        match = re.match(r"rotate (left|right) (\d+) step(?:s|)", line)
        if match:
            if match.group(1) == "left":
                in_deque.rotate(-int(match.group(2)))
            else:
                in_deque.rotate(int(match.group(2)))
            continue
        match = re.match(r"rotate based on position of letter (\w+)", line)
        if match:
            rotate(in_deque, match.group(1))
            continue
        match = re.match(r"reverse positions (\d+) through (\d+)", line)
        if match:
            in_deque = reverse_range(in_deque, int(match.group(1)),
                                               int(match.group(2)))
            continue
        match = re.match(r"move position (\d+) to position (\d+)", line)
        if match:
            move_item(in_deque, int(match.group(1)), int(match.group(2)))
            continue

    return "".join(in_deque)

# Alternative solution for part two:
#def part_two(line_gen, to_search):
#    instrs = list(line_gen)
#    for string in itertools.permutations("abcdefgh"):
#        if part_one(instrs, collections.deque(string)) == "".join(to_search):
#            return "".join(string)

def part_two(line_gen, in_deque):
    # Go through instructions backward
    instrs = reversed(list(line_gen))
    for line in instrs:
        # Entirely reversible
        match = re.match(r"swap position (\d+) with position (\d+)", line)
        if match:
            swap(in_deque, int(match.group(1)), int(match.group(2)))
            continue
        # Entirely reversible
        match = re.match(r"swap letter (\w+) with letter (\w+)", line)
        if match:
            swap(in_deque, in_deque.index(match.group(1)),
                           in_deque.index(match.group(2)))
            continue
        # left shift forward means right shift backwards
        match = re.match(r"rotate (left|right) (\d+) step(?:s|)", line)
        if match:
            if match.group(1) == "left":
                in_deque.rotate(int(match.group(2)))
            else:
                in_deque.rotate(-int(match.group(2)))
            continue
        # Most complicated part: rotate 'result' backwards and try forward
        # rotation with given letter until we find the matching arrangement.
        match = re.match(r"rotate based on position of letter (\w+)", line)
        if match:
            shift_index = 0
            while True:
                cur = in_deque.copy()
                cur.rotate(-shift_index)
                back_shifted = cur.copy()
                rotate(cur, match.group(1))
                if cur == in_deque:
                    in_deque = back_shifted
                    break
                shift_index += 1
            continue
        # Entirely reversible
        match = re.match(r"reverse positions (\d+) through (\d+)", line)
        if match:
            in_deque = reverse_range(in_deque, int(match.group(1)),
                                               int(match.group(2)))
            continue
        # Swap from/to indices
        match = re.match(r"move position (\d+) to position (\d+)", line)
        if match:
            move_item(in_deque, int(match.group(2)), int(match.group(1)))

    return "".join(in_deque)

print("A: " + str(part_one(lib.get_input(21), collections.deque("abcdefgh"))))
print("B: " + str(part_two(lib.get_input(21), collections.deque("fbgdceah"))))
