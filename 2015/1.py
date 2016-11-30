import os
import sys

string = sys.stdin.readlines()[0]
current_floor = 0
index = 0
for c in string:
    if c == '(':
        current_floor += 1
    elif c == ')':
        current_floor -= 1
    index += 1

    if current_floor == -1:
        print "At " + str(index)
