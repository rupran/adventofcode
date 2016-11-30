import sys
import re

class Sue:
    def __init__(self, number, first, first_n, second, second_n, third, third_n):
        self.number = number
        self.container = {}
        self.container[first] = int(first_n)
        self.container[second] = int(second_n)
        self.container[third] = int(third_n)

    def matches(self, description):
        retval = False
        for key in description:
            if key in self.container:
                if (key == "cats" or key == "trees"):
                    if self.container[key] > description[key]:
                        continue
                    else:
                        return False
                elif (key == "pomeranians" or key == "goldfish"):
                    if self.container[key] < description[key]:
                        continue
                    else:
                        return False
                elif self.container[key] != description[key]:
                    return False

        return True

inp = [x.strip() for x in sys.stdin.readlines()]
sues = []
description = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
               'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2,
               'perfumes': 1}


for line in inp:
    matcher = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line) 
    if matcher:
        number = matcher.group(1)
        first = matcher.group(2)
        first_n = matcher.group(3)
        second = matcher.group(4)
        second_n = matcher.group(5)
        third = matcher.group(6)
        third_n = matcher.group(7)

        sues.append(Sue(number=number, 
                     first = first,
                     first_n = first_n,
                     second = second,
                     second_n = second_n,
                     third = third,
                     third_n = third_n))

for sue in sues:
    if sue.matches(description):
        print "A: " + sue.number
