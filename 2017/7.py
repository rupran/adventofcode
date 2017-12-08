#!/usr/bin/env python3

import collections
import re

import lib.common as lib

class Node:
    def __init__(self, name, weight, succs, preds):
        self.name = name
        self.weight = weight
        self.succs = succs
        self.preds = preds
        self.stack_weight = -1

root = None
nodes = {}

def part_one(line_gen):
    global root
    names = set()
    weights = {}
    successors = collections.defaultdict(list)
    preds = collections.defaultdict(list)
    for line in line_gen:
        match = re.match(r"^([a-z]+) \(([0-9]+)\)(?:| -> ([a-z, ]+))$", line)
        if match:
            name, weight, succs = match.groups()
            weights[name] = int(weight)
            names.add(name)
            if succs is None:
                succs = []
            else:
                succs = succs.split(', ')
                for succ in succs:
                    preds[succ].append(name)
            successors[name] = succs

    for name in names:
        node = Node(name, weights[name], successors[name], preds[name])
        nodes[name] = node

    root = [nodes[x] for x in names if not nodes[x].preds][0]
    return root.name

def calc_stack_weight(name):
    if nodes[name].stack_weight == -1:
        nodes[name].stack_weight = nodes[name].weight + \
                sum(calc_stack_weight(x) for x in nodes[name].succs)

    return nodes[name].stack_weight

def part_two():
    # Part one must have already built the graph
    cur_node = root
    sibling_weights = root.weight
    while True:
        succs = [(calc_stack_weight(x), x) for x in cur_node.succs]
        # If all sub-weights are equal, the current node is the culprit and must
        # be adjusted. As its stack weight must match its siblings, we need to
        # calculate the difference between the siblings' stack weights and the
        # sum of all sucessors' weights as the target weight.
        if len(set([x[0] for x in succs])) == 1:
            return sibling_weights - sum(x[0] for x in succs)

        # Dirty hack to find the odd weight and the matching sibling weights
        temp = sorted(succs)
        odd_weight, next_node = temp[0]
        sibling_weights = temp[1][0]
        # If first and second element are equal, they are the sibling weights.
        # In this case, the odd one must be the last weight (it was bigger than
        # the others) and the first one can be used as the sibling weight
        if odd_weight == temp[1][0]:
            odd_weight, next_node = temp[-1]
            sibling_weights = temp[0][0]

        cur_node = nodes[next_node]

print("A: " + str(part_one(lib.get_input(7))))
print("B: " + str(part_two()))
