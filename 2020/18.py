#!/usr/bin/env python3

import re
import lib.common as lib

# In a flattened formula, we need to compute the sums first (as 
# they have precedence over the product)
def calc_flat_formula(tokens, from_idx, to_idx):
    splits = ''.join(tokens[from_idx:to_idx]).split('*')
    sums = []
    for split in splits:
        sums.append(sum(int(c) for c in split.split('+')))
    prod = 1
    for s in sums:
        prod *= s
    return prod

def find_closing_bracket(tokens, from_idx):
    # Find the corresponding closing bracket for the bracket at from_idx
    cur = from_idx
    nesting = 0
    while cur < len(tokens):
        if tokens[cur] == '(':
            nesting += 1
        elif tokens[cur] == ')':
            nesting -= 1
            if nesting == 0:
                return cur
        cur += 1

def parse_from_to(tokens, from_idx, to_idx):
    # Replace contents of brackets with their flat value
    while '(' in tokens[from_idx:to_idx]:
        opening = tokens.index('(', from_idx, to_idx)
        closing = find_closing_bracket(tokens, opening)
        middle = parse_from_to(tokens, opening + 1, closing)
        tokens = tokens[0:opening] + [str(middle)] + tokens[closing+1:to_idx]
        to_idx -= (closing - opening)

    # Calculate the flat value for this expression
    return calc_flat_formula(tokens, from_idx, to_idx)

def parse_subformula(tokens, cur_idx):
    acc = 0
    last_op = None
    while cur_idx < len(tokens):
        token = tokens[cur_idx]
        next_idx = cur_idx + 1
        if token == '(':
            sub_result, end_idx = parse_subformula(tokens, cur_idx + 1)
            next_idx = end_idx + 1
        elif token in ('*', '+'):
            last_op = token
            cur_idx += 1
            continue
        elif token == ')':
            return acc, cur_idx
        else:
            sub_result = int(token)

        if last_op is None:
             acc = sub_result
        elif last_op == '+':
            acc += sub_result
        else:
            acc *= sub_result
        cur_idx = next_idx
    return acc
        
def read_formula(line, part_two=False):
    tokens = [c for c in re.sub(' ', '', line)]
    if part_two:
        return parse_from_to(tokens, 0, len(tokens))
    return parse_subformula(tokens, 0)

def part_one(line_gen):
    return sum(read_formula(inp) for inp in line_gen)

def part_two(line_gen):
    return sum(read_formula(inp, part_two=True) for inp in line_gen)

print("A: " + str(part_one(lib.get_input(18))))
print("B: " + str(part_two(lib.get_input(18))))
