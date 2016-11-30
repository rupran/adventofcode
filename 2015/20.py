import collections

n = 33100000

house = collections.defaultdict(int)
elf_count = collections.defaultdict(int)

for i in range(1, n/10+1):
    for j in range(i, n/10+1, i):
        # Part A: 
        house[j] += i*10
        # Part B:
#        if elf_count[i] >= 50:
#            continue
#        house[j] += i*11
#        elf_count[i] += 1

for i in range(1, len(house.keys())):
    if house[i] > n:
        print i
        break
