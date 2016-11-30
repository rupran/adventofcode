def increment(in_str):
    rev_str = list(reversed(in_str))
    out_str = []
    overflow = True
    index = 0
    while overflow:
        overflow = False
        c = rev_str[index]
        if c == 'z':
            out_str.append('a')
            overflow = True
        else:
            out_str.append(chr(ord(c) + 1))
        index += 1

    out_str.extend(rev_str[index:])

    return "".join(list(reversed(out_str)))

def is_valid(password):
    pairs = set((password[i], password[i+1]) for i in range(0, len(password)-1) if password[i] == password[i+1])
    triplets = set((password[i], password[i+1], password[i+2]) for i in range(0, len(password)-2))
    increasing_series = set(x for x in triplets if ord(x[1]) == ord(x[0]) + 1 and ord(x[2]) == ord(x[1]) + 1)
    
    req1 = len(increasing_series) > 0
    req2 = not (("i" in password) | ("o" in password) | ("l" in password))
    req3 = len(pairs) >= 2

    return req1 & req2 & req3

inp = "vzbxkghb"
while not is_valid(inp):
    inp = increment(inp)

print "A: " + inp
inp = increment(inp)
while not is_valid(inp):
    inp = increment(inp)

print "B: " + inp
