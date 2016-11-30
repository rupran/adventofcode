def gen_next(inp):
    retstr = ""
    cur_count = 1
    prev = None
    for char in inp:
        if prev and prev != char:
            retstr += "%d%c" % (cur_count, prev)
            cur_count = 1
        elif prev and prev == char:
            cur_count += 1
        prev = char
    retstr += "%d%c" % (cur_count, prev)
    return retstr

inp = "3113322113"

for _ in range(0, 50):
    inp = gen_next(inp)

print len(inp)
