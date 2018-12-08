#!/usr/bin/env python3

import collections
import lib.common as lib

def build_tree(from_index, nums, meta_offset, children):
    n_children = nums[from_index]
    n_metadata = nums[from_index + 1]
    cur_len = 2 + n_metadata
    cur_child = from_index + 2
    for n in range(n_children):
        children[from_index].append(cur_child)
        l = build_tree(cur_child, nums, meta_offset, children)
        cur_child += l
        cur_len += l
    meta_offset[from_index] = cur_len - n_metadata
    return cur_len
        
def get_value(idx, nums, children, meta_offset, cache):
    if idx in cache:
        return cache[idx]
    n_meta = nums[idx + 1]
    if not children[idx]:
        return sum(nums[idx + meta_offset[idx]:idx + meta_offset[idx] + n_meta])
    s = 0
    for meta_entry in nums[idx + meta_offset[idx]:idx + meta_offset[idx] + n_meta]:
        if meta_entry == 0:
            continue
        meta_entry -= 1
        if meta_entry < len(children[idx]):
            s += get_value(children[idx][meta_entry], nums, children, meta_offset,
cache)
    cache[idx] = s
    return s

def calc_solution(line_gen, part_two=False):
    nums = [int(num) for num in next(line_gen).split()]
    children = collections.defaultdict(list)
    meta_offset = {}
    build_tree(0, nums, meta_offset, children)
    if part_two:
        cache = {}
        return get_value(0, nums, children, meta_offset, cache)
    else:
        return sum(sum(nums[idx + offset:idx + offset + nums[idx + 1]])
                   for idx, offset in meta_offset.items())

def part_one(line_gen):
    return calc_solution(line_gen)

def part_two(line_gen):
    return calc_solution(line_gen, part_two=True)

print("A: " + str(part_one(lib.get_input(8))))
print("B: " + str(part_two(lib.get_input(8))))
