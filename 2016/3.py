import sys
import re

def is_possible(a, b, c):
    return a + b > c and a + c > b and b + c > a

def first_part(infile):
    possible = 0
    for line in infile.readlines():
        a, b, c = (int(x) for x in line.split())
        if is_possible(a, b, c):
            possible += 1

    return possible

def second_part(infile):
    all_lines = infile.readlines()
    possible = 0
    cur_index = 0
    end_index = 3
    while end_index <= len(all_lines):
        cur_lines = all_lines[cur_index:end_index]

        triangles = [[], [], []]
        for i in range(0, 3):
            a, b, c = (int(x) for x in cur_lines[i].split())
            triangles[0].append(a)
            triangles[1].append(b)
            triangles[2].append(c)

        for i in range(0, 3):
            if is_possible(triangles[i][0], triangles[i][1], triangles[i][2]):
                possible += 1

        cur_index += 3
        end_index += 3

    return possible


with open(sys.argv[1], "r") as infile:
    print(first_part(infile))

with open(sys.argv[1], "r") as infile:
    print(second_part(infile))

