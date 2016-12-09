#!/usr/bin/env python3

import lib.common as lib

def part_one(line_gen):
    line = next(line_gen)
    total_str = ""
    line_len = len(line)
    index = 0
    while index < line_len:
        next_count = 0
        char = line[index]
        next_string = ""
        if char != "(" and char != ")":
            next_string += char
            index += 1
        else:
            if char == "(":
                index += 1
                char = line[index]
                repeat_pattern = ""
                repeat_len = 0
                while char != "x":
                    next_count *= 10
                    next_count += int(char)
                    index += 1
                    char = line[index]
                index += 1
                char = line[index]
                while char != ")":
                    repeat_len *= 10
                    repeat_len += int(char)
                    index += 1
                    char = line[index]
                index += 1
                for _ in range(next_count):
                    char = line[index]
                    repeat_pattern += char
                    index += 1

                next_string = "".join([repeat_pattern] * repeat_len)

        total_str += next_string

    return len(total_str)

def part_two(line_gen):
    # line = next(line_gen) # one line input
    # for line in line_gen: # multi line input
    pass

print("A: " + str(part_one(lib.get_input(9))))
print("B: " + str(part_two(lib.get_input(9))))
