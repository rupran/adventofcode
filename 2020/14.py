#!/usr/bin/env python3

import re
import lib.common as lib

def merge_mask(number, mask):
    masked_bits = [c for c in '{0:0>36}'.format(bin(int(number))[2:])]
    for idx, bit in enumerate(mask):
        if bit == 'X':
            continue
        masked_bits[idx] = bit
    return int(''.join(masked_bits), 2)

def part_one(line_gen):
    mem = {}
    cur_mask = ['X' * 36]
    for line in line_gen:
        cmd, val = (x.strip() for x in line.split('='))
        if cmd == 'mask':
            cur_mask = val
        elif m := re.match(r'mem\[(\d+)\]', cmd):
            cell = m.group(1)
            mem[cell] = merge_mask(val, cur_mask)
    return sum(mem.values())

def or_mask(number, mask):
    masked_bits = [c for c in '{0:0>36}'.format(bin(int(number))[2:])]
    for idx, bit in enumerate(mask):
        if bit == 'X':
            masked_bits[idx] = bit
        else:
            masked_bits[idx] = str(int(masked_bits[idx]) | int(bit))
    return masked_bits

def gen_mask_combinations(mask):
    for num in range(2 ** mask.count('X')):
        current_num = []
        # Generate the bits that need to replace the 'X'es in the mask.
        # Reversed as we build the number from the mask bits in reverse
        # order and replace later bits first.
        splice = list(reversed(bin(num)[2:]))
        splice_idx = 0
        for idx in range(len(mask) - 1, -1, -1):
            # If the current bit in the mask is fixed, keep it.
            if mask[idx] != 'X':
                current_num.append(mask[idx])
            else:
                # If we still have bits to splice, write that bit into the
                # 'X' position. Otherwise, we're writing 0 as we already
                # wrote all lesser significant bits.
                if splice_idx < len(splice):
                    current_num.append(splice[splice_idx])
                    splice_idx += 1
                else:
                    current_num.append('0')
        # If we build the current_num list forward (i.e. by moving through
        # the passed mask using 'range(len(mask))' instead of
        # 'range(len(mask) - 1, -1, -1)', we don't need to reverse() the
        # list here - the result is the same but the resulting numbers will
        # not be sorted in ascending order.
        yield ''.join(reversed(current_num))

def part_two(line_gen):
    mem = {}
    cur_mask = ['X' * 36]
    for line in line_gen:
        cmd, val = (x.strip() for x in line.split('='))
        if cmd == 'mask':
            cur_mask = val
        elif m := re.match(r'mem\[(\d+)\]', cmd):
            addr_mask = or_mask(m.group(1), cur_mask)
            for addr in gen_mask_combinations(addr_mask):
                mem[addr] = int(val)
    return sum(mem.values())

print("A: " + str(part_one(lib.get_input(14))))
print("B: " + str(part_two(lib.get_input(14))))
