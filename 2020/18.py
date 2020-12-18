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

def accumulate_flat_formula(tokens, from_idx, to_idx):
    result = int(tokens[from_idx])
    from_idx += 1
    cur_op = None
    while from_idx < to_idx:
        if tokens[from_idx] in ('+', '*'):
            cur_op = tokens[from_idx]
        elif cur_op == '+':
            result += int(tokens[from_idx])
        elif cur_op == '*':
            result *= int(tokens[from_idx])
        from_idx += 1
    return result

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

def parse_from_to(tokens, from_idx, to_idx, part=1):
    # Replace contents of brackets with their flat value
    while '(' in tokens[from_idx:to_idx]:
        opening = tokens.index('(', from_idx, to_idx)
        closing = find_closing_bracket(tokens, opening)
        middle = parse_from_to(tokens, opening + 1, closing, part)
        tokens = tokens[0:opening] + [str(middle)] + tokens[closing+1:to_idx]
        to_idx -= (closing - opening)

    # Calculate the flat value for this expression
    if part == 1:
        return accumulate_flat_formula(tokens, from_idx, to_idx)
    else:
        return calc_flat_formula(tokens, from_idx, to_idx)
        
def read_formula(line, part=1):
    tokens = [c for c in re.sub(' ', '', line)]
    return parse_from_to(tokens, 0, len(tokens), part)

def part_one(line_gen):
    return sum(read_formula(inp) for inp in line_gen)

def part_two(line_gen):
    return sum(read_formula(inp, part=2) for inp in line_gen)

print("A: " + str(part_one(lib.get_input(18))))
print("B: " + str(part_two(lib.get_input(18))))
