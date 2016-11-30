import sys
import collections

inp = [x.strip() for x in sys.stdin.readlines()]

field = collections.defaultdict(dict)
new_field = collections.defaultdict(dict)

def get_val_at(x, y):
    if x < 0 or x >= len(field.keys()) or y < 0 or y >= len(field[x].keys()):
        return '.'
    else:
        return field[x][y]

def sum_neighbors_on(x, y):
    tot_sum = 0
    for x_1 in range(-1, 2):
        for y_1 in range(-1, 2):
            if x_1 == 0 and y_1 == 0:
                continue
            if get_val_at(x+x_1, y+y_1) == '#':
                tot_sum += 1
    return tot_sum

def check(x, y):
    sum_n = sum_neighbors_on(x, y)
    if field[x][y] == '#': #on
        if sum_n == 2 or sum_n == 3:
            return '#'
        else:
            return '.'
    else: #off
        if sum_n == 3:
            return '#'
        else:
            return '.'

def prep_b():
    field[0][0] = '#'
    field[len(field.keys())-1][0] = '#'
    field[0][len(field[0].keys())-1] = '#'
    field[len(field.keys())-1][len(field[0].keys())-1] = '#'

def simulate():
    global field, new_field
    for x in range(0, len(field.keys())):
        for y in range(0, len(field[x].keys())):
            new_field[x][y] = check(x, y)

    field = new_field.copy()
    prep_b()
    del new_field
    new_field = collections.defaultdict(dict)

def print_field():
    string = ""
    for x in range(0, len(field.keys())):
        for y in range(0, len(field[x].keys())):
            string += field[x][y]
        string += '\n'
    string += "--------------------"
    print string

l = 0
for line in inp:
    for i in range(0, len(line)):
        field[l][i] = line[i]
    pair = (l,i)
    l += 1

prep_b()

for _ in range(0, 100):
    #print_field()
    simulate()

sum = 0

for x in range(0, len(field.keys())):
    for y in range(0, len(field[x].keys())):
        if field[x][y] == '#':
            sum += 1

print str(sum)
