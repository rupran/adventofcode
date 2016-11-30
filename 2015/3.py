import sys

visited = set()

cur_x = 0
cur_y = 0
cur_x2 = 0
cur_y2 = 0

modul = 0

inp = str([x.rstrip('\n') for x in sys.stdin.readlines()][0])

visited.add((0, 0))

for c in inp:
    if modul == 0:
        if c == "<":
            cur_x -= 1
        elif c == ">":
            cur_x += 1
        elif c == "^":
            cur_y += 1
        elif c == "v":
            cur_y -= 1
        visited.add((cur_x, cur_y))
        modul = 1
    else:
        if c == "<":
            cur_x2 -= 1
        elif c == ">":
            cur_x2 += 1
        elif c == "^":
            cur_y2 += 1
        elif c == "v":
            cur_y2 -= 1
        visited.add((cur_x2, cur_y2))
        modul = 0 

print len(visited)
