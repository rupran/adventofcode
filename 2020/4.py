#!/usr/bin/env python3

import re

import lib.common as lib

keywords = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])

def check_valid_one(passport):
    return all(key in passport.keys() for key in keywords)

def check_valid_two(passport):
    if not all(key in passport.keys() for key in keywords):
        return False
    to_check = passport['byr']
    if len(to_check) != 4 or int(to_check) < 1920 or int(to_check) > 2002:
        return False 
    to_check = passport['iyr']
    if len(to_check) != 4 or int(to_check) < 2010 or int(to_check) > 2020:
        return False
    to_check = passport['eyr']
    if len(to_check) != 4 or int(to_check) < 2020 or int(to_check) > 2030:
        return False
    to_check = passport['pid']
    if len(to_check) != 9:
        return False
    to_check = passport['hcl']
    if not re.match(r'#[0-9a-f]{6}', to_check):
        return False
    to_check = passport['ecl']
    if to_check not in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False
    to_check = passport['hgt']
    match = re.match(r'([0-9]+)(cm|in)', to_check)
    if not match:
        return False
    if match.group(2) == 'in' and (int(match.group(1)) < 59 or int(match.group(1)) > 76):
        return False
    elif match.group(2) == 'cm' and (int(match.group(1)) < 150 or int(match.group(1)) > 193):
        return False
    return True 

def process(line_gen, check_fn):
    passports = []
    current = dict()
    for line in line_gen: # multi line input
        if not line:
            passports.append(current)
            current = dict()
            continue
        fields = line.split()
        for field in fields:
            k, v = field.split(':')
            current[k] = v
    passports.append(current)

    valid = 0
    for passport in passports:
        if check_fn(passport):
            valid += 1
    return valid

def part_one(line_gen):
    return process(line_gen, check_valid_one)

def part_two(line_gen):
    return process(line_gen, check_valid_two)

print("A: " + str(part_one(lib.get_input(4))))
print("B: " + str(part_two(lib.get_input(4))))
