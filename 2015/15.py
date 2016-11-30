import sys
import re

class Ingredient:

    def __init__(self, name, cap, dur, fla, tex, cal):
        self.name = name
        self.cap = cap
        self.dur = dur
        self.fla = fla
        self.tex = tex
        self.cal = cal

ingredients = []
ingredients_counter = []

def calc_val(ingredients):
    cap = 0
    dur = 0
    fla = 0
    tex = 0
    for i in range(0, len(ingredients)):
        cap += ingredients_counter[i] * ingredients[i].cap
        dur += ingredients_counter[i] * ingredients[i].dur
        fla += ingredients_counter[i] * ingredients[i].fla
        tex += ingredients_counter[i] * ingredients[i].tex

    if any([x < 0 for x in [cap, dur, fla, tex]]):
        return 0

    return reduce(lambda x, y: x*y, [cap, dur, fla, tex])

def calc_cal(ingredients):
    retval = 0
    for i in range(0, len(ingredients)):
        retval += ingredients_counter[i] * ingredients[i].cal
    return retval


def backpack(depth, max_dep, cur_index):
    if depth == max_dep:
        if calc_cal(ingredients) == 500:
            return calc_val(ingredients)
        else:
            return 0
    if cur_index >= len(ingredients):
        return 0

    sol1 = backpack(depth, max_dep, cur_index + 1)
    ingredients_counter[cur_index] += 1
    sol2 = backpack(depth+1, max_dep, cur_index)
    ingredients_counter[cur_index] -= 1

    retval = max(sol1, sol2)
    return retval

inp = [x.strip() for x in sys.stdin.readlines()]

for line in inp:
    matcher = re.match("(\w+)\: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line)
    if matcher:
        ingredients.append(Ingredient(matcher.group(1),
                                      int(matcher.group(2)),
                                      int(matcher.group(3)),
                                      int(matcher.group(4)),
                                      int(matcher.group(5)),
                                      int(matcher.group(6))))
        ingredients_counter.append(0)

print (backpack(0, 100, 0))
