#!/usr/bin/env python3

from collections import Counter
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

def knot_hash_one_round(lst, in_vals, cur_pos=0, skip_size=0):
    for length in in_vals:
        lst = reverse_sublist(lst, cur_pos, length)
        cur_pos += length + skip_size
        cur_pos %= len(lst)
        skip_size += 1
    return (lst, cur_pos, skip_size)

def knot_hash(key, rounds=64):
    cur_pos = 0
    skip_size = 0
    lst = [x for x in range(256)]
    key = [ord(x) for x in key] + [17, 31, 73, 47, 23]

    for _ in range(rounds):
        lst, cur_pos, skip_size = knot_hash_one_round(lst, key, cur_pos, skip_size)

    return lst

def hexify(lst):
    hex_str = ''
    for i in range(len(lst)//16):
        cur_val = lst[i*16]
        for j in range(1, 16):
            cur_val ^= int(lst[i*16+j])
        hex_str += '{:02x}'.format(cur_val)
    return hex_str

def bitify(lst):
    return ''.join('{:04b}'.format(int(char, 16)) for char in hexify(lst))

def get_field(in_string):
    field = []
    for i in range(128):
        bits = bitify(knot_hash('{}-{}'.format(in_string, i)))
        field.append(['#' if int(c) == 1 else '.' for c in bits])
    return field

def part_one(line_gen):
    return sum(Counter(row)['#'] for row in get_field(next(line_gen)))

def fill_region(start_y, start_x, value, field):
    workset = set()
    workset.add((start_y, start_x))
    while workset:
        cur_y, cur_x = workset.pop()
        field[cur_y][cur_x] = value
        neighbours = [(cur_y+i, cur_x+j) for i in [-1, 0, 1]
                      for j in [-1, 0, 1] if abs(i) != abs(j)]

        for adj_y, adj_x in neighbours:
            if adj_y < 0 or adj_y > 127 or adj_x < 0 or adj_x > 127:
                continue
            if field[adj_y][adj_x] == '#':
                workset.add((adj_y, adj_x))

def part_two(line_gen):
    field = get_field(next(line_gen))
    region_counter = 0
    for y_idx, row in enumerate(field):
        for x_idx, elem in enumerate(row):
            if elem == '#':
                fill_region(y_idx, x_idx, region_counter, field)
                region_counter += 1
    return region_counter

print("A: " + str(part_one(lib.get_input(14))))
print("B: " + str(part_two(lib.get_input(14))))
