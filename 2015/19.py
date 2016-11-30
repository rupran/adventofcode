import sys
import re

inp = [x.strip() for x in sys.stdin.readlines()]
replacements = {}
repl_reverse = {}
variants = set()

def generate_molecules(inp_string):
    for index in range(0, len(inp_string)):
        for key in replacements:
            if inp_string[index:index + len(key)] == key:
                for replacement in replacements[key]:
                    elems = []
                    elems.append(inp_string[:index])
                    elems.append(replacement)
                    elems.append(inp_string[index + len(key):])
                    variants.add("".join(elems))

def reduce_molecule(inp_string):
    count = 0
    pos_rep = sorted(repl_reverse.keys(), key = lambda x: -len(x))
    for rep in pos_rep:
        if rep in inp_string:
            inp_string = inp_string.replace(rep, repl_reverse[rep], 1)
            count += 1
    return (count, inp_string)

for line in inp:
    matcher = re.match("(\w+) => (\w+)", line)
    if matcher:
        if not matcher.group(1) in replacements:
            replacements[matcher.group(1)] = [matcher.group(2)]
        else:
            replacements[matcher.group(1)].append(matcher.group(2))
        if not matcher.group(2) in repl_reverse:
            repl_reverse[matcher.group(2)] = matcher.group(1)
        
        continue

    matcher = re.match("^(\w+)$", line)
    if matcher:
        molecule = matcher.group(1)

#print replacements
# Part A
generate_molecules(molecule)
print len(variants)

# Part B
in_str = molecule
total_count = 0
while in_str != "e":
    count, in_str = reduce_molecule(in_str)
    total_count += count

print total_count
