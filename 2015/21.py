import sys

# (Cost, Damage, Armor)
weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
armor   = [(13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
rings   = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]

def get_all_combinations_of_rings():
    retval = []
    for i in range(0, len(rings)):
        c1, d1, a1 = rings[i]
        # Only ring i
        retval.append((c1, d1, a1))
        for j in range(i + 1, len(rings)):
            c2, d2, a2 = rings[j]
            # Rings i and j
            retval.append((c1+c2,d1+d2,a1+a2))
    return retval

boss_hp = 100
boss_armor = 2
boss_damage = 8

my_hp = 100

all_combinations = []

all_rings = get_all_combinations_of_rings()
for i in range(0, len(weapons)):
    # Weapon only
    all_combinations.append(weapons[i])

    # Without any armor, but with rings
    cw, dw, aw = weapons[i]
    for (cr, dr, ar) in all_rings:
        all_combinations.append((cw+cr, dw+dr, aw+ar))

    # Now with armor:
    for j in range(0, len(armor)):
        ca, da, aa = armor[j]
        for (cr, dr, ar) in all_rings:
            all_combinations.append((cw+ca+cr, dw+da+dr, aw+aa+ar))

#print len(all_combinations)
min_cost = 999
max_cost = 0
combination = None

for c, d, a in all_combinations:
    my_hits = boss_hp / (max(d - boss_armor, 1))    # Hits until boss_hp <= 0
    boss_hits = my_hp / (max(boss_damage - a, 1))   # Hits until my_hp <= 0
    # Part A
    if my_hits <= boss_hits:
        if c < min_cost:
            min_cost = c
    # Part B
    else:
        if c > max_cost:
            max_cost = c

print "A: " + str(min_cost)
print "B: " + str(max_cost)
