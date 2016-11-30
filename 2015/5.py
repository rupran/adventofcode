import sys

def submatch(in_str, index1, index2):
    return in_str[index1] == in_str[index2]

def nice(in_str):
    req1 = sum([in_str.count(c) for c in set(['a', 'e', 'i', 'o', 'u'])]) >= 3
    req2 = any([submatch(in_str, a, a+1) for a in range(0, len(in_str)-1)])
    req3 = any(["ab" in in_str, "cd" in in_str, "pq" in in_str, "xy" in in_str])
    if req3:
        return False
    else:
        return req2 & req1

class Pair:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

def nice_2(in_str):
    all_pairs = [Pair(in_str[a], in_str[a+1]) for a in range(0, len(in_str)-1)]

    pair_map = {}
    index = 0
    req1 = False

    for p in all_pairs:
        if not (p.c1, p.c2) in pair_map:
            pair_map[(p.c1, p.c2)] = index
        elif pair_map[(p.c1, p.c2)] < index - 1:
            req1 = True
            break
        index += 1
    
    req2 = any([submatch(in_str, a, a+2) for a in range(0, len(in_str)-2)])
    return req1 & req2
    
inp = [x.rstrip('\n') for x in sys.stdin.readlines()]

nice_c = 0

for line in inp:
    if nice_2(line):
        nice_c += 1

print nice_c
