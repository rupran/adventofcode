#!/usr/bin/env python3

import collections

import lib.common as lib

def dfs(node, in_port, prev_strength, prev_len, edges, visited, lengths):
    if node in visited:
        return 0

    # We can only leave over the port which we didn't enter through
    out_port = node[0]
    if node[0] == in_port:
        out_port = node[1]

    strength = prev_strength + sum(node)
    length = prev_len + 1

    visited.add(node)
    for succ in edges[node]:
        # Skip nodes only connected through our in_port
        if out_port not in succ:
            continue
        dfs(succ, out_port, strength, length, edges, visited, lengths)
    visited.remove(node)

    lengths[length].add(strength)

def run(line_gen, second_part=False):
    nodes = []
    edges = collections.defaultdict(set)
    for line in line_gen:
        nodes.append(tuple(int(x) for x in line.split('/')))
    for idx, node in enumerate(nodes):
        for _, node_2 in enumerate(nodes[idx+1:]):
            if node[0] in node_2 or node[1] in node_2:
                edges[node].add(node_2)
                edges[node_2].add(node)

    lengths = collections.defaultdict(set)
    for start_node in (node for node in nodes if 0 in node):
        dfs(start_node, 0, 0, 0, edges, set(), lengths)

    if second_part:
        # maximum strength for biggest length
        return max(lengths[max(lengths.keys())])
    else:
        # maximum over all strengths in every length
        return max(max(x) for x in lengths.values())

def part_one(line_gen):
    return run(line_gen)

def part_two(line_gen):
    return run(line_gen, True)

print("A: " + str(part_one(lib.get_input(24))))
print("B: " + str(part_two(lib.get_input(24))))
