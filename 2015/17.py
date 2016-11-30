import sys
import re

sizes = []
used = []
options = 0
used_dict = {}

def backpack(cur_index, fill):
    global options
    if cur_index >= len(sizes):
        if fill == 150:
            options += 1
            if sum(used) in used_dict:
                used_dict[sum(used)] += 1
            else:
                used_dict[sum(used)] = 1
        return
    if fill > 150:
        return

    opt1 = backpack(cur_index + 1, fill)
    used[cur_index] = 1
    opt2 = backpack(cur_index + 1, fill + sizes[cur_index])
    used[cur_index] = 0

inp = [x.strip() for x in sys.stdin.readlines()]

for line in inp:
    sizes.append(int(line))
    used.append(0)

backpack(0, 0)
print "A: " + str(options)
print "B: " + str(used_dict[min(used_dict.keys())])
