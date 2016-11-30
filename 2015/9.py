import sys
import re
import collections
import itertools


inp = [x.strip() for x in sys.stdin.readlines()]
out_edges = collections.defaultdict(set)

def cost(tour):
    cur_sum = 0
    for index in range(0, len(tour)-1):
        cur_sum += int([x[1] for x in out_edges[tour[index]] if x[0] == tour[index+1]][0])
    return cur_sum

for line in inp:
    matcher = re.match(r"(\w+) to (\w+) = (\d+)", line)
    if matcher:
        fr = matcher.group(1)
        to = matcher.group(2)
        e_cost = matcher.group(3)

        out_edges[fr].add((to, e_cost))
        out_edges[to].add((fr, e_cost))

n = len(out_edges.keys())

tours = [x for x in itertools.permutations(out_edges.keys())]
min_tour = min([cost(tour) for tour in tours])
max_tour = max([cost(tour) for tour in tours])

print "A: " + str(min_tour)
print "B: " + str(max_tour)
