#!/usr/bin/env python3

import re
import lib.common as lib

def part_one(line_gen):
    total = 0
    abba_string = r"([a-z])(?!\1)(.)\2\1"
    # Find abba patterns in general
    abba_regex = re.compile(r".*" + abba_string + r".*")
    # Find abba patterns inside []
    in_brackets = re.compile(r".*\[[^\]]*" + abba_string + r".*?\].*")

    for line in line_gen: # multi line input
        # if there is a pattern... 
        if abba_regex.search(line):
            # ... and no pattern inside brackets...
            if not in_brackets.search(line):
                # match it!
                total += 1

    return total

def part_two(line_gen):
    total = 0
    aba_string = r"([a-z])(?!\1)([^\[\]])\1"
    aba_regex = re.compile(aba_string + r".*")

    for line in line_gen: # multi line input
        outside_matches = []
        offset = 0
        while offset < len(line) - 1:
            # Skip stuff in brackets for now
            if line[offset] == "[":
                while line[offset] != "]":
                    offset += 1

            # Collect overlapping matches
            match = aba_regex.match(line, offset)
            if match:
                outside_matches.append(match)
            offset += 1

        # Iterate over matches until we found one 
        found_one = False
        for match in outside_matches:
            reverse = match.group(2) + match.group(1) + match.group(2)
            rev_offset = 0
            in_brackets = False
            # ... until we found a corresponding reverse
            while not found_one and rev_offset < len(line) - 1:
                # skip characters outside brackets now
                if not line[rev_offset] == "[":
                    if not in_brackets:
                        rev_offset += 1
                        continue
                else:
                    in_brackets = True

                # Match reverse at current offset
                rev_match = re.match(r"(" + reverse + r")", line[rev_offset:])
                if rev_match:
                    total += 1
                    found_one = True
                    break

                rev_offset += 1
                # Check for closing bracket and advance past it
                if line[rev_offset] == "]":
                    in_brackets = False
                    rev_offset += 1

    return total

print("A: " + str(part_one(lib.get_input(7))))
print("B: " + str(part_two(lib.get_input(7))))
