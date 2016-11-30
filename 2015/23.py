import sys

inp = [x.strip() for x in sys.stdin.readlines()]
regvals = {'a': 1, 'b': 0}

ip = 0
while ip < len(inp):
    instr = inp[ip][:3]
    par = inp[ip][4:]
    if instr == 'hlf':
        regvals[par] /= 2
    elif instr == 'tpl':
        regvals[par] *= 3
    elif instr == 'inc':
        regvals[par] += 1
    elif instr == 'jmp':
        ip += int(par)
        continue
    elif instr == 'jie':
        reg = par[0]
        offset = par[3:]
        if regvals[reg] % 2 == 0:
            ip += int(offset)
            continue
    elif instr == 'jio':
        reg = par[0]
        offset = par[3:]
        if regvals[reg] == 1:
            ip += int(offset)
            continue
    ip += 1

print regvals['b']
