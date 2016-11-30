import sys
import re
import itertools
import collections

inp = [x.strip() for x in sys.stdin.readlines()]
vals = collections.defaultdict(dict)

def eval_arrangement(arrangement):
    this_sum = 0
    for index in range(0, len(arrangement)):
        fr = arrangement[index]
        to_1 = arrangement[index-1]
        to_2 = arrangement[(index+1) % len(arrangement)]
        this_sum += vals[fr][to_1] + vals[fr][to_2]
    return this_sum

def find_max_arrangement():
    arrangements = [x for x in itertools.permutations(vals.keys())]
    return max(eval_arrangement(x) for x in arrangements)

for line in inp:
    matcher = re.match("(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).", line)
    if matcher:
        fr = matcher.group(1)
        delta = matcher.group(2)
        val = int(matcher.group(3))
        if delta == "lose":
            val = -val
        to = matcher.group(4)
        vals[fr][to] = val

opt = find_max_arrangement()
print "A: " + str(opt)

for key in set(vals.keys()):
    vals["Me"][key] = 0
    vals[key]["Me"] = 0

opt = find_max_arrangement()
print "B: " + str(opt)
