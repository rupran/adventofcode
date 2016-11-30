import sys
import re

def toggle(tuple_map, from_x, from_y, to_x, to_y):
    for x in range(from_x, to_x+1):
        for y in range(from_y, to_y+1):
            tuple_map[(x,y)] = tuple_map[(x,y)] + 2

def turn_on(tuple_map, from_x, from_y, to_x, to_y):
    for x in range(from_x, to_x+1):
        for y in range(from_y, to_y+1):
            tuple_map[(x,y)] += 1

def turn_off(tuple_map, from_x, from_y, to_x, to_y):
    for x in range(from_x, to_x+1):
        for y in range(from_y, to_y+1):
            if tuple_map[(x,y)] > 0:
                tuple_map[(x,y)] -= 1

inp = [x.rstrip('\n') for x in sys.stdin.readlines()]

tuple_map = {}
for x in range(0,1000):
    for y in range(0,1000):
        tuple_map[(x,y)] = 0

for line in inp:
    matcher = re.match(r"([\w ]+) (\d+)\,(\d+) through (\d+)\,(\d+)", line)
    if matcher:
        mode = matcher.group(1)
        from_x = int(matcher.group(2))
        from_y = int(matcher.group(3))
        to_x = int(matcher.group(4))
        to_y = int(matcher.group(5))

        if mode == "toggle":
            toggle(tuple_map, from_x, from_y, to_x, to_y)
        elif mode == "turn on":
            turn_on(tuple_map, from_x, from_y, to_x, to_y)
        elif mode == "turn off":
            turn_off(tuple_map, from_x, from_y, to_x, to_y)

print sum([x for x in tuple_map.values() if x])
