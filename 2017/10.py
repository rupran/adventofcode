#!/usr/bin/env python3

import lib.common as lib

def reverse_sublist(lst, from_idx, length):
    end_idx = from_idx + length
    if end_idx >= len(lst):
        rem = end_idx % len(lst)
        reversed_slice = list(reversed(lst[from_idx:] + lst[:rem]))

        new_lst = [-1 for _ in range(len(lst))]
        cur_idx = from_idx
        index_in_reversed = 0
        while index_in_reversed < len(reversed_slice):
            new_lst[cur_idx] = reversed_slice[index_in_reversed]
            cur_idx += 1
            if cur_idx == len(lst):
                cur_idx = 0
            index_in_reversed += 1

        new_lst[cur_idx:from_idx] = lst[cur_idx:from_idx]
    else:
        new_lst = lst[:from_idx] + \
                    list(reversed(lst[from_idx:end_idx])) + \
                    lst[end_idx:]
    return new_lst

def knot_hash(lst, in_vals, cur_pos=0, skip_size=0):
    for length in in_vals:
        lst = reverse_sublist(lst, cur_pos, length)
        cur_pos += length + skip_size
        cur_pos %= len(lst)
        skip_size += 1
    return (lst, cur_pos, skip_size)

def part_one(line_gen):
    lst = [x for x in range(256)]
    lengths = [int(x) for x in next(line_gen).split(',')]
    lst, _, _ = knot_hash(lst, lengths)
    return lst[0] * lst[1]

def hexify(lst):
    hex_str = ''
    for i in range(len(lst)//16):
        cur_val = lst[i*16]
        for j in range(1, 16):
            cur_val ^= int(lst[i*16+j])
        hex_str += '{:02x}'.format(cur_val)
    return hex_str

def part_two(line_gen):
    lst = [x for x in range(256)]
    lengths = [ord(x) for x in next(line_gen)]
    lengths += [17, 31, 73, 47, 23]
    rounds = 64
    cur_pos = 0
    skip_size = 0
    for _ in range(rounds):
        lst, cur_pos, skip_size = knot_hash(lst, lengths, cur_pos, skip_size)

    return hexify(lst)

print("A: " + str(part_one(lib.get_input(10))))
print("B: " + str(part_two(lib.get_input(10))))
