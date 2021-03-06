#!/usr/bin/env python3

import lib.common as lib
import collections
import re

def read_rules(line_gen):
    rules = {}
    idx = 0
    for line in line_gen:
        if not line:
            break
        name, ranges = line.split(':')
        rules[idx] = {'name': name, 'valid': set()}
        m = re.findall(r'(\d+)-(\d+)', ranges)
        for lower, upper in m:
            rules[idx]['valid'] |= set(range(int(lower), int(upper) + 1))
        idx += 1
    return rules

def get_invalid_numbers(numbers, valid_numbers):
    invalid_numbers = []
    for num in numbers:
        if num not in valid_numbers:
            invalid_numbers.append(num)
    return invalid_numbers

def rule_applies(rule, column):
    # setA - setB returns items which are in setA but not in setB
    return len(column - rule['valid']) == 0

def solve(line_gen, part=1):
    valid_numbers = set()
    rules = read_rules(line_gen)
    for _, rule in rules.items():
        valid_numbers |= rule['valid']

    invalid_sum = 0
    valid_tickets = []
    my_ticket = None
    step = 1
    for line in line_gen: # multi line input
        if not line:
            step += 1
        elif step == 1 and ',' in line:
            my_ticket = [int(n) for n in line.split(',')]
            valid_tickets.append(my_ticket)
        elif step == 2 and ',' in line:
            nums = [int(n) for n in line.split(',')]
            invalid_numbers = get_invalid_numbers(nums, valid_numbers)
            if not invalid_numbers:
                valid_tickets.append(nums)
            invalid_sum += sum(invalid_numbers)

    if part == 1:
        return invalid_sum
    
    vals_in_cols = collections.defaultdict(set)
    for ticket in valid_tickets:
        for idx, num in enumerate(ticket):
            vals_in_cols[idx].add(num)

    rule_candidates = collections.defaultdict(set)
    for rule_idx, rule in rules.items():
        for col_idx, column_values in vals_in_cols.items():
            if rule_applies(rule, column_values):
                rule_candidates[col_idx].add(rule_idx)

    result = 1
    # if no candidates are left, we have a full solution and 
    while rule_candidates:
        # assign the column for which only one rule applies
        column, rule_idx = next(((k, v.pop()) for k, v in rule_candidates.items() if len(v) == 1))

        # remove the assigned column and the assigned rule from the
        # candidate list for the remaining columns
        del rule_candidates[column]
        for other_set in rule_candidates.values():
            other_set.remove(rule_idx)

        # If we assigned a departure rule to a column, aggregate the value from
        # our own ticket.
        if rules[rule_idx]['name'].startswith('departure'):
            result *= my_ticket[column]

    return result

def part_one(line_gen):
    return solve(line_gen)

def part_two(line_gen):
    return solve(line_gen, part=2)

print("A: " + str(part_one(lib.get_input(16))))
print("B: " + str(part_two(lib.get_input(16))))
