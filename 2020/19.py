#!/usr/bin/env python3

import collections
import itertools
import copy
import lib.common as lib

def add_to_field(dictionary, i, j, value):
    if i not in dictionary:
        dictionary[i] = {}
    if j not in dictionary[i]:
        dictionary[i][j] = set()
    dictionary[i][j].add(value)

def get_field(dictionary, i, j):
    if i not in dictionary:
        dictionary[i] = {}
    if j not in dictionary[i]:
        dictionary[i][j] = set()
    return dictionary[i][j]

def matches_rules(word, rules_reversed):
    v = {}
    n = len(word)
    for idx, c in enumerate(list(c for c in word)):
        for lhs in rules_reversed[c]:
            add_to_field(v, idx + 1, 1, lhs)

    for j in range(2, n + 1):
        for i in range(1, n - j + 1 + 1):
            for k in range(1, j - 1 + 1):
                b_set = get_field(v, i, k)
                c_set = get_field(v, i + k, j - k)
                possible_rules = list(itertools.product(b_set, c_set))
                for rule in list(possible_rules):
                    for lhs in rules_reversed[rule]:                      
                        add_to_field(v, i, j, lhs)
#                        if lhs == 0 and i == 1 and j == n:
#                            return True
    if '0' in get_field(v, 1, n):
        return True
    return False

def chomsky_normal_form(rules):
    changed = True
    while changed:
        new_rules = copy.deepcopy(rules)
        n_rules = len(rules)
        changed = False 
        for lhs, rhs_rules in rules.items():
            for rhs_rule in rhs_rules:
                if len(rhs_rule) == 3:
                    # A -> B C D => A -> B E; E -> C D
                    new_rules[lhs].remove(rhs_rule)
                    new_lhs = str(n_rules)
                    new_rules[lhs].append((rhs_rule[0], new_lhs))
                    new_rules[new_lhs].append((rhs_rule[1], rhs_rule[2]))
                    n_rules += 1
                    changed = True
        rules = new_rules

    changed = True
    while changed:
        changed = False
        new_rules = copy.deepcopy(rules)
        n_rules = len(rules)
        for lhs, rhs_rules in rules.items():
            for rhs_rule in rhs_rules:
                if len(rhs_rule) == 1 and type(rhs_rule) != str:
                    # Found a rule A -> B
                    # => need to delete A -> B and replace B -> * with A -> *
                    new_rules[lhs].remove(rhs_rule)
                    for new_rhs in rules[rhs_rule[0]]:
                        new_rules[lhs].append(new_rhs)
                    changed = True
        rules = new_rules

    return rules

def run(line_gen, part):
    rules = collections.defaultdict(list)
    for line in line_gen:
        if not line:
            break
        lhs, rhs = line.split(':')
        if '\"' in rhs:
            rh_rules = rhs.split('\"')[1]
        else:
            rh_rules = list(tuple(rule.strip().split()) for rule in rhs.split('|'))
        rules[lhs] = rh_rules

    if part == 2:
        rules['8'] = [('42',), ('42', '8')]
        rules['11'] = [('42', '31'), ('42', '11', '31')]

    rules = chomsky_normal_form(rules)

    rules_reversed = collections.defaultdict(list)
    for lhs, rhses in rules.items():
        for rhs in rhses:
            rules_reversed[rhs].append(lhs)

    count = 0
    for line in line_gen:
        if matches_rules(line, rules_reversed):
            count += 1
    return count

def part_one(line_gen):
    return run(line_gen, part=1)

def part_two(line_gen):
    return run(line_gen, part=2)

print("A: " + str(part_one(lib.get_input(19))))
print("B: " + str(part_two(lib.get_input(19))))
