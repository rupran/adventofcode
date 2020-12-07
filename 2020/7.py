#!/usr/bin/env python3

import collections
import re
import lib.common as lib

def build_contained_in_graph(line_gen):
    # Build a graph from right hand side to left hand side, i.e. outgoing
    # edges denote a 'contained in' relationship
    graph = collections.defaultdict(set)
    for line in line_gen: # multi line input
        if match := re.match(r'(.*) bags contain (.*)', line):
            lhs = match.group(1)
            rhs = []
            for item in match.group(2).split(','):
                if m := re.match(r'\d+ (.*) bag(:?s|).*', item.strip()):
                    graph[m.group(1)].add(lhs)
    return graph

def build_contains_graph(line_gen):
    # Build a graph from right hand side to left hand side, i.e. outgoing
    # edges denote a 'contained in' relationship
    graph = collections.defaultdict(set)
    for line in line_gen: # multi line input
        if match := re.match(r'(.*) bags contain (.*)', line):
            lhs = match.group(1)
            rhs = []
            for item in match.group(2).split(','):
                if m := re.match(r'(\d+) (.*) bag(:?s|).*', item.strip()):
                    graph[lhs].add((m.group(2), int(m.group(1))))
    return graph

def part_one(line_gen):
    graph = build_contained_in_graph(line_gen)

    # Traverse the graph, starting at the shiny gold bag, and check
    # which nodes are reachable through the 'contained in' relationship
    worklist = ['shiny gold']
    visited = set()
    while worklist:
        cur = worklist.pop()
        outgoing = graph[cur]
        for item in outgoing:
            if item not in visited:
                visited.add(item)
                worklist.append(item)
    return len(visited)

def calc_cost(node, graph, cost_cache):
    if node in cost_cache:
        return cost_cache[node]
    # If the current node contains no other bags, its cost is 1
    result = 1
    for (outgoing, number) in graph[node]:
        result += (number * calc_cost(outgoing, graph, cost_cache))
    cost_cache[node] = result
    return result

def part_two(line_gen):
    graph = build_contains_graph(line_gen)

    cost_cache = {}
    # Subtract 1 because we don't count 'shiny gold' itself
    return calc_cost('shiny gold', graph, cost_cache) - 1
    

print("A: " + str(part_one(lib.get_input(7))))
print("B: " + str(part_two(lib.get_input(7))))
