#!/usr/bin/env python3

import collections
import re

import lib.common as lib

def bfs(start, adj):
    visited = set()
    worklist = collections.deque()
    worklist.append(start)
    while worklist:
        cur = worklist.popleft()
        visited.add(cur)
        for child in adj[cur]:
            if child not in visited:
                worklist.append(child)

    return visited

def parse(line_gen, second_part=False):
    groups = []
    adj = collections.defaultdict(set)
    for line in line_gen:
        left, right = re.match(r'^(\d+) <-> (.+)$', line).groups()
        left = int(left)
        right = [int(x.strip()) for x in right.split(',')]
        adj[left].update(x for x in right)
        for succ in right:
            adj[succ].add(left)

    vis = set()
    counter = 0
    for start in adj.keys():
        if start in vis:
            continue
        cur_group = bfs(start, adj)
        if not second_part and 0 in cur_group:
            return len(cur_group)
        vis.update(cur_group)
        groups.append(cur_group)
        counter += 1

    return counter

def part_one(line_gen):
    return parse(line_gen)

def part_two(line_gen):
    return parse(line_gen, True)

print("A: " + str(part_one(lib.get_input(12))))
print("B: " + str(part_two(lib.get_input(12))))
